import unittest
import os
import os.path
import sys
from mock import *
sys.path.append('../../src/')

from rate_calculator import *

class FileCounter:
	def __init__(self):
		self.fileCount = 0

	def getFileCount(self):
		return self.fileCount

	def count(self, file):
			self.fileCount += 1 

class FileEnumeratorTestCase(unittest.TestCase):
	def testFileEnumerator(self):
		enumerator = FileEnumerator('fixture\module_foo')
		counter = FileCounter()
		enumerator.enumerate(counter.count)
		self.assertEqual(3, counter.getFileCount())

# MAIN program ---------------------------------------------------
if __name__ == "__main__":
	unittest.main()

