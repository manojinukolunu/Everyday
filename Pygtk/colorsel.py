import pygtk
pygtk.require('2.0')
import gtk

class ColorSelectionExample:
  def color_changed_cb(self,widget):
    colormap=self.drawingarea.get_colormap()
    color=self.colorseldlg.colorsel.get_current_color()
    self.drawingarea.modify_bg(gtk.STATE_NORMAL,color)

  def area_event(self,widget,event):
    handled=False
    if event.type==gtk.gdk.BUTTON_PRESS:
      handled=True
      if self.colorseldlg==None:
        self.colorseldlg=gtk.ColorSelectionDialog("Select background color")
      colorsel=self.colorseldlg.colorsel
      colorsel.set_previous_color(self.color)
      colorsel.set_current_color(self.color)
      colorsel.set_has_palette(True)

      colorsel.connect("color_changed",self.color_changed_cb)

      response=self.colorseldlg.run()

      if response==gtk.RESPONSE_OK:
        self.color=colorsel.get_current_color()
      else:
        self.drawingarea.modify_bg(gtk.STATE_NORMAL,self.color)
      self.colorseldlg.hide()
    return handled
  def destroy_window(self,widget,event):
    gtk.main_quit()
    return True
  def __init__(self):
    self.colorseldlg=None
    window=gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Color Selection Test")
    window.set_resizable(True)

    window.connect("delete_event",self.destroy_window)
    self.drawingarea=gtk.DrawingArea()

    self.color=self.drawingarea.get_colormap().alloc_color(0,65535,0)

    self.drawingarea.set_size_request(200,200)
    self.drawingarea.set_events(gtk.gdk.BUTTON_PRESS_MASK)
    self.drawingarea.connect("event",self.area_event)

    window.add(self.drawingarea)
    self.drawingarea.show()
    window.show()

def main():
   gtk.main()
   return 0

if __name__=="__main__":
   ColorSelectionExample()
   main()



