import pygtk
pygtk.require('2.0')
import gtk

class AspectFrameExample:
    def hello(self):
        print "hello"
    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Aspect Frame")
        window.connect("destroy",lambda x:gtk.main_quit())
        window.set_border_width(10)


        aspect_frame=gtk.AspectFrame("2x1",0.5,0.5,2,False)
        window.add(aspect_frame)

        aspect_frame.show()

       
        button=gtk.Button("Hello")
        button.set_size_request(200,20)
        button.connect("clicked",lambda w:self.hello()) 
        aspect_frame.add(button)
        button.show()
        

        window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    AspectFrameExample()
    main()
