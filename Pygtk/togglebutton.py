import pygtk
pygtk.require('2.0')
import gtk

class ToggleButton:
	def callback(self,widget,data=None):
		print "%s Pressed" %data
		
	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False
		
		
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Toggle Button")
		self.window.set_border_width(20)
		
		self.window.connect("delete_event",self.delete_event)
		
		vbox=gtk.VBox(True,2)
		self.window.add(vbox)
		button=gtk.ToggleButton("toggle Button 1")
		
		button.connect("toggled",self.callback,"toggle Button1")
		vbox.pack_start(button,True,True,2)
		button.show()
		
		button=gtk.ToggleButton("Toggle Button 2")
		button.connect("toggled",self.callback,"Toggle Button 2")
		
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
	ToggleButton()
	main()
	
		