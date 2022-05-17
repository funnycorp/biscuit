from trigger import trigger
from time import sleep
import storage
import usb_cdc

import color

storage.disable_usb_drive()
usb_cdc.disable()

print("biscuit: booting...")

color.write(15, 15, 15)
sleep(.05)

color.write(15, 15, 0)
sleep(.1)

color.write(0, 15, 0)
sleep(.05)

if trigger.value:
	color.write(0, 0, 255)
	print("biscuit: debug mode...")
	storage.enable_usb_drive()
	usb_cdc.enable()
	sleep(2)

color.write(0, 0, 0)