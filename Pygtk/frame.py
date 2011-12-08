import pygtk
pygtk.require('2.0')
import gtk

class FrameExample:
    def callback_button(self,widget,data):
        print "Hello %s "%data
    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Frame Example")
        window.connect("destroy",lambda w:gtk.main_quit())
        window.set_size_request(300,300) #What does this do?

        window.set_border_width(10)

        frame=gtk.Frame() #Create a frame
        window.add(frame)

        frame.set_label("GTK Frame WIdget")

        frame.set_label_align(1.0,0.0) # What does this do?

        frame.set_shadow_type(gtk.SHADOW_NONE)
        button=gtk.Button("Hello")
        button.connect("clicked",self.callback_button,"Button1")
        frame.add(button)
        button.show()
        frame.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    FrameExample()
    main()
