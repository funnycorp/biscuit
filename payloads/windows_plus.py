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
	layout.write("chrome bit.ly/SussyAmogus\n")
	sleep(1)
	kbd.send(Keycode.SPACE)
	sleep(.1)

	for i in range(10):
		# Initialization for crewmate payload
		kbd.press(Keycode.WINDOWS)
		kbd.send(Keycode.R)
		kbd.release(Keycode.WINDOWS)
		sleep(.2)

		layout.write("mspaint\n")
		sleep(1)

		kbd.press(Keycode.ALT)
		kbd.send(Keycode.SPACE)
		kbd.release(Keycode.ALT)
		sleep(.5)
		kbd.send(Keycode.X)
		sleep(.2)

		kbd.press(Keycode.CONTROL)
		kbd.send(Keycode.E)
		kbd.release(Keycode.CONTROL)
		sleep(.2)

		layout.write("2000\t2000\n")

		mouse.move(-1000, -1000)
		mouse.move(50, 95)
		sleep(1)

		# Crewmate
		crewmate.draw(mouse)
		sleep(1)