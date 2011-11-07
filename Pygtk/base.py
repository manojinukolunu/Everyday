import pygtk#import pygtk module
pygtk.require('2.0')#This specifies that we want to use PyGTK version
#2.0 which covers all versions of PyGK with the major number 2.
#This prevents the program from using earlier version of PyGTK if
#it happens to be installed 
import gtk#import gtk module

class Base:
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.show()
		
	def main(self):#why this method?
		gtk.main()
		
print __name__
if __name__=="__main__":
	base=Base()
	base.main()
	