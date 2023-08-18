import rotatescreen
import time
screen = rotatescreen.get_primary_display()
screen.rotate_to(0)
for i in range(0):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)
