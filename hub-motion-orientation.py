import hub
import time

while True:
    print(hub.motion.orientation())
    hub.display.align(hub.motion.orientation())
    hub.display.show(hub.Image.ARROW_N)
    time.sleep(1)