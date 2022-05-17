from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode as ControlCode
from time import sleep
import crewmate

def start(*, kbd, layout, mouse, consumer_control):
	# Volume up
	consumer_control.press(ControlCode.VOLUME_INCREMENT)
	sleep(3)
	consumer_control.release()

	# Rickroll
	kbd.press(Keycode.WINDOWS)
	kbd.send(Keycode.R)
	kbd.release(Keycode.WINDOWS)
	sleep(.1)

	# Opens Chrome
	layout.write("chrome youtu.be/prPjpwsGiws\n")
	sleep(1)
	kbd.send(Keycode.SPACE)
	sleep(.1)