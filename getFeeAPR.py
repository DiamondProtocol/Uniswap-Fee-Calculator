import time
from pathlib import Path
import pandas as pd 
from feeCalculator import fetchData, Raw2CSV, getFeeAPR
from config import config, subgraphURLs, backtestParams
import json

# get backtest params
# day means how many days of average fee APR we wanna use
# tickNumber means the range we wanna backtest, default = 5000 means 50% range


def getUniswapFeeAPRs():
    UniswapFeeAPRs = {}
    period = backtestParams['period']
    tickNumber = backtestParams['tickNumber']

    # traverse and get the pool info for each trading pair
    for pair in config:
        configData = config[pair]
        chain = configData['chain']
        pool = configData['pool']
        ticker = configData['ticker']
        feeTier = configData['feeTier']
        subgraphURL = subgraphURLs[chain]

        # get data from subgraph
        # In case error occurs when subgraph data is not up to date
        endTime = int(time.time()) - 7200
        startTime = endTime - 86400 * period
        
        print(pair)
        print('fetching data...')
        fetchData(configData, subgraphURL, startTime, endTime)
        # put data into readable CSV
        print('transforming data...')
        Raw2CSV(configData)
        # calculate Fee APR based on the params
        # return a dict
        data = pd.read_csv(f'data/{ticker}_swap.csv')
        uniswapFeeAPR = getFeeAPR(configData, tickNumber, data)
        UniswapFeeAPRs = {**UniswapFeeAPRs, **uniswapFeeAPR}

    return UniswapFeeAPRs


if __name__ == '__main__':
    UniswapFeeAPRs = getUniswapFeeAPRs()
    with open('result.json', 'w') as fp:
        json.dump(UniswapFeeAPRs, fp)