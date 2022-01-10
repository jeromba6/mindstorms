# LEGO type:standard slot:11 autostart

import hub
import time
battery = 0

if battery != hub.battery.capacity_left():
    battery = hub.battery.capacity_left()
    print('Battery: '+str(battery) + '%')

while True:
    val=hub.status()['port']
    print(val.keys())
    for i in val.keys():
        print('    ', i,end=' - ')
        print(val[i])
    print()
    time.sleep(1)