import os.path
import fnmatch

class RateCalculator:
	def __init__(self):
		return

	def calculate(self, folder):
		return 0


class FileEnumerator:
	def __init__(self, dir):
		self.dir = dir

	def enumerate(self, callback):
		self.callback = callback
		os.path.walk(self.dir, self.preCallback, None)

	def preCallback(self, arg, dir, files):
		for f in files:
			fullname = os.path.join(dir, f)
			if os.path.isfile(fullname):
				self.callback(f)

class Module:
	pass

class TestingCode:
	def match(self, file):
		return file.lower().find("test") != -1

class Rater:
	def __init__(self):
		self.typeFilter = {'cpp': '*.cpp;*.c;*.cc;*.h;*.hpp', 
				'cpp_test': '*Test.c*;*test.c*;test*.c*;*test.c*', 
				'java': '*.java', 
				'java_test': '*test.java;test*.java;Test*.java;*Test.java', 
				'php': '*.php', 
				'php_test': '*test.php;test*.php;Test*.php;*Test.php', 
				'python': '*.py', 
				'python_test': '*test.py;test*.py;Test*.py;*Test.py', }
		self.rateRecord = {}
		for k,v in self.typeFilter.iteritems():
			print "init:" , k
			self.rateRecord[k] = 0


	def rate(self, file, size):
		for k,v in self.typeFilter.iteritems():
			wildcards = v.split(';')
			for wildcard in wildcards:
				if fnmatch.fnmatch(file, wildcard):
					print "file:", file, " rate:" , k, " size: ", size
					self.rateRecord[k] += size

	def rate2(self, file, size):
		if ( testing.match(file) ):
			self.rateTestingCode(file, size)
		else:
			self.rateCode(file, size)

	def module(self):
		max = 0;
		key = '';
		for k,v in self.rateRecord.iteritems():
			print "module", k,v
			if (k.find('test') == -1) and ( v - self.rateRecord[k+'_test'] > max):
				max =  v - self.rateRecord[k+'_test']
				key = k
		print '---------------------'
		module = Module()
		module.codeSize = max
		module.testingSize = self.rateRecord[key+'_test']
		return module


