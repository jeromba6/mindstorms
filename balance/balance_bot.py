# LEGO type:standard slot:0 autostart
import hub
import time
import math

from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
wheels = MotorPair('E','A')
left_motor = Motor('A')
wheel_left = hub.port.A.motor
wheel_right = hub.port.E.motor
upright = hub.port.D.motor
# upright.mode(3)
hub.led(0,0,255)

battery = 0
max_dev = 6

if battery != hub.battery.capacity_left():
    battery = hub.battery.capacity_left()
    print('Battery: '+str(battery) + '%')

_,_,roll = hub.motion.yaw_pitch_roll()
upright.run_for_degrees(270,-100)
time.sleep(0.1)
pos = upright.get()
while pos[0] != 0:
    # print(pos[0])
    time.sleep(0.1)
    pos = upright.get()
upright.preset(0)
wheel_left.preset(0)
wheel_right.preset(0)
p_roll = roll
for set_pos in range(80,180):
    pos = upright.get()
    # print('-'.join(map(str,pos)))
    upright.run_to_position(set_pos,100,100,2)
    pos = upright.get()
    ct = time.ticks_ms()
    while pos[1] < set_pos - max_dev or pos[1] > set_pos + max_dev and time.ticks_ms() - ct < 100:
        pos = upright.get()
        pass
    time.sleep(0.1)
    _,_,roll = hub.motion.yaw_pitch_roll()
    if roll > 92 and roll - p_roll > 1:
        roll_target = p_roll
        break
    p_roll = roll
    # print('Roll: {}'.format(roll))
upright.run_to_position(0,100,100)
print("Roll_target: {}".format(roll_target))
roll_target=roll+4
kp = 13 #proportional gain
ki = 4.2 #integral gain
kd = 140 #derivative gain
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
hub.led(0,255,0)
ct = time.time()
wl = wheel_left.get()[1]
wr = wheel_right.get()[1]*-1
_,_,angle = hub.motion.yaw_pitch_roll()
while angle<roll_target+40 and angle>roll_target-40:
    error = roll_target - angle
    integral = integral + (error*0.25)
    derivative = error - prev_error
    prev_error = error
    start = (start_target - wheel_left.get()[1])
    result = (error*kp) + (integral*ki) + (derivative*kd) + (start*ks)
    power = math.floor(result)
    wheels.start_at_power(power)
    _,_,angle = hub.motion.yaw_pitch_roll()
    if time.time()-ct > 2:
        wln = wheel_left.get()[1]
        wrn = wheel_right.get()[1]*-1
        total = wln - wl + wrn - wr
        print('---\n',total)
        wl = wln
        wr = wrn
        ct = time.time()
        if total < -5:
            roll_target += -1
        elif total > 5:
            roll_target += 1
        print(roll_target)
wheels.stop()
hub.led(255,0,0)