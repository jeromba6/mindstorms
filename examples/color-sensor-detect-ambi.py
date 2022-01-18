# LEGO type:standard slot:3 autostart

import hub
import time

colorsensor = hub.port.C.device

battery = 0
hub.battery.capacity_left()
pambiance = -1 # Set to a value that doesn't exist so it won't match the initial round.
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))

    ambiance = colorsensor.get()[0]
    if pambiance != ambiance:
        if ambiance:
            print('Ambiance light: ', ambiance)
        else:
            print('No light detected.')
        pambiance = ambiance
    time.sleep(1)