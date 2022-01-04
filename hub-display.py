import hub
import time
import random
snake = [[0,0]]*9
print(snake)
while True:
    move_x = random.randint(-1,1)
    move_y = random.randint(-1,1)
    x ,y = snake[0][0]+move_x, snake[0][1]+move_y
    if x < 0:
        x = 0
    if x > 4:
        x =4
    if y < 0:
        y = 0
    if y > 4:
        y = 4
    if [x, y] == snake[0]:
        continue
    for i in range(len(snake)-1):
        pos = len(snake) - 1 - i
        b = int(i*9/len(snake))
        hub.display.pixel(snake[pos][0],snake[pos][1],b)
        snake[pos] = snake[pos-1]
    hub.display.pixel(x,y,9)
    snake[0] = [x,y]
    time.sleep(0.2)