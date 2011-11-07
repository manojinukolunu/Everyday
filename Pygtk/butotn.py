import pygtk
pygtk.require('2.0')
import gtk

def xpm_label_box(parent,xpm_filename,label_text):
	box1=gtk.HBox(False,0)
	box1.set_border_width(2)
	
	image=gtk.Image()
	image.set_from_file(xpm_filename)
	label=gtk.Label(label_text)
	
	box1.pack_start(image,False,False,3)
	box1.pack_start(label,False,False,3)
	
	image.show()
	label.show()
	return box1
	
	
	
class Buttons:
	def callback(self,widget,data=None):
		print "%s was pressed " % data
		
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Image'd Buttons")
		self.window.connect("destroy",lambda wid:gtk.main_quit())
		self.window.connect("delete_event",lambda a1,a2:gtk.main_quit())
		
		self.window.set_border_width(10)
		button=gtk.Button()
		
		button.connect("clicked",self.callback,"cool button")
		box1=xpm_label_box(self.window,"info.xpm","cool button")
		button.add(box1)
		box1.show()
		button.show()
		
		self.window.add(button)
		self.window.show()
		
def main():
	gtk.main()
	return 0
	
if __name__=="__main__":
	Buttons()
	main()