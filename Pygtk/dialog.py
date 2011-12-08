import pygtk
pygtk.require('2.0')
import gtk

class dialog():
    def __init__(self):
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.dialog=gtk.Dialog(parent=self.window)
        self.window.show()
        

def main():
    gtk.main()
    return 0
if __name__=="__main__":
    dialog()
    main()
    

