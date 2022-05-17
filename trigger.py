from digitalio import DigitalInOut, Pull, Direction
import board

trigger = DigitalInOut(board.SWITCH)
trigger.direction = Direction.INPUT
trigger.pull = Pull.DOWN