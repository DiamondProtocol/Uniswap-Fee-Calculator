import time
from pathlib import Path
from feeCalculator import fetchData, Raw2CSV, getFeeAPR
from config import config, subgraphURLs, backtestParams

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
        subgraphURL = subgraphURLs[chain]
        feeTier = configData['feeTier']

        # get data from subgraph
        # In case error occurs when subgraph data is not up to date
        endTime = int(time.time()) - 3600
        startTime = endTime - 86400 * period
        fetchData(configData, subgraphURL, startTime, endTime)
        # put data into readable CSV
        Raw2CSV(configData)
        # calculate Fee APR based on the params
        # return a dict
        uniswapFeeAPR = getFeeAPR(configData, tickNumber)
        UniswapFeeAPRs = {**UniswapFeeAPRs, **uniswapFeeAPR}

    return UniswapFeeAPRs
