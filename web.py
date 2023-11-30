import time

def countdown_timer(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("lets go!")

seconds = input("Enter the number of seconds you want to count down from: ")

countdown_timer(int(seconds))