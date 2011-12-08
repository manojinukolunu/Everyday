button=gtk.Button(label=None,stock=None)
If stock is specified it is used to select a stock icon and text 
label for the button.


The Button widget has the following signals:
pressed - emitted when pointer button is pressed within Button widget
released - emitted when pointer button is released within Button widget
clicked - emitted when pointer button is pressed and then released within -Button widget
enter - emitted when pointer enters Button widget
leave - emitted when pointer leaves Button widget


toggle_button=gtk.ToggleButotn(label=None)
def toggle_button_callback(widget,data=None):
	if widget.get_active(): 
		#toggle button is active
	else:
		#toggle button is inavtive
		
		
		
toggle_button.set_active(boolean is_active)

toggle_button.get_active() retruns the state of the toggle button





check_button=gtk.CheckButton(label=None)

radio_button-gtk.RadioButton(group=None,label=None)
To add more radio buttons to a group, pass in a reference to a radio button in group in subsequent calls to
gtk.RadioButton().
object.set_flags(gtk.CAN_DEFAULT)
object.grab_default()#This call causes the object to be the default selected object meaning when enter is pressed in the window
#This button is activated by default This requires the gtk.CAN_DEFAULT to be set by the above call on the widget

---------------------------------------------
ADJUSTMENTS
---------------------------------------------
adjustment=gtk.Adjustment(value=0,lower=0,upper=0,step_incr=0 \
page_incr=0,page_size=0)











--------------------------------------------
Range Widgets

--------------------------------------------
hscrollbar = gtk.HSscrollbar(adjustment=None)
vscrollbar = gtk.VSscrollbar(adjustment=None)
and

vscale = gtk.VScale(adjustment=None)
hscale = gtk.HScale(adjustment=None)

-------------------------------------------
Arrows
-------------------------------------------

arrow=gtk.Arrow(arrow_type,shadow_type)
arrow.set(arrow_type,shadow_type)
Arrow widget emits no signals
arrow_type={ARROW_UP or ARROW_DOWN or ARROW_LEFT or ARROW_RIGHT}
shadow_type={SHADOW_IN or SHADOW_OUT(default) or SHADOW_ETCHED_IN or SHADOW_ETCHED_OUT}


Dialogs:
-------------------------------------------
dialog = gtk.Dialog(title=None, parent=None, flags=0, buttons=None)

parent is the main application window

flags:
DIALOG_MODAL - make the dialog modal
DIALOG_DESTROY_WITH_PARENT - destroy dialog when its parent is destroyed
DIALOG_NO_SEPARATOR - omit the separator between the vbox and the action_area

The buttons argument is a tuple of button text and response pairs. All arguments have defaults and can be specified
using keywords.

Images:
-------------------------------------------------------------
image=gtk.Image()


load image using the following methods
image.set_from_pixbuf(pixbuf)
image.set_from_pixmap(pixmap, mask)
image.set_from_image(image)
image.set_from_file(filename)
image.set_from_stock(stock_id, size)
image.set_from_icon_set(icon_set, size)
image.set_from_animation(animation)

Where pixbuf is a gtk.gdk.Pixbuf; pixmap and mask are gtk.gdk.Pixmaps; image is a
gtk.gdk.Image; stock_id is the name of a gtk.StockItem; icon_set is a gtk.IconSet; and,
animation is a gtk.gdk.PixbufAnimation. the size argument is one of:
ICON_SIZE_MENU
ICON_SIZE_SMALL_TOOLBAR
ICON_SIZE_LARGE_TOOLBAR
ICON_SIZE_BUTTON
ICON_SIZE_DND
ICON_SIZE_DIALOG
The easiest way to create an image is using the set_from_file() method which automatically determines the
image type and loads it.


PIXMAPS:
--------------------------------------------------------------
pixmap = gtk.gdk.pixmap_create_from_data(window, data, width, height, depth, -fg, bg)

To Create PixMap From XPM::
pixmap, mask = gtk.gdk.pixmap_create_from_xpm(window, transparent_color, -filename)

Pixmaps can also be created from data in memory using the function::
pixmap, mask = gtk.gdk.pixmap_create_from_xpm_d(window, transparent_color, -data)

The final way to create a blank pixmap suitable for drawing operations is:
pixmap = gtk.gdk.Pixmap(window, width, height, depth=-1)
window is either a gtk.gdk.Window. or None. If window is a gtk.gdk.Window then depth can be -1 to
indicate that the depth should be determined from the window. If window is None then the depth must be specified.


RULERS:
--------------------------------------------------------------
Ruler widgets are used to locate the mouse pointer in the window

hruler=gtk.HRuler()
vruler=gtk.VRuler()
Units of measure for rulers can be PIXELS, INCHES or CENTIMETERS set using the method ruler.set_metric(metric)
default is gtk.PIXELS
ruler.set_range(lower, upper, position, max_size)  for marking the units of scale and where the position indicator is initially placed

The indicator on the ruler is a small triangular mark that indicates the position of the pointer relative to the ruler.
If the ruler is used to follow the mouse pointer, the "motion_notify_event" signal should be connected to the
"motion_notify_event" method of the ruler. We need to setup a "motion_notify_event" callback for the area and
use connect_object() to get the ruler to emit a "motion_notify_signal":
def motion_notify(ruler, event):
return ruler.emit("motion_notify_event", event)
area.connect_object("motion_notify_event", motion_notify, ruler)



TEXT ENTRIES:
---------------------------------------------------------------
The Entry widget allows text to be typed and displayed in a single line text box.
entry=gtk.Entry(max=0)
entry.set_max_length()

HBOX AND VBOX:
---------------------------------------------------------------
  hbox = gtk.HBox(homogeneous=False, spacing=0)

  vbox = gtk.VBox(homogeneous=False, spacing=0)

The homogeneous argument to gtk.HBox() and gtk.VBox() controls whether each object in the box has the same size (i.e., the same width in an hbox, or the same height in a vbox). If it is set, the pack routines function essentially as if the expand argument was always turned on.

Whats the difference between spacing (set when the box is created) and padding (set when elements are packed)? Spacing is added between objects, and padding is added on either side of an object. 


FIXED CONTAINER:
----------------------------------------------------------------
The Fixed container allows you to place widgets at a fixed position within it's window, relative to it's upper left hand corner. The position of the widgets can be changed dynamically.

There are only three calls associated with the fixed widget:

  fixed = gtk.Fixed()

  fixed.put(widget, x, y)

  fixed.move(widget, x, y)

The function gtk.Fixed() allows you to create a new Fixed container.

The put() method places widget in the container fixed at the position specified by x and y.

The move() method allows the specified widget to be moved to a new position.
