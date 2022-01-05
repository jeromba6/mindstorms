import hub
import time

image=[
    '00900',
    '09990',
    '95959',
    '00900',
    '00900'
]

battery = 0
hub.battery.capacity_left()
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))
    img=hub.Image(':'.join(image))
    hub.display.align(hub.RIGHT)
    hub.display.show(img)
    time.sleep(1)
    hub.display.align(hub.FRONT)
    hub.display.show(img)
    time.sleep(1)
    hub.display.align(hub.LEFT)
    hub.display.show(img)
    time.sleep(1)
    hub.display.align(hub.BACK)
    hub.display.show(img)
    time.sleep(1)
