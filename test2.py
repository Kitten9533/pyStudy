#coding=utf-8
# !/usr/bin/env python
#port os
import os,subprocess
import unittest
import logging
from appium import webdriver
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
	#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.1'
		desired_caps['deviceName'] = '7SDMOJEM99999999'
		desired_caps['appPackage'] = 'com.resell.df'
		desired_caps['appActivity'] = '.MainActivity'
		desired_caps['noRest'] = True
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
		def skip():
			sleep(5)
			# self.driver.find_element_by_id('com.android.calculator2:id/digit9').click()
			print(self.windowSize)
			self.driver.swipe(0.9*self.x, 0.75*self.y, 0.1*self.x, 0.75*self.y, 300)
			sleep(2)
			self.driver.swipe(0.9*self.x, 0.75*self.y, 0.1*self.x, 0.75*self.y, 300)
			# d(className="android.widget.ImageView", instance=15).click()
			xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.ImageView'
			self.driver.find_element_by_xpath(xpath).click()
			sleep(3)

		def login():
			#登录
			btnMy = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]'
			self.driver.find_element_by_xpath(btnMy).click();
			sleep(3)
			userNameText = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[2]/android.widget.EditText'
			self.driver.find_element_by_xpath(userNameText).send_keys('17816866126')
			pwdText = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[3]/android.widget.EditText'
			self.driver.find_element_by_xpath(pwdText).send_keys('12345678')
			btnlogin='	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[4]/android.widget.TextView'
			self.driver.find_element_by_xpath(btnlogin).click()
			sleep(4)

		def toOrderList():
			btnMy = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]'
			self.driver.find_element_by_xpath(btnMy).click();
			sleep(2)
			#我买到的
			btnwmd='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[5]/android.widget.TextView'
			self.driver.find_element_by_xpath(btnwmd).click()
			sleep(3)

		def swipeUp(driver, t=500, n=1):
			l = driver.get_window_size()
			x1 = l['width'] * 0.5     # x坐标
			y1 = l['height'] * 0.75   # 起始y坐标
			y2 = l['height'] * 0.25   # 终点y坐标
			for i in range(n):
				driver.swipe(x1, y1, x1, y2, t)

		def testCancelOrder():
			# print el
			# print u'cancelOrder'
			# el为取消订单按钮
			sleep(2)
			# try:
			# alert = self.driver.switch_to_alert()
			# Assert.assertEquals(u'是否取消该订单', alert.text)
			# alert.accept()
			alert = self.driver.switchTo().alert()
			alert.accept()
			# except:
				# Assert.fail(u'没有找到confirm框')
			# sleep(2)

		def findOrderCanCancel():
			toPayText = u'待支付'
			toPayTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ScrollView/android.view.View/android.view.View[' + str(self.initNum) + ']/android.view.View/android.widget.TextView[2]'
			try:		
				btnEl = self.driver.find_element_by_xpath(toPayTextPath)
				if btnEl.text == toPayText:
					print self.initNum
					cancelBtnEl = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ScrollView/android.view.View/android.view.View[' + str(self.initNum) + ']/android.view.View/android.view.View[4]/android.widget.TextView'
					self.driver.find_element_by_xpath(cancelBtnEl).click()
					self.doFlag = True
					testCancelOrder()
			except:
				self.initNum = self.initNum + 1

		def toBePayList():
			toBePayBtn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'
			self.driver.find_element_by_xpath(toBePayBtn).click()
			sleep(3)

			# #新品
			# btnxinpin='	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.TextView'
			# self.driver.find_element_by_xpath(btnxinpin).click()
			# sleep(3)

			self.initNum = 1
			self.doFlag = False
			while self.doFlag == False:
				findOrderCanCancel()
				
			# while 1:
			# 	sleep(3)
			# 	try:
			# 		toPayTextPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ScrollView/android.view.View/android.view.View[' + str(initNum) + ']/android.view.View/android.widget.TextView[2]'
			# 		if self.driver.find_element_by_xpath(toPayTextPath).text == toPayText:
			# 			print initNum
			# 		initNum = initNum + 1

			# 	except:
			# 		swipeUp(self.driver)
			# 		initNum = initNum + 1


		skip()
		login()
		toOrderList()
		toBePayList()






			


	# def testCase002(self):
	# 	sleep(3)
	# 	#登录
	# 	btnMy = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]'
	# 	self.driver.find_element_by_xpath(btnMy).click();
	# 	sleep(3)
	# 	userNameText = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[2]/android.widget.EditText'
	# 	self.driver.find_element_by_xpath(userNameText).send_keys('17816866126')
	# 	pwdText = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[3]/android.widget.EditText'
	# 	self.driver.find_element_by_xpath(pwdText).send_keys('12345678')
	# 	btnlogin='	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[4]/android.widget.TextView'
	# 	self.driver.find_element_by_xpath(btnlogin).click()
	# 	time.sleep(4)

#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
	unittest.TextTestRunner(verbosity=2).run(suite)