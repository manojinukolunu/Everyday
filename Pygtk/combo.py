import pygtk
pygtk.require('2.0')
import gtk

class ComboExample:
  def __init_(self):
    window=gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Combo WIdget Example")
    window.connect("destroy",lambda w:gtk.main_quit())

    combo=gtk.Calender()

    window.add(combo)
    combo.show()
    window.show()

def main():
  gtk.main()
  return 0

if __name__=="__main__":
  ComboExample()
  main()

