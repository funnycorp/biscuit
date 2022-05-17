import board
from digitalio import DigitalInOut, Direction
from neopixel_write import neopixel_write

try:
	neopixel = DigitalInOut(board.NEOPIXEL)
	neopixel.direction = Direction.OUTPUT

	def write(r, g, b):
		neopixel_write(neopixel, bytearray([r, g, b]))
except AttributeError:
	#from adafruit_dotstar import DotStar
	#dotstar = DotStar(board.DOTSTAR_CLOCK, board.DOTSTAR_DATA, 1)

	def write(r, g, b):
		pass#dotstar[0] = (r, g, b)