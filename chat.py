#encoding: utf-8
import requests
import time
import json

# 图灵机器人文档地址 https://www.kancloud.cn/turing/web_api/522989
url = 'http://www.tuling123.com/openapi/api'
key = '7e4a79e3e5fc4f63b7d87d68e5802bc8'

name = None
def user_init():
	print('\n----------Start----------')
	print('    输入END则结束聊天    \n')
	name = input('Set your name: ')
	while(len(name) == 0):
		name = input('Set your name again:')
	print('Let\'s chat, %s!\n' % name)
	return name

	# for x in '我的天啊':
		# print(x, end = '')

def simulate(msg):
	pass

class DoChat(object):
	def __init__(self, name):
		self.name = name
	
	# 开始聊天
	def start(self):
		pass;

	# 发送聊天信息
	def chat(self, msg):
		query = {'key': key, 'info': msg.encode('utf-8')}
		r = requests.get(
				url, 
				params = query,
				headers = {'Content-Type': 'text/html', 'charset': 'utf-8'}
			)
		r.encoding = 'utf-8'
		print('Robot: %s' % json.loads(r.text).get('text'))

	# 输入END则结束聊天
	def exit(self):
		print('\nRobot:Bye...')
		print('-----------END-----------\n')

def main():
	# username = user_init()
	user = DoChat(user_init())
	msg = input('%s:' % user.name)
	while(msg != 'END'):
		user.chat(msg)
		msg = input('%s:' % user.name)
	user.exit()

if __name__=='__main__':
	main()