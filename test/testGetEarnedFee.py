import unittest
import sys 
sys.path.append('..')
import feeCalculator


class TestGetEarnedFee(unittest.TestCase):

    def testCase1(self): # tick is covered by the range
        prevTick = 10
        curTick = 15
        tickRange = [10,30]
        feeTier = 0.01
        
        realEarnedFee = 0.0025
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")

    def testCase2(self): # tick is covered by the range, with different fee tier
        prevTick = 10
        curTick = 15
        tickRange = [10,30]
        feeTier = 0.03
        
        realEarnedFee = 0.0075
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")

    def testCase3(self): # tick is not moving 
        prevTick = 10
        curTick = 10
        tickRange = [10,30]
        feeTier = 0.01

        realEarnedFee = 0
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")   
    
    def testCase4(self): # tick is not in the range 
        prevTick = 8
        curTick = 9
        tickRange = [10,30]
        feeTier = 0.01

        realEarnedFee = 0
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")   

    def testCase5(self): # tick is crossing lower bound 
        prevTick = 9
        curTick = 12
        tickRange = [10,30]
        feeTier = 0.01

        realEarnedFee = 0.001
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")   
    
    def testCase6(self): # tick is crossing lower bound 
        prevTick = 32
        curTick = 25
        tickRange = [10,30]
        feeTier = 0.01

        realEarnedFee = 0.0025
        testedEarnedFee = feeCalculator.getEarnedFee(prevTick, curTick, tickRange, feeTier)
        
        self.assertEqual(realEarnedFee, testedEarnedFee, "Calculation is wrong")

if __name__ == '__main__':
    unittest.main()
  
