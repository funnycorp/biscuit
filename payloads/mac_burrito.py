from adafruit_hid.keycode import Keycode
from time import sleep

def start(*, kbd, layout, mouse, consumer_control):
	kbd.press(Keycode.COMMAND)
	kbd.send(Keycode.SPACE)
	kbd.release(Keycode.COMMAND)
	sleep(.2)

	layout.write("safari\n")
	sleep(1)
	layout.write("http:youtu.be/prPjpwsGiws\n")
	sleep(.2)