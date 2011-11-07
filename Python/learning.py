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


