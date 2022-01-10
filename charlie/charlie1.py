# LEGO type:standard slot:9 autostart

import hub
import time

wheel_left = hub.port.A.motor
wheel_right = hub.port.E.motor
wheels = wheel_left.pair(wheel_right)
arm_left = hub.port.B.motor
arm_right = hub.port.F.motor
sensor_color = hub.port.C.device
sensor_distance = hub.port.D.device

sensor_color.mode(3)
sensor_color.mode(3,b''+(chr(0)*3))

hub.led(255,0,0)

arm_left.run_for_degrees(360,50,50,0,100,100,False)
arm_right.run_for_degrees(360,-50,50,0,100,100,False)
while True:
    time.sleep(0.2)
    values_left = arm_left.get()
    values_right = arm_right.get()
    if values_left[0] == 0:
        arm_left.float()
    if values_right[0] == 0:
        arm_right.float()
    if values_left[0] == 0 and values_right[0] == 0:
        break
val = values_left[2]
arm_left.run_for_degrees(val, -50)
val = values_right[2] if values_right[2] < 0 else (180 - values_right[2])+180
arm_right.run_for_degrees(val, 50)
marge = 10
while True:
    time.sleep(0.2)
    values_left = arm_left.get()
    values_right = arm_right.get()
    if values_left[0] == 0:
        arm_left.float()
    if values_right[0] == 0:
        arm_right.float()
    if values_left[0] == 0 and values_right[0] == 0:
        break
hub.display.align(hub.motion.orientation())
hub.display.show(hub.Image.HAPPY)

for i in range(255,-1,-1):
    hub.led((0,i,0))
    time.sleep(0.005)

while True:

    distance = sensor_distance.get()[0]
    if distance and distance < 30:
        wheels.float()
        wheels.run_at_speed(40,-40)
        time.sleep(1)
        wheels.run_at_speed(40,40)
        time.sleep(1)
    else:
        wheels.run_at_speed(-70,70)
