import pygtk
pygtk.require('2.0')
import gtk

class CheckButton:
	def callback(self,widget,data):
		print "%s was toggled" % data
		
	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False
		
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Check Buttons")
		self.window.connect("delete_event",self.delete_event)
		self.window.set_border_width(10)
		
		vbox=gtk.VBox(True,2)
		self.window.add(vbox)
		
		button=gtk.CheckButton("check Button1 ")
		
		button.connect("toggled",self.callback,"check Button1")
		vbox.pack_start(button,True,True,2)
		
		button.show()
		
		button=gtk.CheckButton("Check Button2")
		button.connect("toggled",self.callback,"Check Button 2")
		vbox.pack_start(button,True,True,2)
		
		button.show()
		
		button=gtk.Button("Quit")
		
		button.connect("clicked",lambda wid:gtk.main_quit())
		
		vbox.pack_start(button,True,True,2)
		
		button.show()
		vbox.show()
		self.window.show()
		
		
		
def main():
	gtk.main()
	return 0
	
	
if __name__=="__main__":
	CheckButton()
	main()
	