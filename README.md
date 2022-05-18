# Biscuit

This repository contains code which can be copied onto an
[Adafruit NeoKey Trinkey](https://adafru.it/5020) running
[CircuitPython](https://circuitpython.org).

The code has been tested on relatively recent versions of
CircuitPython (7.x).

When using this, you should also copy the Adafruit HID library
from the CircuitPython library bundle, which can be found on
[its GitHub releases](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest).

## Install

Your NeoKey Trinkey should have CircuitPython installed by
default. If the installed CircuitPython is version 6 or below,
download and install CircuitPython 7.x from
[the official website](https://circuitpython.org/board/adafruit_neokey_trinkey_m0/).

If you are unsure how to install CircuitPython, see
[Adafruit's guide](https://learn.adafruit.com/adafruit-neokey-trinkey/circuitpython).

After installing CircuitPython (if needed), delete the
existing `.py` files on the CIRCUITPY drive. Copy the
`adafruit_hid` folder from the CircuitPython library bundle into
the `lib` folder on the CIRCUITPY drive.

Finally, copy the files inside this repo to the CIRCUITPY drive.
To change the payload, change the word after `payloads.` on the
first line in `code.py` to one of the following:

* `windows`: opens a rickroll and draws a crewmate
* `windows_plus`: like `windows`, but with ten crewmates
* `windows_burrito`: plays a funny song
* `mac`: opens a rickroll and an image of a crewmate
* `mac_burrito`: `windows_burrito` for Mac OS
* `cros_burrito`: `windows_burrito` for Chrome OS 

## License

This code is licensed under the MIT license. You should not
expect any kind of warranty, and we disclaim all responsibility
for the havoc you wreak and the chaos you cause. Nevertheless,
you might receive some support from us by making a GitHub issue.

Have fun, and happy trolling :)