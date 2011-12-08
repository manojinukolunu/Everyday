import pygtk
pygtk.require('2.0')
import gtk

class ImageExample:
    def close_application(self,widget,event,data=None):
        gtk.main_quit()
        return 0
    def button_clicked(self,widget,data=None):
        print "button %s clicked" %data


    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event",self.close_application)
        window.set_border_width(10)
        window.show()

        hbox=gtk.HBox()
        hbox.show()
        window.add(hbox)

        filename="/home/manoj/Dropbox/Photos/Sample Album/Bostom City Flow.jpg"

        image=gtk.Image()
        image.set_from_file(filename)
        image.show()
        button=gtk.Button()
        button.add(image)
        button.show()
        hbox.pack_start(button)
        button.connect("clicked",self.button_clicked,"1")


def main():
    gtk.main()
    return 0
ImageExample()
main()
