import hub
import time

def turn_left(image):
    new_image = ['']*5
    for line in image:
        for i in range(5):
            new_image[4-i] += line[i]
    return new_image

def turn_upside_down(image):
    new_image = turn_left(image)
    return turn_left(new_image)

def turn_right(image):
    new_image = turn_left(image)
    new_image = turn_left(new_image)
    return turn_left(new_image)

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
    img=hub.Image(':'.join(image))
    hub.display.show(img)
    time.sleep(1)
    img=hub.Image(':'.join(turn_right(image)))
    hub.display.show(img)
    time.sleep(1)
    img=hub.Image(':'.join(turn_upside_down(image)))
    hub.display.show(img)
    time.sleep(1)
    img=hub.Image(':'.join(turn_left(image)))
    hub.display.show(img)
    time.sleep(1)
