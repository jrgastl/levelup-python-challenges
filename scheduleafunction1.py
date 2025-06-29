## Brief:
#Python function which sets an alarm that plays a sound and prints a message at a specified time.
#Three inputs: event time, function and any number of arguments.
#Sound file, printing a message at a specified time.
#A call might look like this schedule_function(time.time()+1,print,'Howdy'):
import time
import os

def alarm(sound_file,message):
    os.system('start' + sound_file)
    return print(message)

def schedule_function(set_time,user_function,*args):
    if set_time <= time.time():
        print('Desire time is in the past')
    else:
        print(f'{(user_function.__name__)}() scheduled  for {time.asctime(time.localtime(set_time))}')
        while set_time >= time.time():
            if set_time <= time.time():
                return user_function(*args)

schedule_function((time.time()+2),print,'Howdy!')
#schedule_function((time.time()+2),alarm,'./sounds/Ring08.wav','Good morning!')