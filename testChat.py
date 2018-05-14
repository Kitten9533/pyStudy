import unittest
from chat import *

class TestChat(unittest.TestCase):
	def test_user_init(self):
		'''Test method user_init()'''
		pass

	def test_chat(self):
		user = DoChat('Kitten')
		user.chat('早上好')
		user.chat('杭州天气')
		user.chat('')
		pass

if __name__ == '__main__':
    unittest.main()