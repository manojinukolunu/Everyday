import pygtk
pygtk.require('2.0')
import gtk

class FixedExample:
  def move_button(self,widget):
    self.x=(self.x+30)%300
    self.y=(self.y+50)%300

    self.fixed.move(widget,self.x,self.y)

  def __init__(self):
    self.x=50
    self.y=50

    window=gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Fixed Container")

    window.connect("destroy",lambda w:gtk.main_quit())

    window.set_border_width(10)

    self.fixed=gtk.Fixed()
    window.add(self.fixed)
    self.fixed.show()

    for i in range(1,4):
      button=gtk.Button("Press me")
      button.connect("clicked",self.move_button)

      self.fixed.put(button,i*50,i*50)
      button.show()
    window.show()
def main():
  gtk.main()
  return 0

if __name__=="__main__":
  FixedExample()
  main()

