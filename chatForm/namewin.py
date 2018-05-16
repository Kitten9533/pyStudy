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
## Class BaseNameWind
###########################################################################

class BaseNameWind ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,160 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( 300,160 ), wx.DefaultSize )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"请输入您的名字" ), wx.VERTICAL )
		
		self.NameBox = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.NameBox, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.WarnText = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WarnText.Wrap( -1 )
		sbSizer1.Add( self.WarnText, 0, wx.ALL, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( sbSizer1.GetStaticBox(), wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( sbSizer1.GetStaticBox(), wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		sbSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.NameBox.Bind( wx.EVT_TEXT_ENTER, self.name_text_enter )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.name_cancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.name_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def name_text_enter( self, event ):
		event.Skip()
	
	def name_cancel( self, event ):
		event.Skip()
	
	def name_ok( self, event ):
		event.Skip()
	

