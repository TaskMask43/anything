from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
blue = (0,0,255)
purple = (255,0,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)
cyan = (0,255,255)
white = (255,255,255)

sense.show_letter("A", red)
sleep(.5)
sense.show_letter("A", blue)
sleep(.5)
sense.show_letter("A", purple)
sleep(.5)
sense.show_letter("A", black)
sleep(.5)
sense.show_letter("A", green)
sleep(.5)
sense.show_letter("A", yellow)
sleep(.5)
sense.show_letter("A", cyan)
sleep(.5)
sense.show_letter("A", white)
