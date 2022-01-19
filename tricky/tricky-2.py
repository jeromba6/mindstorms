# LEGO type:standard slot:2 autostart

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

    # def break(self):
    #     self.motor_left.break()
    #     self.motor_right.break()

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

wheels = motor_pair('A','B')
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

image_none = [
    '90009',
    '09090',
    '00900',
    '09090',
    '90009']

dist_range = max_distance - activate_distance
nr_leds = 25

while True:
    distance = sensor_us.get()[0]

    if distance and distance < activate_distance:
        hub.display.show(hub.Image.HAPPY)
        hub.led((255,0,0))
        wheels.float()
        wheels.run_at_speed(-40,0)
        time.sleep(2)
        wheels.run_at_speed(30,-100)
        time.sleep(1)
    else:
        if distance == None:
            wheels.run_at_speed(80)
            intensity = 0
            img=hub.Image(':'.join(image_none))
        else:
            wheels.run_at_speed(50)
            intensity = 255 - int((distance - activate_distance) / (max_distance-activate_distance)*255)
            leds_on = (distance - activate_distance) / dist_range * nr_leds
            nr_leds_on = int(leds_on)
            next_led = str(int(leds_on - nr_leds_on * 10))
            leds = '9' * nr_leds_on + next_led
            leds += '0' * (25 - len(leds))
            img=hub.Image(leds[0:5] + ':' + leds[5:10] + ':' + leds[10:15] + ':' + leds[15:20] + ':' + leds[20:25])
        hub.led((0,intensity,0))
        hub.display.show(img)
        time.sleep(0.1)