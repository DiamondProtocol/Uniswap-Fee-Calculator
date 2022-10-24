# the backtest period for Fee APR and the range we wanna test on
backtestParams = {
    "period": 3,  # backtest based on the past 3 days of data
    "tickNumber": 5000  # backtest based on a 50% range of liquidity provision
}
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
# the subgraph url we use to query data from different chains
subgraphURLs = {
    "Arbitrum": "https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-minimal",
    "Optimism": "https://api.thegraph.com/subgraphs/name/ianlapham/optimism-post-regenesis",
    "Polygon": "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-polygon"}
