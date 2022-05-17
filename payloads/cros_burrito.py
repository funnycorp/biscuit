from adafruit_hid.keycode import Keycode
from time import sleep

def start(*, kbd, layout, mouse, consumer_control):
	kbd.press(Keycode.CONTROL)
	kbd.send(Keycode.N)
	kbd.release(Keycode.CONTROL)
	sleep(.2)

	layout.write("youtu.be/prPjpwsGiws\n")
	sleep(.2)