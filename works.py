from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
b = (0,0,255)
r = (255,0,0)
w = (255,255,255)

while True:
    temp=sense.get_temperature()
    #temp = round(temp, 1)
    temp = 10
    print (temp)
    
    if (temp) > 26.7:
            colour = r
            warn = ("DANGER! TEMPERATURE HIGH:")
    elif (temp) < 18.3:
            colour = b
            warn = ("DANGER! TEMPERATURE LOW:")
    else:
        colour = w
        warn = ("")
    
    sense.show_message(f"{warn} {temp}", text_colour=colour, scroll_speed = 0.08)
            
        
            

  
        



    