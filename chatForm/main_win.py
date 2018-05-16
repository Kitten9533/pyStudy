# -*- coding: UTF-8 -*-    
import wx  
import basewin
import namewin
import sys   
import requests
import time
import json
# 图灵机器人文档地址 https://www.kancloud.cn/turing/web_api/522989
url = 'http://www.tuling123.com/openapi/api'
key = '7e4a79e3e5fc4f63b7d87d68e5802bc8'
# reload(sys)
# sys.setdefaultencoding('utf-8')  

class Name(object):
	def __init__(self, name):
		self.name = name

	def set_name(self, name):
		self.name = name

user = Name(None)

# 聊天主界面
class MianWindow(basewin.BaseMainWind):  
	# 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。  
	def init_main_window(self):  
		pass

	def send_message(self, event):
		msg = self.SendText.GetValue().replace(' ', '')
		if len(msg) != 0:
			self.MsgBox.Append('%s：%s' % (user.name, msg))
			self.SendText.SetValue('')
			query = {'key': key, 'info': msg.encode('utf-8')}
			r = requests.get(
					url, 
					params = query,
					headers = {'Content-Type': 'text/html', 'charset': 'utf-8'}
				)
			r.encoding = 'utf-8'
			self.MsgBox.Append('Robot: %s' % json.loads(r.text).get('text'))
	# 回车键事件
	def send_text_enter(self, event):
		self.send_message(event)

# 名字设置界面
class NameWindow(namewin.BaseNameWind):
	def init_main_window(self):
		pass

	def name_ok(self, event):
		name = self.NameBox.GetValue().replace(' ', '')
		if len(name) == 0:
			self.WarnText.SetLabel(u'格式错误，请输入正确的名字~')
		else:
			user.set_name(name)
			event.Skip()
			main_win = MianWindow(None)
			main_win.Show()

	# 回车键事件
	# def name_text_enter(self, event):
	# 	print(u'回车')
	# 	self.name_ok(event)

	def name_cancel(self, event):
		event.Skip()

if __name__ == '__main__':  
	app = wx.App()
	dialog = NameWindow(None)
	dialog.Show()   
	app.MainLoop()  