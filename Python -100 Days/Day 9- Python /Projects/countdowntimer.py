# Countdown timer 
# input time and count down to 0 

import time # Time Function 

def countdown(t):
    while t:
# convert command 
     min,secs = divmod(t,60) # Conversion divmod 
     # f string which is used {min:02d - d is integer,02 two decimal places}
     timer = f"{min: 02d}:{secs:02d}" 
     print(timer)
     # end ="\r" - don't go to new line go to the beginning of same line 
     print(timer, end ="\r")
     time.sleep(1) # Pause of 1 second
     t-=1 # Reduce the seconds so loop reduces to 0

     print("00.00")
     print("Time's up")


countdown(180)









