import time
import random

def waiting_game():
    target = random.randint(2,4)
    print(f'\n Your target  time is {target} seconds')
    input(' ---Press Enter to Begin--- ')
    start = time.perf_counter()
    input(f'\n  ...Press Enter again after {target} seconds...')
    elapsed = time.perf_counter() - start
    print(f'\n Elapsed time: {elapsed:.3f} seconds')
    if elapsed == target:
        print('(Unbelievable! Perfect  timing!)')
    elif elapsed < target:
        print(f'({target - elapsed:.3f} seconds too fast)')
    elif elapsed > target:
        print(f'({elapsed - target:.3f} seconds too slow)')

# Please, uncomment the lines below to execute the code with the example given
# waiting_game()
