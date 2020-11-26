import datetime
import os
import time
i = 1000
ACTION_TIME = 22 * 3600 + 31 * 60 + 25  # 开放时间戳
now = str(datetime.datetime.now().strftime("%H%M%S"))
now_sec = int(now[0:2]) * 3600 + int(now[2:4]) * 60 + int(now[4:])  # 当前时间戳
delay = ACTION_TIME - now_sec
tem = datetime.datetime.now().strftime("%H:%M:%S")
i = 1
while i <= 1000:
    print("第" + str(i))
    print("距离开放预约时间还有【" + str(int(delay / 3600)) + "小时" + str(int(delay % 3600 / 60)) + "分钟" + str(
        int(delay % 3600 % 60)) + "秒】，请耐心等待")
    time.sleep(0.9)
    i += 1
    os.system("cls")
print(datetime.datetime.now().strftime("%H:%M:%S") + "\n" + tem)
i = input()
