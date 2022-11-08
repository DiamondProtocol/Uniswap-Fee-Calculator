import unittest
import sys 
import pandas as pd 
import os
import time 
sys.path.append('..')
import config 
import random
import feeCalculator

class TestRaw2CSV(unittest.TestCase):
    def testCase1(self):
        configData = config.config["ARB_WETHUSDC_0.05%"]
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        feeCalculator.Raw2CSV(configData)
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        rowData = data.iloc[random.randint(0,len(data))]
            
        self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
        self.assertTrue(int(rowData['block_time']) <= int(time.time()), "timestamp exceeds current time")
        self.assertEqual(rowData['block_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertEqual(rowData['tx_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertTrue(int(rowData['log_index']) >= 0, "logIndex < 0")
        self.assertTrue(int(rowData['price']) >= 0, "price < 0")

    def testCase2(self):
        configData = config.config["ARB_GMXWETH_1%"]
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        feeCalculator.Raw2CSV(configData)
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        rowData = data.iloc[random.randint(0,len(data))]
            
        self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
        self.assertTrue(int(rowData['block_time']) <= int(time.time()), "timestamp exceeds current time")
        self.assertEqual(rowData['block_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertEqual(rowData['tx_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertTrue(int(rowData['log_index']) >= 0, "logIndex < 0")
        self.assertTrue(int(rowData['price']) >= 0, "price < 0")
        
    def testCase3(self):
        configData = config.config["OP_WETHUSDC_0.05%"]
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
        feeCalculator.Raw2CSV(configData)
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        rowData = data.iloc[random.randint(0,len(data))]
            
        self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
        self.assertTrue(int(rowData['block_time']) <= int(time.time()), "timestamp exceeds current time")
        self.assertEqual(rowData['block_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertEqual(rowData['tx_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertTrue(int(rowData['log_index']) >= 0, "logIndex < 0")
        self.assertTrue(int(rowData['price']) >= 0, "price < 0")
        
    def testCase4(self):
        configData = config.config["MATIC_WETHUSDC_0.05%"]
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
        feeCalculator.Raw2CSV(configData)
        data = pd.read_csv(f'{scriptDir}/data/{ticker}_swap.csv')
        rowData = data.iloc[random.randint(0,len(data))]
            
        self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
        self.assertTrue(int(rowData['block_time']) <= int(time.time()), "timestamp exceeds current time")
        self.assertEqual(rowData['block_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertEqual(rowData['tx_hash'][:2],"0x" , "block_hash should start with 0x")
        self.assertTrue(int(rowData['log_index']) >= 0, "logIndex < 0")
        self.assertTrue(int(rowData['price']) >= 0, "price < 0")
        
            
            
if __name__ == '__main__':
    unittest.main()
  