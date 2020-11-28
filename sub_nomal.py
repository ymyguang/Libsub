import requests
import datetime


class subclass:
    seatNum = ""

    def sub(self, num):
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
                "text": result,
                'desp': "当前是第" + str(str1) + "次扫描！"
            }
            requests.get(url="https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send",
                         params=params)

        hour = str(21)
        d = int(datetime.datetime.now().weekday())
        if d == 2:
            hour = str(11)

        today = datetime.date.today()
        delay = 0

        tomorrow_month = (today + datetime.timedelta(days=delay)).strftime('%m')
        tomorrow_day = (today + datetime.timedelta(days=delay)).strftime('%d')
        tomorrow_year = (today + datetime.timedelta(days=delay)).strftime('%Y')
        HEADERS[
            'Cookie'] = "ASP.NET_SessionId=e1by510tkh1td31dl5pgzq2h; Reader_barcode=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserIdentID=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserOpenID=WechatTSG=1008220201127223551561013081; UserName=WechatTSG=%e7%a9%86%e4%bf%8a%e5%87%af; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e7%a9%86%e4%bf%8a%e5%87%af;" \
                        + "StrBespeakTime=" + tomorrow_year + "%2f" + tomorrow_month + "%2f" + tomorrow_day + "+" + str(
            hour) + "%3a30%3a00"

        r = requests.post(SEAT, headers=HEADERS, json={"seatNum": self.seatNum})  # 读取座位信息/六楼走廊
        if r.text == "\"11\";/*":
            result = '当前位置位置已被预约'
        else:
            result = r.text
        print(result)
        feedback(result, num)


"""
p = subclass()
p.seatNum = ""
p.sub(1)
"""
