import time 

def countdown(t): # function to start countdown
    while t: # while loop to run until time reaches 0
        mins, secs = divmod(t, 60) # convert time to minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs) # format time string
        print(timer, end="\r") # print time with return at end
        time.sleep(1) # wait for 1 second
        t -= 1 # decrement time by 1 second
    print('Timer completed!') # print timer completed message

    t = input("Enter the time in seconds: ") # take user input for time in seconds
    countdown(int(t)) # call countdown function with input time