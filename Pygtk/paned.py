import pygtk
pygtk.require('2.0')
import gtk

class PaneExample:
    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Pane Example")
        window.connect("destroy",lambda w:gtk.main_quit())

        vpane=gtk.VPaned()

        button=gtk.Button("Hello")
        button.set_size_request(100,200)
        button.connect("clicked",lambda w:"Hello")

        vpane.add1(button)
        button.show()
        button=gtk.Button("Hello 2")
        button.set_size_request(200,200)
        vpane.add2(button)
        button.show()

        window.add(vpane)

        vpane.show()

        window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    PaneExample()
    main()
