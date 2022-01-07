import hub
import time

colorsensor = hub.port.C.device

led1 = 0  #brightness in range 0...9
led2 = 4  #brightness in range 0...9
led3 = 9  #brightness in range 0...9

colorsensor.mode(3)
colorsensor.mode(3,b''+chr(led1)+chr(led2)+chr(led3))

battery = 0
hub.battery.capacity_left()
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))
    nr_vars = len(colorsensor.get())
    vars = colorsensor.get()
    for i in range(nr_vars):
        vars[i] = (vars[i] + 3) % 10
        colorsensor.mode(3,b''+chr(vars[0])+chr(vars[1])+chr(vars[2]))
        time.sleep(0.3)