import datetime
import os
import time
ACTION_TIME = 224844
now = int(datetime.datetime.now().strftime("%H%M%S"))
delay = ACTION_TIME - now
while delay > 0:
    print("距抢座时间还有" + str(delay) + "秒")
    time.sleep(1)
    delay -= 1
    os.system("cls")
