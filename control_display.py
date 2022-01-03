from mindstorms import MSHub, Motor, MotorPair, DistanceSensor
import time

hub = MSHub()
hub.speaker.beep()

b = 0
while True:
    b = (b + 10) % 110
    for v in range(25):
        x = v % 5
        y = v // 5
        hub.light_matrix.set_pixel(x,y,b)
        time.sleep(0.1)
