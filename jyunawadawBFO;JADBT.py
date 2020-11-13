from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

w = (255,255,255)
sense.set_pixel(3,3,w)
while True:
    for event in sense.stick.get_events():
        if event.action=='pressed':
            if event.action=='up':
                sense.set_pixel (3,4,w)



