import sched
import time
import os

def alarm(sound_file,message):
    os.system('start' + sound_file)
    return print(message)

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{(function.__name__)}() scheduled  for {time.asctime(time.localtime(event_time))}')
    s.run()

schedule_function((time.time()+2),alarm,'./sounds/Ring08.wav','Good morning!')
#schedule_function((time.time()+2),print,'Howdy!')s