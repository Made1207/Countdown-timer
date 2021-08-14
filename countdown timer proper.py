import time

hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

mainloop = 90 > 1
loop01 = 56 > 100
loop02 = 20 > 100
loop03 = 100 > 3

while mainloop  == True:
    if loop03 == True:
        if minutes >= 1 and hours >= 1:
            for i in range(seconds):
                print(hours, ':', minutes, ':', seconds)
                seconds = seconds - 1
                if seconds == 0:
                    time.sleep(1)
                    print(hours, ':', minutes, ':', seconds)
                    loop03 = False 
                    loop02 = True
                time.sleep(1)
        elif minutes >= 1 and hours >= 1 or minutes == 0 and hours >= 1 or minutes >= 1 and hours == 0:
            for i in range(seconds):
                print(hours, ':', minutes, ':', seconds)
                seconds = seconds - 1
                if seconds == 0:
                    time.sleep(1)
                    print(hours, ':', minutes, ':', seconds)
                    loop03 = False 
                    loop02 = True
                time.sleep(1)
        elif minutes == 0 and hours == 0:
            for i in range(seconds):
                print(hours, ':', minutes, ':', seconds)
                seconds = seconds - 1
                if seconds == 0:
                    time.sleep(1)
                    print(hours, ':', minutes, ':', seconds)
                    mainloop = False
                time.sleep(1)

    if loop02 == True:
        if minutes == 0:
            if hours == 0:
                seconds = 59
                loop03 = True
            elif hours > 0:
                hours = hours - 1
                minutes = 60
                seconds = 59
                loop03 = True
        seconds = 59
        minutes = minutes - 1
        loop03 = True     