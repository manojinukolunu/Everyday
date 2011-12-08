import pygtk
pygtk.require('2.0')
import gtk,gobject

class PanedExample:
    def create_list(self):
        scrolled_window=gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
        model=gtk.ListStore(gobject.TYPE_STRING)
        tree_view=gtk.TreeView(model)
        scrolled_window.add_with_viewport(tree_view)

        tree_view.show()

        for i in range(10):
            msg="Message #%d" %i
            iter=model.append()
            model.set(iter,0,msg)
            
        cell=gtk.CellRendererText()
        column=gtk.TreeViewColumn("Messages",cell,text=0)
        tree_view.append_column(column)

        return scrolled_window

    def insert_text(self,buffer):
        iter=buffer.get_iter_at_offset(0)
        buffer.insert(iter,
                      "From\n")
    def create_text(self):
        view=gtk.TextView()
        buffer=view.get_buffer()
        scrolled_window=gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
        scrolled_window.add(view)
        self.insert_text(buffer)
        scrolled_window.show_all()
        return scrolled_window
    def __init__(self):
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Paned Window")
        window.connect("destroy",lambda w:gtk.main_quit())
        window.set_border_width(10)
        window.set_size_request(450,450)

        vpaned=gtk.VPaned()
        window.add(vpaned)
        vpaned.show()

        list=self.create_list()
        vpaned.add1(list)
        list.show()

        text=self.create_text()
        vpaned.add2(text)
        text.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    PanedExample()
    main()
    
