from time import sleep
from random import randint

back = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 '
with open('data.txt', 'w+') as f:
    f.write(back)

while True:
    with open('data.txt', 'a') as f:
        f.write(str(randint(30, 40)) + ' ')
    sleep(1)




