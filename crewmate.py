from time import sleep

moves = (
	(30, 0),
	(15, -15),
	(-15, -15),
	(-35, 0),
	(-15, 15),
	(15, 15),
	(15, 0),
	(0, 70),
	(25, 0),
	(0, -25),
	(25, 0),
	(0, 25),
	(25, 0),
	(0, -30),
	(25, 0),
	(0, -50),
	(-25, 0),
	(0, -30),
	(-25, -25),
	(-25, 0),
	(-20, 20),
	(0, 20)
)

def draw(mouse):
	mouse.press(mouse.LEFT_BUTTON)

	for x, y in moves:
		mouse.move(x, y)
		sleep(.02)

	mouse.release(mouse.LEFT_BUTTON)