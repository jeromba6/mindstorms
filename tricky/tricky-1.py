# LEGO type:standard slot:1 autostart

import hub
import time

wheel_right  = hub.port.A.motor
wheel_left   = hub.port.B.motor
wheels       = wheel_left.pair(wheel_right)
arm          = hub.port.C.motor
sensor_us    = hub.port.D.device
sensor_color = hub.port.E.device

activate_distance = 30
max_distance = 200

sensor_color.mode(3)
sensor_color.mode(3,b''+(chr(0)*3))

for i in range(255,-1,-1):
    hub.led((0,i,0))
    time.sleep(0.005)

while True:
    distance = sensor_us.get()[0]

    if distance and distance < activate_distance:
        hub.led((255,0,0))
        wheels.float()
        wheels.run_at_speed(40,40)
        time.sleep(2)
        wheels.run_at_speed(-40,-40)
        time.sleep(1)
    else:
        wheels.float()
        if distance == None:
            intensity = 0
        else:
            intensity = 255 - int((distance - activate_distance) / (max_distance-activate_distance)*255)
        hub.led((0,intensity,0))
        print(distance ,intensity)
        time.sleep(0.1)