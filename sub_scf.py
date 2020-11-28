import datetime
import requests
import time


# 使用时，删除一下两行，并在下方加入cookies和座位号
class privitec:
    cookie = "ASP.NET_SessionId=e1by510tkh1td31dl5pgzq2h; Reader_barcode=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserIdentID=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserOpenID=WechatTSG=1008220201127223551561013081; UserName=WechatTSG=%e7%a9%86%e4%bf%8a%e5%87%af; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e7%a9%86%e4%bf%8a%e5%87%af;"
    seat = "101014066"  #14是走廊，12是南区（均四楼）


start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

p = privitec()
# 设置参数
cookie = p.cookie  # 等号后，填写cookie
seat = p.seat  # 等号后，填写座位号

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {
    'Cookie': '',
    'X-AjaxPro-Method': 'submitBespeak',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def feedback(result, str1):
    params = {
        "text": result[1:],
        'desp': str1
    }
    requests.get(url=URL, params=params)


def juagehour():
    hour = str(21)
    delay = 1
    d = int(datetime.datetime.now().weekday())
    if d == 2:  # 周三，明天周四->明天，修改时间到上午
        hour = str(11)
    elif d == 3:
        now_time = int(datetime.datetime.now().strftime('%H'))
        if int(now_time) < 19:
            delay = 0
            hour = str(20)  # 周四下午六点
    return delay, hour


def flashcookie(cookie):
    today = datetime.date.today()
    delay, hour = juagehour()
    tomorrow_month = (today + datetime.timedelta(days=delay)).strftime('%m')
    tomorrow_day = (today + datetime.timedelta(days=delay)).strftime('%d')
    tomorrow_year = (today + datetime.timedelta(days=delay)).strftime('%Y')
    flashcookie = cookie + "StrBespeakTime=" + tomorrow_year + "%2f" + tomorrow_month + "%2f" + tomorrow_day + "+" + hour + "%3a20%3a00"
    return flashcookie


def sub():
    i = 1
    HEADERS['Cookie'] = flashcookie(cookie)
    result = "ww"
    while len(result) < 50 and i < 500:
        r = requests.post(SEAT, headers=HEADERS, json={"seatNum": seat})
        result = r.text
        if result != """"3对不起当前日期或时间段暂不开放预约!";/*""":
            break
        time.sleep(0.1)
        i = i + 1
    str1 = '第' + str(i) + "次请求  \n 开始时间：" + str(start) + '   \n 结束时间：' + str(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return result, str1


def main(x, y):
    s, ss = sub()
    feedback(s, ss)  # 推送结果
