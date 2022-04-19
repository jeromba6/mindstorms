# LEGO type:standard slot:0 autostart
# all credits to Creator Academy Pty Ltd
# https://github.com/CreatorAcademyAu

from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
hub = MSHub()
wheels = MotorPair('E','A')
left_motor = Motor('A')
kp = 11 #proportional gain
ki = 4.2 #integral gain
kd = 92 #derivative gain
roll_target = 99 #balance angle
integral = 0
error = 0
start_target = 0
derivative = 0
prev_error = 0
result = 0
ks = -0.6
start = 0
start_target = 0
left_motor.set_degrees_counted(0)
hub.light_matrix.set_pixel(0,0)
hub.light_matrix.set_pixel(0,1)
hub.light_matrix.set_pixel(1,0)
hub.light_matrix.set_pixel(1,1)

hub.light_matrix.set_pixel(0,3)
hub.light_matrix.set_pixel(0,4)
hub.light_matrix.set_pixel(1,3)
hub.light_matrix.set_pixel(1,4)

hub.light_matrix.set_pixel(3,0)
hub.light_matrix.set_pixel(3,4)
hub.light_matrix.set_pixel(4,1)
hub.light_matrix.set_pixel(4,2)
hub.light_matrix.set_pixel(4,3)
angle = hub.motion_sensor.get_roll_angle()
while angle<roll_target+30 and angle>roll_target-30:
    error = roll_target - angle
    integral = integral + (error*0.25)
    derivative = error - prev_error
    prev_error = error
    start = (start_target - left_motor.get_degrees_counted())
    result = (error*kp) + (integral*ki) + (derivative*kd) + (start*ks)

    wheels.start_at_power(math.floor(result),0)
    angle = hub.motion_sensor.get_roll_angle()
wheels.stop()
