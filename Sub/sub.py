import requests

cookieDic = {
    "my": "ASP.NET_SessionId=wldmrppkfwpiiu2xo5eirup2; Reader_barcode=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserIdentID=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserOpenID=WechatTSG=1008220200902091753255265176; UserName=WechatTSG=%e5%88%98%e5%bd%aa; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e5%88%98%e5%bd%aa;",
    "other": "ASP.NET_SessionId=wldmrppkfwpiiu2xo5eirup2; Reader_barcode=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserIdentID=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserOpenID=WechatTSG=1008220201127223551561013081; UserName=WechatTSG=%e7%a9%86%e4%bf%8a%e5%87%af; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e7%a9%86%e4%bf%8a%e5%87%af;"
}
# SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.ChooseSeat.ChooseSeatList,WechatTSG.Web.ashx"
SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {
    # 'Cookie': cookieDic["my"],
    'Cookie': cookieDic["other"],
    # 'X-AjaxPro-Method': 'submitChoose',
    'X-AjaxPro-Method': 'submitBespeak',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def feedback(result):
    params = {
        "text": result,
    }
    requests.get(url="https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send",
                 params=params)


def subscribe(seatNum):
    seatNum = str(seatNum)
    result = requests.post(SEAT, headers=HEADERS, json={"seatNum": seatNum})  # 读取座位信息/六楼走廊
    return result


def getCookie():
    return HEADERS["Cookie"]
