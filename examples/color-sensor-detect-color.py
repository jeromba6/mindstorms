# LEGO type:standard slot:2 autostart

import hub
import time

colorsensor = hub.port.C.device

colorsensor.mode(0)
colors = {
    0: 'black',
    1: 'pink',
    2: 'violet',
    3: 'blue',
    4: 'light blue',
    5: 'light green',
    6: 'green',
    7: 'yellow',
    8: 'orange',
    9: 'red',
    10: 'white'
}
battery = 0
hub.battery.capacity_left()
pcolor = -1 # Set to a value that doesn't exist so it won't match the initial round.
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))

    color = colorsensor.get()[0]
    if pcolor != color:
        if color != None:
            if color in colors.keys():
                print('Detected color: ', colors[color])
            else:
                print('Detected color number: ', color)
        else:
            print('No color detected.')
        pcolor = color
    time.sleep(1)