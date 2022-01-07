import hub
import time
battery = 0

if battery != hub.battery.capacity_left():
    battery = hub.battery.capacity_left()
    print('Battery: '+str(battery) + '%')

class motor_pair:
    def __init__(self, a, b, a_reverse=True, b_reverse=False):
        self.motor_a = set_motor(a)
        self.motor_b = set_motor(b)
        self.a_reverse = a_reverse
        self.b_reverse = b_reverse

    def move(self, speed=100, direction=0):
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100
        if direction > 100:
            direction = 100
        if direction < -100:
            direction = -100
        speed_a = speed * (1 - 2 * self.a_reverse)
        speed_b = speed * (1 - 2 * self.b_reverse)
        if direction > 0:
            speed_b = int(speed_b * (50 - direction) / 50)
        if direction < 0:
            speed_a = int(speed_a * (50 + direction) / 50)
        self.motor_a.pwm(speed_a)
        self.motor_b.pwm(speed_b)

    def stop(self):
        self.motor_a.pwm(0)
        self.motor_b.pwm(0)


def set_motor(var):
    if var == 'A':
        return hub.port.A
    if var == 'B':
        return hub.port.B
    if var == 'C':
        return hub.port.C
    if var == 'D':
        return hub.port.D
    if var == 'E':
        return hub.port.E
    if var == 'F':
        return hub.port.F

wheels = motor_pair('A','E')

# foward
wheels.move()
time.sleep(2)

# turn right
wheels.move(direction=50)
time.sleep(1)

# turn left in place
wheels.move(direction=-100)
time.sleep(1)

# half speed backup
wheels.move(-50)
time.sleep(1)

wheels.stop()