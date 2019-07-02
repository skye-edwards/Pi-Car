#import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set up the pins to use for the motor
#motor 1
m1For = 7
m1Back = 11

#motor 2
m2For = 32
m2Back = 36

#pin to enabled the chip
ene = 31

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
#set up the pins for output
GPIO.setup(m1For,GPIO.OUT)
GPIO.setup(m1Back,GPIO.OUT)
GPIO.setup(m2For,GPIO.OUT)
GPIO.setup(m2Back,GPIO.OUT)
GPIO.setup(ene,GPIO.OUT)


#get the curses window, turn off echoing of keyboard to screen
#turn on instant key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#motor control
try:
	#have the car be stopped at the start
	GPIO.output(m1For,False)
	GPIO.output(m1Back,False)
	GPIO.output(m2For,False)
	GPIO.output(m2Back,False)

	while True:
		GPIO.output(ene,True)
		char = screen.getch()
		#End the Program
		if char == ord('q'):
			break
		#move forward with the Up Arrow Key
		elif char == curses.KEY_UP:
			GPIO.output(m1For,True)
			GPIO.output(m1Back,False)
			GPIO.output(m2For,True)
			GPIO.output(m2Back,False)
		#move backwards with the Down Arrow Key
		elif char == curses.KEY_DOWN:
			GPIO.output(m1For,False)
			GPIO.output(m1Back,True)
			GPIO.output(m2For,False)
			GPIO.output(m2Back,True)
		#Turn Right with the Right Arrow Key
		elif char == curses.KEY_RIGHT:
			GPIO.output(m1For,False)
			GPIO.output(m1Back,True)
			GPIO.output(m2For,True)
			GPIO.output(m2Back,False)
		#Turn LEFT with the Left Arrow key
		elif char == curses.KEY_LEFT:
			GPIO.output(m1For,True)
			GPIO.output(m1Back,False)
			GPIO.output(m2For,False)
			GPIO.output(m2Back,True)
		#Stop the Car with the Home key
		elif char == curses.KEY_HOME:
			GPIO.output(m1For,False)
			GPIO.output(m1Back,False)
			GPIO.output(m2For,False)
			GPIO.output(m2Back,False)

finally:
#Stop the car at the end of the program
	GPIO.output(m1For,False)
	GPIO.output(m1Back,False)
	GPIO.output(m2For,False)
	GPIO.output(m2Back,False)
	GPIO.output(ene,False)
#close  curses properly	
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
	GPIO.cleanup()
