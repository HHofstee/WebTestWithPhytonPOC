import unittest
from selenium import webdriver

class BenchPythonSel(unittest.TestCase):

	def test_url_phantom(self):
		self.driver = webdriver.PhantomJS()
		self.driver.get("http://google.com")
		self.assertIn('not the rigth title', self.driver.title)
		print "success"
		
	def endTest(self):
		print "%s: %.3f" % (self.id(), t)
		self.driver.exit()
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BenchPythonSel)
    unittest.TextTestRunner(verbosity=0).run(suite)
