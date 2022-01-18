# LEGO type:standard slot:4 autostart

import hub
import time

# Define on which port the distance sensor is connected
distance_sensor = hub.port.D.device

# Set the mode for the distance sensor to DISTL(distance long)
distance_sensor.mode(0)

# Define variable that holds the prefious value
pval = 0

# Infinate loop
while True:

    # Get the mesurement of the sensor
    val = distance_sensor.get()

    # Take action when value is diffrent form previouse value
    if val[0] != pval:

        # When no mesurement can be done
        if val[0] == None:
            print('Can\'t determine the distance.')

        # Output mesurement
        else:
            print('Distance in cm: ',val[0])

        # Set pervious value to current value
        pval = val[0]

    # Wait before new cycle
    time.sleep(1)
