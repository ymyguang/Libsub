# from qcloud_cos_v5 import requests
import datetime
import requests


# 使用时，删除一下两行，并在下方加入cookies和座位号
class privitec:
    cookie = "ASP.NET_SessionId=wnit24qis30eanezqvsqfmu3; Reader_barcode=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserIdentID=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserOpenID=WechatTSG=1008220200902091753255265176; UserName=WechatTSG=%e5%88%98%e5%bd%aa; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e5%88%98%e5%bd%aa; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1606400922; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1606400922"
    seat = "101014033"


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


def feedback(result):
    params = {
        "text": result[1:]
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
    while len(result) < 50 and i < 3000:
        r = requests.post(SEAT, headers=HEADERS, json={"seatNum": seat})  # 读取座位信息/六楼走廊
        result = r.text
        print(result)
        i += 1
    return result


feedback(sub())
