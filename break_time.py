import time
import webbrowser

# Loops 3 times, prompting the user to take a break with
# their favorite music video. Uses the Pomodoro timing method.
# 25 minutes on, 5 minutes off. 

x = 0
for x in range(0,3):
    time.sleep(25 * 60)
    webbrowser.open("https://www.youtube.com/watch?v=ALj5MKjy2BU")
    time.sleep(5 * 60);
