from adafruit_hid.keycode import Keycode
from time import sleep

def start(*, kbd, layout, mouse, consumer_control):
	kbd.press(Keycode.COMMAND)
	kbd.send(Keycode.SPACE)
	kbd.release(Keycode.COMMAND)
	sleep(.2)

	layout.write("safari\n")
	sleep(1)
	layout.write("http:bit.ly/SussyAmogus\n")
	sleep(.2)

	kbd.press(Keycode.COMMAND)
	kbd.send(Keycode.N)
	kbd.release(Keycode.COMMAND)
	sleep(.5)

	layout.write("http:bit.ly/SussyAmongus\n")