import pygtk
pygtk.require('2.0')
import gtk
import random

class LayoutExample:
  def windowdeleteevent(self,widget,event):
    return False
  def windowdestroy(self,widget,*data):
    gtk.main_quit()
  def buttonclicked(self,button):
    self.layout.move(button,random.randint(0,500),random.randint(0,500))
  def __init__(self):
    window=gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Layout Example")
    window.set_default_size(300,300)
    window.connect("delete-event",self.windowdeleteevent)
    window.connect("destroy",self.windowdestroy)

    table=gtk.Table(2,2,False)
    window.add(table)

    self.layout=gtk.Layout(None,None)
    self.layout.set_size(600,600)
    table.attach(self.layout,0,1,0,1,gtk.FILL|gtk.EXPAND,gtk.FILL|gtk.EXPAND,0,0)
    vscrollbar=gtk.VScrollbar(None)
    table.attach(vscrollbar,1,2,0,1,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,0,0)
    hscrollbar=gtk.HScrollbar(None)
    table.attach(hscrollbar,0,1,1,2,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,0,0)
    vadjust=self.layout.get_vadjustment()
    vscrollbar.set_adjustment(vadjust)
    hadjust=self.layout.get_hadjustment()
    hscrollbar.set_adjustment(hadjust)
    button=gtk.Button("Press Me")
    button.connect("clicked",self.buttonclicked)
    self.layout.put(button,0,0)
    button=gtk.Button("Press me")
    button.connect("clicked",self.buttonclicked)
    self.layout.put(button,100,0)
    window.show_all()
def main():
  gtk.main()
  return 0
if __name__=="__main__":
  LayoutExample()
  main()

