import csv
from distutils.command.config import config
import json
import os
import requests
import pandas as pd
from pathlib import Path

# chain can be "Arbitrum", "Optimism", "Polygon"
# pool is the pool address


def fetchData(
        configData,
        subgraphURL,
        startTime=1652000000,
        endTime=1652089128,
        force=True):
    # pull data from configData
    chain = configData['chain']
    pool = configData['pool']
    ticker = configData['ticker']

    columns = """{
    amount0
    amount1
    timestamp
    sender
    sqrtPriceX96
    tick
    logIndex
    transaction { id\\n blockNumber}
}""".split("\n")

    columns = "\\n".join(columns)

    cousorTime = startTime
    timeStep = 86400
    scriptDir = Path(__file__).parent.absolute()
    rawDataFilePath = f'{scriptDir}/data/{ticker}_swap.txt'
    if force:
        if os.path.exists(rawDataFilePath):
            os.remove(rawDataFilePath)
    else:
        assert os.path.exists(
            rawDataFilePath), f'{rawDataFilePath} already existing.'
    f = open(rawDataFilePath, "a")
    totalCount = 0
    while cousorTime < endTime:
        dpayload = '{"query":"{\\n swaps(first: 1000, orderBy: timestamp, orderDirection: asc, where:' + \
            '{ pool: \\"' + pool + '\\", '
        dpayload += 'timestamp_lte: ' + str(cousorTime + timeStep)
        dpayload += ', timestamp_gt: ' + str(cousorTime) + '}) '
        dpayload += columns + '\\n}\\n","variables":null}'
        data = dpayload

        headers = {
            'cache-control': 'no-cache',
            'content-type': 'application/json'
        }
        response = requests.post(subgraphURL, headers=headers, data=data)
        jdata = response.json()

        tmpCousorTime = cousorTime
        if response.status_code == 200:
            for o in jdata["data"]["swaps"]:
                dataTimestamp = int(o["timestamp"])
                tmpCousorTime = dataTimestamp
                totalCount += 1
                f.write(json.dumps(o) + "\n")
            cousorTime = tmpCousorTime
            print(tmpCousorTime)
        else:
            print(
                f'${cousorTime} response.status_code: ${response.status_code}, will retry')
    f.close()
    print(f'total counts: {totalCount}')


def Raw2CSV(configData, switch=False):
    # pull data from configData
    chain = configData['chain']
    pool = configData['pool']
    ticker = configData['ticker']

    scriptDir = Path(__file__).parent.absolute()
    file1 = open(f'{scriptDir}/data/{ticker}_swap.txt', 'r')
    lines = file1.readlines()
    if len(lines) != 0:
        fileOutputDir = f'{scriptDir}'
        if not os.path.exists(fileOutputDir):
            os.mkdir(fileOutputDir)
        fileOutputFileth = f'{fileOutputDir}/data/{ticker}_swap.csv'
        if os.path.exists(fileOutputFileth):
            os.remove(fileOutputFileth)
        f = open(fileOutputFileth, 'w')
        cwriter = csv.writer(f)
        header = [
            "pool",
            "block_number",
            "block_hash",
            "block_time",
            "log_index",
            "tx_hash",
            "sender",
            "recipient",
            "amount0",
            "amount1",
            "sqrt_price_x96",
            "liquidity",
            "price",
            "tick"]
        cwriter.writerow(header)

        blockNumber = 0
        for line in lines:
            o = json.loads(line)
            sqrtPriceX96 = int(o["sqrtPriceX96"])
            if switch:
                price = 2 ** 192 / (sqrtPriceX96 ** 2)
            else:
                price = ((sqrtPriceX96 * (10 ** 6)) ** 2) / (2 ** 192)

            row = [
                # "pool", "block_number"
                "mypool", o['transaction']['blockNumber'],
                # "block_hash", "block_time"
                o['transaction']["id"], o["timestamp"],
                # "log_index", "tx_hash"
                int(o["logIndex"]), o['transaction']["id"],
                # "sender", "recipient"
                "sender", "recipient",
                # "amount0", "amount1
                float(o["amount0"]), float(o["amount1"]),
                # sqrt_price_x96
                int(o["sqrtPriceX96"]),
                # "liquidity", "price"
                0, price,
                # "tick"
                int(o['tick'])
                # math.floor(math.log(price) / math.log(1.0001))
                # or o['tick'] ?
            ]
            blockNumber += 1
            cwriter.writerow(row)
    file1.close()
    f.close()

# TickRange = something like [100,200]


def getEarnedFee(prevTick, curTick, tickRange, feeTier):
    if prevTick >= tickRange[0] and prevTick <= tickRange[1] and curTick >= tickRange[0] and curTick <= tickRange[1]:  # In range
        # ROI made from the swap
        earnedFee = abs(curTick - prevTick) / \
            (tickRange[1] - tickRange[0]) * feeTier

        return earnedFee
    elif prevTick < tickRange[0] < curTick:
        earnedFee = abs(curTick - tickRange[0]) / \
            (tickRange[1] - tickRange[0]) * feeTier
        return earnedFee
    elif prevTick > tickRange[1] > curTick:
        earnedFee = abs(curTick - tickRange[1]) / \
            (tickRange[1] - tickRange[0]) * feeTier
        return earnedFee
    else:  # if out-of-range, no fee
        return 0


def getFeeAPR(configData, tickNumber, data):

    chain = configData['chain']
    pool = configData['pool']
    feeTier = configData['feeTier']
    ticker = configData['ticker']

    # put data in order, sort by [timestamp, log_index]
    data = data.drop_duplicates(subset=["tx_hash"], keep="first")
    data = data.sort_values(by=['block_number'])
    data = data.sort_values(
        ['block_number', 'log_index'], ascending=[True, True])
    data['prevTick'] = data['tick'].shift(1)
    data = data.iloc[1:]

    # backtest Fee APR
    noPosition = True
    culmulativeFee = 0
    for index, value in data.iterrows():
        if noPosition:  # initialize tickRange
            tickRange = [
                value['tick'] - tickNumber,
                value['tick'] + tickNumber]
            noPosition = False
        else:
            earnedFee = getEarnedFee(
                value['prevTick'], value['tick'], tickRange, feeTier)
            culmulativeFee += earnedFee

    backtestDays = (data.iloc[-1]['block_time'] -
                    data.iloc[0]['block_time']) / 86400  # days

    # calculate Fee APR (%) based on tickNumber liquidity
    feeAPR = culmulativeFee * 365 / backtestDays * 100

    return {ticker: feeAPR}
