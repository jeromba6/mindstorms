import hub
import time

colorsensor = hub.port.C.device

colorsensor.mode(0)
colors = {
    0: 'black',
    3: 'blue',
    5: 'green',
    7: 'yellow',
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