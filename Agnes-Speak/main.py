import threading
import wx
from agnes import *
from find import *

def work_agnes():
	a = Agnes()
	a.start()

def work_detect_faces():
	d = detectFace()
	d.startWeb()

class ButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Agnes', size=(485, 330))
		self.Center()
		panel = wx.Panel(self, -1)
		self.button = wx.Button(panel, -1, "Start", pos=(205, 300))
		self.Bind(wx.EVT_BUTTON, self.start, self.button)
		self.button.SetDefault()
		
		#self.label = wx.StaticText(panel, -1, "Oi, eu sou a Agnes ^^", pos=(230,10))
		#self.texto = wx.TextCtrl(panel, pos=(220,30), size = (180,50))
		
		png = wx.Image("Images/Faces/face-1.png",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		wx.StaticBitmap(panel, 1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
		

	"""	
	def change_image(self,number):
		print "ve "+str(number)
		panel = wx.Panel(self, -1)
		png = wx.Image("Imagem/Faces/face-"+str(number)+".png",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		wx.StaticBitmap(panel, 1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
	"""

	def start(self, event):

		t1 = threading.Thread(target = work_agnes)
		t1.start()

		t2 = threading.Thread(target = work_detect_faces)
		t2.start()

def main():
	
	
	app = wx.PySimpleApp()
	frame = ButtonFrame()
	frame.Show()
	app.MainLoop()
	
	


if __name__ == '__main__':
	main()