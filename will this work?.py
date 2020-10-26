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

sense.show_letter("1", text_colour=red, back_colour=blue)
sleep(.5)
sense.show_letter("2", text_colour=blue, back_colour=red)
sleep(.5)
sense.show_letter("3", text_colour=purple, back_colour=cyan)
sleep(.5)
sense.show_letter("4", text_colour=black, back_colour=green)
sleep(.5)
sense.show_letter("5", text_colour=green, back_colour=yellow)
sleep(.5)
sense.show_letter("6", text_colour=yellow, back_colour=black)
sleep(.5)
sense.show_letter("7", text_colour=cyan, back_colour=purple)
sleep(.5)
sense.show_letter("8", text_colour=white, back_colour=blue)