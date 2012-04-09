import unittest
import os
import os.path
import sys
sys.path.append('../../src/')

from rate_calculator import *

class IntegrationTestCase(unittest.TestCase):
	def testCalculateRateOfTestAndProductCode(self):
		calculator = RateCalculator()
		rate = calculator.calculate("./test/ut/fixture/module_foo")
		self.assertEqual(0.5, rate)


	def suite():
		suite = unittest.TestSuite()
		suite.addTest(unittest.makeSuite(testsuit_A, 'test'))
		return suite

# MAIN program ---------------------------------------------------
if __name__ == "__main__":
	unittest.main()

