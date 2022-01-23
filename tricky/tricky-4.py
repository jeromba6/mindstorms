# LEGO type:standard slot:4 autostart
"""
Follow line

This works as follows:
When the green light goes is turned off move the colorsensor over the line so it can detrmine the
low and high value for reflection of the line and the background, be sure not to lift the robot
during this callibration. When te callibration is done press the left button then the line following
starts. Have fun and try adjusting some parameters
"""

import hub
import time

class motor_pair:
    def __init__(
        self,
        left_motor_port:str = 'A',
        right_motor_port:str = 'B',
        left_reverse:bool = True,
        right_reverse:bool = False,
        default_speed:int = 70,
        default_max_power: int = 70,
        default_acceleration: int = 0,
        default_deceleration: int = 0
    ):
        self.motor_left = hub.port.__dict__[left_motor_port].motor
        self.motor_right = hub.port.__dict__[right_motor_port].motor
        self.left_reverse = left_reverse
        self.right_reverse = right_reverse
        self.default_speed = default_speed
        self.default_max_power = default_max_power
        self.default_acceleration = default_acceleration
        self.default_deceleration = default_deceleration


    def float(self):
        self.motor_left.float()
        self.motor_right.float()

    def hold(self):
        self.motor_left.hold()
        self.motor_right.hold()

    def pwm(self, speed:int = None, direction:int = 0):
        speed = self.default_speed if speed == None else speed
        speed_left, speed_right = self.determine_motors_speed(speed, direction)
        self.motor_left.pwm(speed_left)
        self.motor_right.pwm(speed_right)

    def run_at_speed(self, speed:int = None, direction:int = 0, max_power:int = None, acceleration:int = None, deceleration:int = None):
        # to add (max_power: int, acceleration: int, deceleration: int)
        speed = self.default_speed if speed == None else speed
        max_power = self.default_max_power if max_power == None else max_power
        acceleration = self.default_acceleration if acceleration == None else acceleration
        deceleration = self.default_deceleration if deceleration == None else deceleration
        speed_left, speed_right = self.determine_motors_speed(speed, direction)
        self.motor_left.run_at_speed(speed_left,max_power,acceleration,deceleration)
        self.motor_right.run_at_speed(speed_right,max_power,acceleration,deceleration)

    def run_for_time(self, msec:int, speed:int = None, direction:int = 0, max_power:int = None, acceleration:int = None, deceleration:int = None):
        speed = self.default_speed if speed == None else speed
        max_power = self.default_max_power if max_power == None else max_power
        acceleration = self.default_acceleration if acceleration == None else acceleration
        deceleration = self.default_deceleration if deceleration == None else deceleration
        speed_left, speed_right = self.determine_motors_speed(speed, direction)
        self.motor_left.run_for_time(msec, speed_left,max_power,acceleration,deceleration)
        self.motor_right.run_for_time(msec, speed_right,max_power,acceleration,deceleration)

    def run_for_degrees(self, degrees:int, speed:int = None, direction:int = 0, max_power:int = None, acceleration:int = None, deceleration:int = None):
        # Todo fix degrees depending on direction
        speed = self.default_speed if speed == None else speed
        max_power = self.default_max_power if max_power == None else max_power
        acceleration = self.default_acceleration if acceleration == None else acceleration
        deceleration = self.default_deceleration if deceleration == None else deceleration
        speed_left, speed_right = self.determine_motors_speed(speed, direction)
        degrees_left, degrees_right = self.determine_motors_degrees(degrees, direction)
        self.motor_left.run_for_degrees(degrees, speed_left,max_power,acceleration,deceleration)
        self.motor_right.run_for_degrees(degrees, speed_right,max_power,acceleration,deceleration)

    def determine_motors_speed(self, speed, direction):
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100
        if direction > 100:
            direction = 100
        if direction < -100:
            direction = -100
        speed_left = speed * (1 - 2 * self.left_reverse)
        speed_right = speed * (1 - 2 * self.right_reverse)
        if direction > 0:
            speed_right = int(speed_right * (50 - direction) / 50)
        if direction < 0:
            speed_left = int(speed_left * (50 + direction) / 50)
        return speed_left, speed_right

    def determine_motors_degrees(self, degrees, direction):
        degrees_left, degrees_right = self.determine_motors_speed(degrees, direction)
        return abs(degrees_left), abs(degrees_right)

wheels = motor_pair('A', 'B')
arm          = hub.port.C.motor
sensor_us    = hub.port.D.device
sensor_color = hub.port.E.device

sensor_color.mode(0)
arm.run_for_degrees(360,speed=20)
for i in range(255,-1,-1):
    hub.led((0,i,0))
    time.sleep(0.005)

nr_leds = 25

# # arm.mode((3,0))
while arm.busy(1):
    time.sleep(0.01)
arm.preset(0)

wheels.run_at_speed(40)
distance = sensor_us.get()[0]
while not distance or distance > 5:
    time.sleep(0.05)
    distance = sensor_us.get()[0]

wheels.float()

arm.run_to_position(-90, speed=20)
while arm.busy(1):
    time.sleep(0.01)

wheels.run_at_speed(-20)
while not sensor_color.get()[0] == 4:
    print(sensor_color.get()[0])
    time.sleep(0.05)

wheels.hold()
arm.run_to_position(-240,speed=100)
while arm.busy(1):
    time.sleep(0.01)

arm.run_to_position(-90,20)
wheels.run_for_degrees(180)