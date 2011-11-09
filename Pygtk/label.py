import pygtk
pygtk.require('2.0')
import gtk

class Labels:
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",lambda w:gtk.main_quit())
		self.window.set_title("Label")
		
		
		vbox=gtk.VBox(False,0)
		hbox=gtk.HBox(False,5)
		
		self.window.add(hbox)
		hbox.pack_start(vbox,False,False,0)
		
		self.window.set_border_width(5)
		
		frame=gtk.Frame("Normal Label")
		
		label=gtk.Label("This is a Normal Label")
		
		frame.add(label)
		
		vbox.pack_start(frame,False,False,0)
		
		frame=gtk.Frame("Mult-line Label")
		label=gtk.Label("This is a multi line label\n Hello")
		frame.add(label)
		
		
		vbox.pack_start(frame,False,False,0)
		
		frame=gtk.Frame("Left Justified Label")
		label=gtk.Label("this is a left justified label \n asdfasdf")
		label.set_justify(gtk.JUSTIFY_LEFT)
		
		frame.add(label)
		
		vbox.pack_start(frame,False,False,0)
		
		frame=gtk.Frame("Right Justified Label")
		
		label=gtk.Label("This is airight justified label\n dsafsdfasf")
		label.set_justify(gtk.JUSTIFY_RIGHT)
		frame.add(label)
		
		vbox.pack_start(frame,False,False,0)
		
		vbox=gtk.VBox(False,5)
		
		hbox.pack_start(vbox,False,False,0)
		
		frame=gtk.Frame("Line Wrapped Label")
		label=gtk.Label("This i sfkalshfkjas hlfkjshfskjhf")
		label.set_line_wrap(True)
		frame.add(label)
		
		vbox.pack_start(frame,False,False,0)
		
		frame=gtk.Frame("Underlined Label")
		label=gtk.Label("This label is underlined")
		label.set_justify(gtk.JUSTIFY_LEFT)
		label.set_pattern("_______________________________ __")
		frame.add(label)
		vbox.pack_start(frame,False,False,0)
		self.window.show_all()
		
def main():
	gtk.main()
	return 0
	
if __name__=="__main__":
	Labels()
	main()
		
		