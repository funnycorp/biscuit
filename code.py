from payloads.windows_plus import start
import color

from usb_hid import devices
from digitalio import DigitalInOut, Pull
from touchio import TouchIn
from trigger import trigger

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.mouse import Mouse

from time import sleep, monotonic_ns

kbd = Keyboard(devices)
layout = KeyboardLayoutUS(kbd)
consumer_control = ConsumerControl(devices)
mouse = Mouse(devices)

while 1:
	# Wait for key to be pressed
	while not trigger.value:
		pass

	color.write(31, 0, 0)
	sleep(.1)
	color.write(0, 0, 0)

	# The Trinkey has been armed >:}
	sleep(1 * 60)

	color.write(31, 31, 0)
	sleep(.1)
	color.write(0, 0, 0)

	start(kbd=kbd, layout=layout, mouse=mouse, consumer_control=consumer_control)