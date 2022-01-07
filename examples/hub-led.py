import hub
import time

# Show battery status
battery = hub.battery.capacity_left()
print('Battery: '+str(battery) + '%')

# Set list for color R, G, B
color=[255,255,255]
while True:

    # Loop over the 3 values for the color
    for j in range(3):

        # Loop over the values to set the color
        for i in range(256):
            color[(j+1)%3] = i
            color[j]=255-i

            # Put selected color on brick button
            hub.led(tuple(color))

            # Wait 10 miliseconds befor applying next value
            time.sleep(0.01)
