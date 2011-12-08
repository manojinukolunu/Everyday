import pygtk
pygtk.require('2.0')
import gtk

class ScrolledWindow:
    def destroy(self,widget):
        gtk.main_quit()

    def __init__(self):
        window=gtk.Dialog()
        window.connect("destroy",self.destroy)
        window.set_title("Scrolled Window Example")
        window.set_border_width(0)
        window.set_size_request(300,300)

        scrolled_window=gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)

        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_ALWAYS)

        window.vbox.pack_start(scrolled_window,True,True,0)

        scrolled_window.show()

        table=gtk.Table(10,10,False)

        table.set_row_spacings(10)
        table.set_col_spacings(10)

        scrolled_window.add_with_viewport(table)

        table.show()

        for i in range(10):
            for j in range(10):
                buffer="button (%d,%d)" %(i,j)
                button=gtk.ToggleButton(buffer)
                table.attach(button,i,i+1,j,j+1)
                button.show()
        button=gtk.Button("close")
        button.connect_object("clicked",self.destroy,window)
        button.set_flags(gtk.CAN_DEFAULT)
        window.action_area.pack_start(button,True,True,0)

        button.grab_default()
        button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    ScrolledWindow()
    main()
    
        
