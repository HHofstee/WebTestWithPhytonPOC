import unittest
import time
from selenium import webdriver

class BenchPythonSel(unittest.TestCase):

	def setUp(self):
		self.startTime = time.time()
	
	def test_url_phantom(self):
		time.sleep(1)
		self.driver = webdriver.PhantomJS()
		self.driver.get("http://google.com")
		self.assertIn('Google', self.driver.title)
		print "success"
		
	def endTest(self):
		t = time.time() - self.startTime
		print "%s: %.3f" % (self.id(), t)
		self.driver.exit()
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BenchPythonSel)
    unittest.TextTestRunner(verbosity=0).run(suite)
