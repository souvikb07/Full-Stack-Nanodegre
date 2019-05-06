import webbrowser
import time

n = 1
print('Your Program Starts at ' + time.ctime())
while n <= 3:
    time.sleep(4)
    webbrowser.open('https://www.youtube.com/watch?v=-tJOTReUjKE', new=2)
    print('Break ' + str(n) + ' Starts at ' + time.ctime())
    n += 1
