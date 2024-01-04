from emoji import emojize
from time import sleep

while True:
    print(emojize('\r:thumbs_up:'), end='')
    sleep(1)
    print(emojize('\r:thumbs_down:'), end='')
    sleep(1)
