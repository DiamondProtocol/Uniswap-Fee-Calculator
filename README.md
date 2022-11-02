# Uniswap Fee Calculator 
[![](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/downloads/) <br>
Uniswap Fee Calculator is a tool for you to get the approximated fee APR from every trading pair on Uniswap. <br> Currently it supports Polygon, Optimism, and Arbitrum. Users can easily expand the supported trading pairs and chains by editing the config file. 

## Getting Started 
```bash
git clone git@github.com:ZooWallet/Uniswap-Fee-Calculator.git
cd uniswap-fee-calculator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Get Fee APR
```python
UniswapAPRs = getUniswapAPRs() 
```

## Behind The Scenes 
1. `fetchData(chain, pool, startTime, endTime)` pulls raw data from Subgraph, and save it to a .txt file with raw data in it
2. `Raw2CSV(chain,pool)` handles the raw data and put it into a human-readable csv file
3. `getFeeAPR(chain,pool,tickNumber,feeTier)` reads corresponding csv file and calculate Fee APR, and return a dictionary
4. Based on the preset config file, every time a user calls `getUniswapAPRs()`, the program runs all of the above and return a dictionary of Fee APR

## Code Breakdown 

### config.py
Keeps all the parameters, including: <br> 

`backtestParams`: how many days of data is used for the backtest, and the liquidity range for the backtest <br> 
```python
# the backtest period for Fee APR and the range we wanna test on 
backtestParams = {
    "period" : 3, # backtest based on the past 3 days of data
    "tickNumber" : 5000 # backtest based on a 50% range of liquidity provision 
}
```

`config`: All the info for supported trading pairs, need to manually add it if user wants to support additional pairs <br> 
```python
# the pair info, have to manually add/remove this config variable if we
# want get fee apr for more pairs
config = {
    "ARB_WETHUSDC_0.05%": {
        "ticker": "ARB_WETHUSDC_0.05%",
        "chain": "Arbitrum",
        "pool": "0xc31e54c7a869b9fcbecc14363cf510d1c41fa443",
        "feeTier": 0.0005
    },
    "ARB_GMXWETH_1%": {
        "ticker": "ARB_GMXWETH_1%",
        "chain": "Arbitrum",
        "pool": "0x80a9ae39310abf666a87c743d6ebbd0e8c42158e",
        "feeTier": 0.01
    },
    "OP_WETHUSDC_0.05%": {
        "ticker": "OP_WETHUSDC_0.05%",
        "chain": "Optimism",
        "pool": "0x85149247691df622eaf1a8bd0cafd40bc45154a9",
        "feeTier": 0.0005
    },
    "MATIC_WETHUSDC_0.05%": {
        "ticker": "MATIC_WETHUSDC_0.05%",
        "chain": "Polygon",
        "pool": "0x45dda9cb7c25131df268515131f647d726f50608",
        "feeTier": 0.0005
    }

}
```

`subgraphURLs`: the subgraph query URLs for different chains <br> 
```python
# the subgraph url we use to query data from different chains
subgraphURLs = {
    "Arbitrum": "https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-minimal",
    "Optimism": "https://api.thegraph.com/subgraphs/name/ianlapham/optimism-post-regenesis",
    "Polygon": "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-polygon"}
```

### feeCalculator.py
There are four functions: <br>
`fetchData()`: Based on the input params, pulling data from Subgraph and save it to a .txt file <br>
`Raw2CSV()`: Handles the raw data and put it into a human-readable csv file <br>
`getEarnedFee()`: Calculates the Fee APR for a single swap <br>
`getFeeAPR()`: Reads corresponding csv file and calculate Fee APR, and return a dictionary <br>

### run.py
Traverse each trading pair in `config.py` to calculate the fee APR for each of them. Will return a dictionary of Fee APRs. 

