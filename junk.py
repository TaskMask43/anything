from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

o = sense.get_orientation()

print(o)

pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]

print(f"Pitch:{pitch}\tRoll:{roll}\tYaw:{yaw}")
