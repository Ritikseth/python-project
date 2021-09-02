# import unittest
# import testing_main

# class TestMain(unittest.TestCase):
# 	def setUp(self):
# 		print('Gonna start the test')
# 	def test_do_stuff(self):
# 		'''Hiiiiii'''
# 		test_param=10
# 		result = testing_main.do_stuff(test_param)
# 		self.assertEqual(result,15)

# 	def test_do_stuff2(self):
# 		test_param='ieivee'
# 		result = testing_main.do_stuff(test_param)
# 		self.assertIsInstance(result,ValueError)

# 	def test_do_stuff3(self):
# 		test_param=None
# 		result = testing_main.do_stuff(test_param)
# 		self.assertEqual(result,'please enter a number')

# 	def test_do_stuff4(self):
# 		test_param=''
# 		result = testing_main.do_stuff(test_param)
# 		self.assertEqual(result,'please enter a number')

# 	def test_do_stuff5(self):
# 		test_param=0
# 		result = testing_main.do_stuff(test_param)
# 		self.assertEqual(result,'number can\'t be zero')

import unittest
import testing_main

class TestMain(unittest.TestCase):
	def test_check_guess(self):
		test_param=5



if __name__=='__main__':
	unittest.main()