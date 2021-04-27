import requests
import time
import datetime

from privite import privitec

p = privitec()
URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"

# 设置参数
cookie = p.cookie  # 等号后，填写cookie
seat = p.seat  # 等号后，填写座位号

SITE = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {
    'Cookie': '',
    'X-AjaxPro-Method': 'submitBespeak',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}
ROOM = [1010140, 1010050, 1010080, 1010110]
ROOM_NAME = ['六楼走廊', '三楼走廊', '四楼走廊', '五楼走廊']
SEAT = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
        74, 75, 76, 77, str("01"), str("02"), str("03"), str("04"), str("05"), str("06"), str("07"), str("08"),
        str("09"), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]


def feedback(result, str1):
    params = {
        "text": result[1:],
        'desp': str1
    }
    requests.get(url=URL, params=params)


hour = 21
d = int(datetime.datetime.now().weekday())
if d == 2:
    hour = 11

today = datetime.date.today()
now_time = datetime.datetime.now().strftime('%H')
delay = 0
if int(now_time) >= 22:
    delay = 1
tomorrow_month = (today + datetime.timedelta(days=delay)).strftime('%m')
tomorrow_day = (today + datetime.timedelta(days=delay)).strftime('%d')
tomorrow_year = (today + datetime.timedelta(days=delay)).strftime('%Y')

HEADERS[
    'Cookie'] = cookie + "StrBespeakTime=" + str(tomorrow_year) + "%2f" + str(tomorrow_month) + "%2f" + str(
    tomorrow_day) + "+" + str(hour) + "%3a30%3a00"

cnt = 1
isok = 0
while 1:
    for i in range(0, len(ROOM)):
        if isok:
            break
        else:
            for j in range(0, len(SEAT)):
                seatnum = (str(ROOM[i]) + str(SEAT[j]))
                r = requests.post(SITE, headers=HEADERS, json={"seatNum": seatnum})  # 读取座位信息/六楼走廊
                result = r.text

                if result == "\"11\";/*":
                    result = '已被预约'
                print("第" + str(cnt) + "次尝试占座：" + "【" +
                      ROOM_NAME[i] + str(SEAT[j]) + "号】" + result)
                status = result[0:2]
                if status == "\"4" or status == "\"3":
                    isok = 1
                    break
                cnt += 1
                time.sleep(0.1)
    if isok:
        break
    else:
        print("轮询完成，将进行下一轮扫描：\n ***************************************")
        feedback("轮询完成未找到位置，十分钟后将进行下一轮扫描", "")
        time.sleep(10 * 60)

feedback(result, "")
