import pygtk
pygtk.require('2.0')
import gtk

xpm_data=[
 "16 16 3 1",
 " c None",
 ". c #000000000000",
 "X c #FFFFFFFFFFFF",
 " ",
 " ...... ",
 " .XXX.X. ",
 " .XXX.XX. ",
 " .XXX.XXX. ",
 " .XXX..... ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " .XXXXXXX. ",
 " ......... ",
 " ",
 " "]

class PixmapExample:
    def close_applicaton(self,widget,event,data=None):
        gtk.main_quit()
        return False

    def button_clicked(self,widget,data=None):
        print "button clicked"

        def __init__(self):
            window=gtk.Window(gtk.WINDOW_TOPLEVEL)
            window.connect("delete_event",self.close_application)
            window.set_border_width(10)
            window.show()

            pixmap,mask=gtk.gdk.pixmap_create_from_xpm_d(window.window,None,xpm_data)
            image=gtk.Image()
            image.set_from_pixmap(pixmap,mask)
            image.show()
            button=gtk.Button()
            button.add(image)
            window.add(button)
            button.show()
            button.connect("clicked",self.button_clicked)

def main():
    gtk.main()
    return 0

PixmapExample()
main()
