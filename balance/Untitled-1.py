# LEGO type:standard slot:0 autostart
import hub
import time
import math

wheel_left = hub.port.A.motor
wheel_right = hub.port.E.motor
wheels = wheel_left.pair(wheel_right)
upright = hub.port.C.motor


while True:
    pos =upright.get()
    print('-'.join(map(str,pos)))
    time.sleep(1)


# upright.mode(3)
hub.led(255,0,0)

battery = 0
max_dev = 6

if battery != hub.battery.capacity_left():
    battery = hub.battery.capacity_left()
    print('Battery: '+str(battery) + '%')

_,_,roll = hub.motion.yaw_pitch_roll()
p_roll = roll
for set_pos in range(0,180):
    pos = upright.get()
    print('-'.join(map(str,pos)))
    upright.run_to_position(set_pos,100,100,2)
    pos = upright.get()
    while pos[1] < set_pos - max_dev or pos[1] > set_pos + max_dev or pos[1] > 110:
        pos = upright.get()
        pass
    time.sleep(0.1)
    _,_,roll = hub.motion.yaw_pitch_roll()
    if roll > 92 and roll - p_roll > 1:
        roll_target = p_roll
        break
    p_roll = roll
    print('Roll: {}'.format(roll))
upright.run_to_position(30,100,100)
print("Roll_target: {}".format(roll_target))

kp = 11 #proportional gain
ki = 4.2 #integral gain
kd = 92 #derivative gain
roll_target = 87 #balance angle
integral = 0
error = 0
start_target = 0
derivative = 0
prev_error = 0
result = 0
ks = -0.6
start = 0
start_target = 0
# wheel_left.set_degrees_counted(0)
_,_,angle = hub.motion.yaw_pitch_roll()
while angle<roll_target+30 and angle>roll_target-30:
    error = roll_target - angle
    integral = integral + (error*0.25)
    derivative = error - prev_error
    prev_error = error
    start = (start_target - wheel_left.get()[1])
    result = (error*kp) + (integral*ki) + (derivative*kd) + (start*ks)
    power = math.floor(result/10)
    wheel_left.run_at_speed(power)
    wheel_right.run_at_speed(power*-1)
    _,_,angle = hub.motion.yaw_pitch_roll()
    print(power,angle)
wheels.float()
