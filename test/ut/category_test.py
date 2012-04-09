import unittest
import sys
sys.path.append('../../src/')
from rate_calculator import *

class CategoryTestSuite(unittest.TestCase):
	def testMatchTestingCategory(self):
		testingCode= TestingCode()
		self.assertTrue(testingCode.match("test_a.py"))
		self.assertTrue(testingCode.match("a_test.py"))
		self.assertTrue(testingCode.match("test_a.py"))
		self.assertTrue(testingCode.match("a_TeSt.py"))
		self.assertTrue(testingCode.match("a_Test_b.py"))
		self.assertTrue(testingCode.match("a_teSt_b.py"))


if __name__ == "__main__":
	unittest.main()

