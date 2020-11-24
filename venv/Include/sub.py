import requests
import time
import datetime
import os

SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {
    'Cookie': '',
    'X-AjaxPro-Method': 'submitBespeak',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}

def delaytime():
    ACTION_TIME = 223305
    now = int(datetime.datetime.now().strftime("%H%M%S"))
    delay = ACTION_TIME - now
    while delay > 0:
        print("距抢座时间还有" + str(delay) + "秒")
        time.sleep(1)
        delay -= 1
        os.system("cls")


hour = str(21)
d = int(datetime.datetime.now().weekday())
if d == 3:
    hour = str(11)

today = datetime.date.today()
now_time = datetime.datetime.now().strftime('%H')
delay = 0
if int(now_time) >= 22:
    delay = 1
tomorrow_month = (today + datetime.timedelta(days=delay)).strftime('%m')
tomorrow_day = (today + datetime.timedelta(days=delay)).strftime('%d')
tomorrow_year = (today + datetime.timedelta(days=delay)).strftime('%Y')
HEADERS[
    'Cookie'] = "ASP.NET_SessionId=ou4h2ftudtaykra1543wk34s; Reader_barcode=WechatTSG=A3B25858882C96748B640873190B1D4F&WeChatUserCenter=1990752134; UserIdentID=WechatTSG=A3B25858882C96748B640873190B1D4F&WeChatUserCenter=1990752134; UserOpenID=WechatTSG=1008220201108173938977205291; UserName=WechatTSG=%e6%9d%8e%e6%a8%8a; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e6%9d%8e%e6%a8%8a; " \
                + "StrBespeakTime=" + tomorrow_year + "%2f" + tomorrow_month + "%2f" + tomorrow_day + "+" + hour + "%3a30%3a00"


delaytime()

i = 1
result = "ww"
while len(result) < 50:
    r = requests.post(SEAT, headers=HEADERS, json={"seatNum": "101014068"})  # 读取座位信息/六楼走廊
    if r.text == "\"11\";/*":
        result = '当前位置位置已被预约'
    else:
        result = r.text
    print("第" + str(i) + "次尝试占座：" + result)
    i += 1
    time.sleep(0.1)
i = input()
