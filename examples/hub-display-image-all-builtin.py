import hub
import time
import sys

battery = 0
hub.battery.capacity_left()
hub.display.align(hub.LEFT)
images = dir(hub.Image)
print(images)
while True:
    if battery != hub.battery.capacity_left():
        battery = hub.battery.capacity_left()
        print('Battery: '+str(battery))
    for image in images:
        if image.upper() != image:
            continue
        print(image)
        img = hub.Image.__dict__[image]
        hub.display.show(img)
        time.sleep(1)
