import unittest
import sys 
from pathlib import Path
import pandas as pd 
import os
import time 
import json 
sys.path.append('..')
import config 
import feeCalculator
import random

class TestFetchData(unittest.TestCase):
    # def testCase1(self):
    #     configData = config.config["ARB_WETHUSDC_0.05%"]
    #     subgraphURL = config.subgraphURLs['Arbitrum']
    #     endTime = int(time.time()) - 3600
    #     startTime = endTime - 3600 # 1 hr
    #     # fetch data
    #     print('fetching data')
    #     feeCalculator.fetchData(configData,subgraphURL,startTime,endTime)
    #     # read txt file 
    #     ticker = configData['ticker']
    #     scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     file1 = open(f'{scriptDir}/data/{ticker}_swap.txt', 'r')
    #     lines = file1.readlines()
        
    #     # test first & last line 
    #     pickedLines = [lines[random.randint(0, len(lines))],lines[random.randint(0, len(lines))]] # get two random data

    #     for line in pickedLines:
    #         rowData = json.loads(line)
    #         self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
    #         self.assertTrue(int(rowData['timestamp']) <= int(time.time()), "timestamp exceeds current time")
    #         self.assertEqual(rowData['sender'][:2],"0x" , "sender should be an address")
    #         self.assertTrue(int(rowData['logIndex']) >= 0, "logIndex < 0")
    #         self.assertIs(type(rowData['transaction']),dict, "transaction column is not dictionary")

    #     file1.close()

    # def testCase2(self):
    #     configData = config.config["OP_WETHUSDC_0.05%"]
    #     subgraphURL = config.subgraphURLs['Optimism']
    #     endTime = int(time.time()) - 3600
    #     startTime = endTime - 3600 # 1 hr
    #     # fetch data
    #     print('fetching data')
    #     feeCalculator.fetchData(configData,subgraphURL,startTime,endTime)
    #     # read txt file 
    #     ticker = configData['ticker']
    #     scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     file1 = open(f'{scriptDir}/data/{ticker}_swap.txt', 'r')
    #     lines = file1.readlines()
        
    #     # test first & last line 
    #     pickedLines = [lines[random.randint(0, len(lines))],lines[random.randint(0, len(lines))]] # get two random data

    #     for line in pickedLines:
    #         rowData = json.loads(line)
    #         self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
    #         self.assertTrue(int(rowData['timestamp']) <= int(time.time()), "timestamp exceeds current time")
    #         self.assertEqual(rowData['sender'][:2],"0x" , "sender should be an address")
    #         self.assertTrue(int(rowData['logIndex']) >= 0, "logIndex < 0")
    #         self.assertIs(type(rowData['transaction']),dict, "transaction column is not dictionary")

    #     file1.close()

    # def testCase3(self):
    #     configData = config.config["MATIC_WETHUSDC_0.05%"]
    #     subgraphURL = config.subgraphURLs['Polygon']
    #     endTime = int(time.time()) - 3600
    #     startTime = endTime - 3600 # 1 hr
    #     # fetch data
    #     print('fetching data')
    #     feeCalculator.fetchData(configData,subgraphURL,startTime,endTime)
    #     # read txt file 
    #     ticker = configData['ticker']
    #     scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     file1 = open(f'{scriptDir}/data/{ticker}_swap.txt', 'r')
    #     lines = file1.readlines()
        
    #     # test first & last line 
    #     pickedLines = [lines[random.randint(0, len(lines))],lines[random.randint(0, len(lines))]] # get two random data

    #     for line in pickedLines:
    #         rowData = json.loads(line)
    #         self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
    #         self.assertTrue(int(rowData['timestamp']) <= int(time.time()), "timestamp exceeds current time")
    #         self.assertEqual(rowData['sender'][:2],"0x" , "sender should be an address")
    #         self.assertTrue(int(rowData['logIndex']) >= 0, "logIndex < 0")
    #         self.assertIs(type(rowData['transaction']),dict, "transaction column is not dictionary")

    #     file1.close()

    def testCase4(self):
        configData = config.config["ARB_GMXWETH_1%"]
        subgraphURL = config.subgraphURLs['Arbitrum']
        endTime = int(time.time()) - 7200
        startTime = endTime - 86400
        # fetch data
        print('fetching data')
        feeCalculator.fetchData(configData,subgraphURL,startTime,endTime)
        # read txt file 
        ticker = configData['ticker']
        scriptDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file1 = open(f'{scriptDir}/data/{ticker}_swap.txt', 'r')
        lines = file1.readlines()
        
        # test first & last line 
        pickedLines = [lines[random.randint(0, len(lines))],lines[random.randint(0, len(lines))]] # get two random data

        for line in pickedLines:
            rowData = json.loads(line)
            self.assertTrue(float(rowData['amount0']) * float(rowData['amount1']) <= 0, "same direction of swap")
            self.assertTrue(int(rowData['timestamp']) <= int(time.time()), "timestamp exceeds current time")
            self.assertEqual(rowData['sender'][:2],"0x" , "sender should be an address")
            self.assertTrue(int(rowData['logIndex']) >= 0, "logIndex < 0")
            self.assertIs(type(rowData['transaction']),dict, "transaction column is not dictionary")

        file1.close()


if __name__ == '__main__':
    unittest.main()
  