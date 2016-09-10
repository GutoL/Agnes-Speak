
import wx
from agnes import *


class ButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Agnes', size=(410, 310))
		self.Center()
		panel = wx.Panel(self, -1)
		self.button = wx.Button(panel, -1, "Start", pos=(160, 280))
		self.Bind(wx.EVT_BUTTON, self.start, self.button)
		self.button.SetDefault()
		
		#self.label = wx.StaticText(panel, -1, "Oi, eu sou a Agnes ^^", pos=(230,10))
		#self.texto = wx.TextCtrl(panel, pos=(220,30), size = (180,50))
		
		# Image link: http://28.media.tumblr.com/tumblr_lgu4uzyYkB1qe2w1uo1_500.jpg
		png = wx.Image("Imagem/eva.JPG",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		wx.StaticBitmap(panel, 1, png, (0, 0), (png.GetWidth(), png.GetHeight()))

	def start(self, event):
		self.a = Agnes()
		self.a.start()




def main():
	
	
	app = wx.PySimpleApp()
	frame = ButtonFrame()
	frame.Show()
	app.MainLoop()
	
	


if __name__ == '__main__':
	main()