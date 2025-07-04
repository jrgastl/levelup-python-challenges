'''
Author Note:
I suddenly realized how poorly I implemented the input() function after checking the instructor solution. Overall the code still works, however, so I didn't change it that much.
I only added some small things like, for example, the feedback in case the player gets the time 100% correct. Besides that, it was resourceful to understand a bit how to use the time module. 
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
