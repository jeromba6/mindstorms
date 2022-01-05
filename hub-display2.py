import hub
import time

image=[
    '00900',
    '09990',
    '99999',
    '00900',
    '00900'
]

battery = 0
hub.battery.capacity_left()
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))
    print(hub.RIGHT)
    img=hub.Image(':'.join(image))
    hub.display.align(hub.RIGHT)
    hub.display.show(img)
    time.sleep(1)
    hub.display.rotation(90)
    hub.display.show(img)
    time.sleep(1)
    hub.display.rotation(180)
    hub.display.show(img)
    time.sleep(1)
    hub.display.rotation(-90)
    hub.display.show(img)
    time.sleep(1)
