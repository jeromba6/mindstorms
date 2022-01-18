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

tone = {'C0':	16.35,
        'C#0':	17.32,
        'D0':	18.35,
        'D#0':	19.45,
        'E0':	20.60,
        'F0':	21.83,
        'F#0':	23.12,
        'G0':	24.50,
        'G#0':	25.96,
        'A0':	27.50,
        'A#0':	29.14,
        'B0':	30.87,
        'C1':	32.70,
        'C#1':	34.65,
        'D1':	36.71,
        'D#1':	38.89,
        'E1':	41.20,
        'F1':	43.65,
        'F#1':	46.25,
        'G1':	49.00,
        'G#1':	51.91,
        'A1':	55.00,
        'A#1':	58.27,
        'B1':	61.74,
        'C2':	65.41,
        'C#2':	69.30,
        'D2':	73.42,
        'D#2':	77.78,
        'E2':	82.41,
        'F2':	87.31,
        'F#2':	92.50,
        'G2':	98.00,
        'G#2':	103.83,
        'A2':	110.00,
        'A#2':	116.54,
        'B2':	123.47,
        'C3':	130.81,
        'C#3':	138.59,
        'D3':	146.83,
        'D#3':	155.56,
        'E3':	164.81,
        'F3':	174.61,
        'F#3':	185.00,
        'G3':	196.00,
        'G#3':	207.65,
        'A3':	220.00,
        'A#3':	233.08,
        'B3':	246.94,
        'C4':	261.63,
        'C#4':	277.18,
        'D4':	293.66,
        'D#4':	311.13,
        'E4':	329.63,
        'F4':	349.23,
        'F#4':	369.99,
        'G4':	392.00,
        'G#4':	415.30,
        'A4':	440.00,
        'A#4':	466.16,
        'B4':	493.88,
        'C5':	523.25,
        'C#5':	554.37,
        'D5':	587.33,
        'D#5':	622.25,
        'E5':	659.25,
        'F5':	698.46,
        'F#5':	739.99,
        'G5':	783.99,
        'G#5':	830.61,
        'A5':	880.00,
        'A#5':	932.33,
        'B5':	987.77,
        'C6':	1046.50,
        'C#6':	1108.73,
        'D6':	1174.66,
        'D#6':	1244.51,
        'E6':	1318.51,
        'F6':	1396.91,
        'F#6':	1479.98,
        'G6':	1567.98,
        'G#6':	1661.22,
        'A6':	1760.00,
        'A#6':	1864.66,
        'B6':	1975.53,
        'C7':	2093.00,
        'C#7':	2217.46,
        'D7':	2349.32,
        'D#7':	2489.02,
        'E7':	2637.02,
        'F7':	2793.83,
        'F#7':	2959.96,
        'G7':	3135.96,
        'G#7':	3322.44,
        'A7':	3520.00,
        'A#7':	3729.31,
        'B7':	3951.07,
        'C8':	4186.01,
        'C#8':	4434.92,
        'D8':	4698.63,
        'D#8':	4978.03,
        'E8':	5274.04,
        'F8':	5587.65,
        'F#8':	5919.91,
        'G8':	6271.93,
        'G#8':	6644.88,
        'A8':	7040.00,
        'A#8':	7458.62,
        'B8':	7902.13}

# (Tone, duration)
melody=(
  ('G4',2), ('G4',2), ('A4',8), ('G4',8), ('C5',8), ('B4',16), (0,1),
  ('G4',2), ('G4',2), ('A4',8), ('G4',8), ('D5',8), ('C5',16), (0,1),
  ('G4',2), ('G4',2), ('G5',8), ('E5',8), ('C5',8), ('B4',8), ('A4',16), (0,1),
  ('F5',2), ('F5',2), ('E5',8), ('C5',8), ('D5',8), ('C5',16))

wholeNoteLeght = 60

colorsensor = hub.port.C.device

hub.sound.volume(9)
colorsensor.mode(3)
led_color_sensor = [0,0,0]
colorsensor.mode(3,b''+chr(led_color_sensor[0])+chr(led_color_sensor[1])+chr(led_color_sensor[2]))

led_distance_sensor = [0,9,0,9]
led_distance_sensor_nr = 0
sensor_distance.mode(5,b''+chr(led_distance_sensor[0])+chr(led_distance_sensor[1])+chr(led_distance_sensor[2])+chr(led_distance_sensor[3]))
hub.display.align(hub.motion.orientation())
image = (hub.Image.HAPPY, hub.Image.SMILE)
imageno = 0
color = [0,1,0]
colornr=0
arms = ((-70,0),(0,50),(70,0),(0,-50))
arms_nr = 0
arm_right.run_for_degrees(90,-50)

for i in range(len(melody)):
    if melody[i][0]:
        hub.sound.beep( int( tone[melody[i][0]] ), int( wholeNoteLeght * melody[i][1] ))
        hub.display.show(image[imageno])
        hub.led(255*color[0],255*color[1],255*color[2])
        color[colornr] = (color[colornr] + 1) % 2
        colornr = (colornr + 1) % len(color)
        imageno = (imageno + 1) % len(image)
        led_color_sensor = [0,0,0]
        led_color_sensor[colornr] = 9
        colorsensor.mode(3,b''+chr(led_color_sensor[0])+chr(led_color_sensor[1])+chr(led_color_sensor[2]))
        arm_right.run_for_degrees(90,arms[arms_nr][0])
        arm_left.run_for_degrees(90,arms[arms_nr][1])
        arms_nr = (arms_nr + 1) % len(arms)
        sensor_distance.mode(5,b''+chr(led_distance_sensor[0])+chr(led_distance_sensor[1])+chr(led_distance_sensor[2])+chr(led_distance_sensor[3]))
        led_distance_sensor[led_distance_sensor_nr] = (led_distance_sensor[led_distance_sensor_nr]-9) * -1
        led_distance_sensor_nr = (led_distance_sensor_nr + 1) % len(led_distance_sensor)
    time.sleep( wholeNoteLeght * ( melody[i][1] + 0.5 ) / 1000 )
hub.led(255*color[0],255*color[1],255*color[2])
hub.display.show(hub.Image.HAPPY)
colorsensor.mode(3,b''+chr(0)+chr(0)+chr(0))
sensor_distance.mode(5,b''+chr(0)+chr(0)+chr(0)+chr(0))
for i in range(254,-1,-1):
    hub.led(i*color[0],i*color[1],i*color[2])
    time.sleep(.01)

