import hub
import time

# Dim button light
hub.led((0,0,0))

# Rotate display 90 counter clockwise
hub.display.align(5)

# Define text to display
text = "Mindstorms is cool"

# Begin with white space
text_scroll = ["00000"]*5

# Loop over each character of the text
for char in text:

    # getting text and making it proportional

    # A space is known how it looks like
    if char == ' ':
        new_char = ['00'] * 5

    # Any other character display it
    else:
        hub.display.show(char)

        # Retrieve the pixels status
        new_char = hub.status()['display'].split(':')

        # When all pixels in the first colomn are '0' remove colomn
        for i in range(4):
            remove_col = True
            for j in range(5):
                if new_char[j][0] != '0':
                    remove_col = False
                    break
            if remove_col:
                for j in range(5):
                    new_char[j] =  new_char[j][1:]
            else:
                break

        # When all pixels of the last colomn are '0' remove colomn
        for i in range(len(new_char[0])-1):
            remove_col = True
            for j in range(5):
                if new_char[j][-1] != '0':
                    remove_col = False
                    break
            if remove_col:
                for j in range(5):
                    new_char[j] =  new_char[j][0:-1]
            else:
                break

    # Add the slimmed down character to scroll_text
    for i in range(5):
        text_scroll[i] += new_char[i] + '0'

# Add additional white space at the end
for i in range(5):
    text_scroll[i] += '00000'

# Setup variable
image = [''] * 5
sleep_time = 0.3
speed_change = 1.1

# Infite loop
while True:

    # Loop over scrolling text and shift right 1 colomn each iteration
    for i in range(len(text_scroll[0])-5):

        # decrease speed
        for j in range(hub.button.left.presses()):
            sleep_time = sleep_time * speed_change

        # increase speed
        for j in range(hub.button.right.presses()):
            sleep_time = sleep_time / speed_change

        # Set display to correct position
        hub.display.align(hub.motion.orientation())

        # Fill all rows
        for j in range(5):
            image[j] = text_scroll[j][i:i+5]

        # Generate image for display
        img = hub.Image(':'.join(image))

        # Display the image
        hub.display.show(img)

        # Wait for dispaying next image
        time.sleep(sleep_time)

    # End of cycle so wait some extra
    time.sleep(sleep_time * 3)
