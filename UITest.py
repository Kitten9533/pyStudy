#coding=utf-8
# !/usr/bin/env python
#port os
import os,subprocess
import unittest
import logging
from appium import webdriver
from time import sleep

#类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
	#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '8.0'
		desired_caps['deviceName'] = '988954465155325349'
		desired_caps['appPackage'] = 'com.resell.df'
		desired_caps['appActivity'] = '.MainActivity'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.windowSize = self.driver.get_window_size()
		self.x = self.driver.get_window_size()['width']
		self.y = self.driver.get_window_size()['height']

	#tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出
	def tearDown(self):
		# self.driver.close_app()
		# self.driver.quit()
		pass

	#跳过引导
	def testCase001(self):
		sleep(5)
		# self.driver.find_element_by_id('com.android.calculator2:id/digit9').click()
		print(self.windowSize)
		self.driver.swipe(0.9*self.x, 0.75*self.y, 0.1*self.x, 0.75*self.y, 300)
		sleep(2)
		self.driver.swipe(0.9*self.x, 0.75*self.y, 0.1*self.x, 0.75*self.y, 300)
		# d(className="android.widget.ImageView", instance=15).click()

#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
	unittest.TextTestRunner(verbosity=2).run(suite)