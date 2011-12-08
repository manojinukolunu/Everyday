import pygtk
pygtk.require('2.0')
import gtk

class FileSelectionExample:
  def file_ok_sel(self,w):
    print "%s"%self.filew.get_filename()
  def destroy(self,widget):
    gtk.main_quit()
  def __init__(self):
    self.filew=gtk.FileSelection("File Selection")
    self.filew.connect("destroy",self.destroy)

    self.filew.ok_button.connect("clicked",self.file_ok_sel)

    self.filew.cancel_button.connect("clicked",lambda w:self.filew.destroy())

    self.filew.set_filename("Penguim.png")
    self.filew.show()
def main():
  gtk.main()
  return 0

if __name__=="__main__":
  FileSelectionExample()
  main()

