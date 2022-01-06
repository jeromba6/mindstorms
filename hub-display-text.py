import hub
import time

# Dim button light
hub.led((0,0,0))

# Rotate display 90 counter clockwise
hub.display.align(5)

# Define text to display
text="Mindstorms is cool"

# Infinate loop
while True:

    # Loop over each character of the text
    for char in text:

        # Display the caracter
        hub.display.show(char)

        # Wait for half a second
        time.sleep(.5)

        # Clear display, this is done to see a blink when the same character is shown twice after each other
        hub.display.clear()

        # Wait just long enough to see the blink
        time.sleep(0.05)

    # Wait a bit extra at the end of the string    
    time.sleep(0.95)
