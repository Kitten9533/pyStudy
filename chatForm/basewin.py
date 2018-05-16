# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseMainWind
###########################################################################

class BaseMainWind ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chat", pos = wx.DefaultPosition, size = wx.Size( 600,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 600,370 ), wx.Size( 600,370 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		MsgBoxChoices = [ u"Rebot：让我们来聊天吧~" ]
		self.MsgBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,260 ), MsgBoxChoices, 0 )
		bSizer1.Add( self.MsgBox, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.SendText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,55 ), wx.TE_AUTO_URL|wx.TE_MULTILINE )
		bSizer2.Add( self.SendText, 1, wx.ALL, 5 )
		
		self.SendBtn = wx.Button( self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer2.Add( self.SendBtn, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.SendText.Bind( wx.EVT_TEXT_ENTER, self.send_text_enter )
		self.SendBtn.Bind( wx.EVT_BUTTON, self.send_message )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def send_text_enter( self, event ):
		event.Skip()
	
	def send_message( self, event ):
		event.Skip()
	

