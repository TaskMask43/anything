from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

B = (102,51,0)
b = (0,0,255)
s = (205,133,63)
W = (25,255,255)
image_pixels = [
    B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    B,s,s,s,s,s,s,B,
    s,s,s,s,s,s,s,s,
    s,W,b,s,s,b,W,s,
    s,s,s,B,B,s,s,s,
    s,s,B,s,s,B,s,s,
    s,s,B,B,B,B,s,s
    ]
    
    


sense.set_pixels(image_pixels)