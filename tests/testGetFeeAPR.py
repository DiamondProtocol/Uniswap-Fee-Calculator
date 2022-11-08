import unittest
import sys 
import pandas as pd 
import os
import time 
sys.path.append('..')
import config 
import random
import feeCalculator

class TestGetFeeAPR(unittest.TestCase):
    def testCase1(self): # read ARB WETH-USDC 0.05% data
        configData = config.config["ARB_WETHUSDC_0.05%"]
        tickNumber = 1500 # 15%
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        feeAPRs = feeCalculator.getFeeAPR(configData, tickNumber, data)
        print(feeAPRs)
        self.assertIs(type(feeAPRs),dict, "fee APR should be a dictionary")
        self.assertTrue(feeAPRs[ticker] >= 0, "fee APR should not be negative")
        
    def testCase2(self): # read ARB GMX-WETH 1% data
        configData = config.config["ARB_GMXWETH_1%"]
        tickNumber = 1500 # 15%
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        feeAPRs = feeCalculator.getFeeAPR(configData, tickNumber, data)
        print(feeAPRs)
        self.assertIs(type(feeAPRs),dict, "fee APR should be a dictionary")
        self.assertTrue(feeAPRs[ticker] >= 0, "fee APR should not be negative")
    
    def testCase3(self):
        configData = config.config["OP_WETHUSDC_0.05%"]
        tickNumber = 1500 # 15%
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        feeAPRs = feeCalculator.getFeeAPR(configData, tickNumber, data)
        print(feeAPRs)
        self.assertIs(type(feeAPRs),dict, "fee APR should be a dictionary")
        self.assertTrue(feeAPRs[ticker] >= 0, "fee APR should not be negative")

    def testCase4(self):
        configData = config.config["MATIC_WETHUSDC_0.05%"]
        tickNumber = 1500 # 15%
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        feeAPRs = feeCalculator.getFeeAPR(configData, tickNumber, data)
        print(feeAPRs)
        self.assertIs(type(feeAPRs),dict, "fee APR should be a dictionary")
        self.assertTrue(feeAPRs[ticker] >= 0, "fee APR should not be negative")
                         
            
if __name__ == '__main__':
    unittest.main()
  