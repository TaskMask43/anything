from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

sense.set_pixel(0,2,black)
sense.set_pixel(7,4,black)
sense.set_pixel(0,1,blue)
sense.set_pixel(1,1,blue)
sense.set_pixel(1,2,blue)
sense.set_pixel(1,3,blue)
sense.set_pixel(0,3,blue)