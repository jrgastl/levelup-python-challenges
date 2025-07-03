'''
Learned different ways of using the input() function and time module.
'''

import time
import random

def waiting_game():
    seconds = random.randint(2,5)
    print(f'Time to achieve is {seconds} seconds')
    print('---Press Enter to Begin---')
    keyPressed = input()
    if keyPressed != None:
        startTime = time.time()
        print(f'Press Enter again after {seconds} seconds')
        keyPressedAgain = input()
        if keyPressedAgain != None:
            endTime = time.time()
    elapsedTime = endTime - startTime
    if elapsedTime > seconds:
        print(f'Elapsed time: {round(elapsedTime,3)} seconds. ({round(elapsedTime - seconds,3)} too slow)')
    elif elapsedTime < seconds:
        print(f'Elapsed time: {round(elapsedTime,3)} seconds. ({round(seconds - elapsedTime,3)} too fast)')
    elif elapsedTime == seconds:
        print(f'Elapsed time: {round(elapsedTime,3)} seconds. (Unbelievable!)')

waiting_game()
