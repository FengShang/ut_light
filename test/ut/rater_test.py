import unittest
import os
import os.path
import sys
sys.path.append('../../src/')
from rate_calculator import *

class RaterTestSuite(unittest.TestCase):
	def dummyEnumerate(self, files, callback):
		for f in files:
			callback(f, 1)  

	def testRateForCpp(self):
		rater = Rater()
		files = ['a.h', 'a.cpp', 'a.hpp', 'a.cc', 'a.c', 'test_a.cpp']	
		self.dummyEnumerate(files, rater.rate)
		m = rater.module()
		self.assertEqual(5, m.codeSize)
		self.assertEqual(1, m.testingSize)

	def testRateForMixedLanguage(self):
		rater = Rater()
		files = ['a.cpp', 'b.h', 'c.cc', 'x.py', 'test_foo.cpp', 'test_a.py']	
		self.dummyEnumerate(files, rater.rate)
		m = rater.module()
		self.assertEqual(3, m.codeSize)
		self.assertEqual(1, m.testingSize)

	def testRateForPython(self):
		rater = Rater()
		files = ['a.py', 'test_a.py']	
		self.dummyEnumerate(files, rater.rate)
		m = rater.module()
		self.assertEqual(1, m.codeSize)
		self.assertEqual(1, m.testingSize)





# MAIN program ---------------------------------------------------
if __name__ == "__main__":
	unittest.main()


