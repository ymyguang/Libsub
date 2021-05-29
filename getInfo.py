# 展示使用
import printLog
import Cancel.BespeakCancel_nomal
import requests
from bs4 import BeautifulSoup

SITE = "http://tsgic.hebust.edu.cn/seat/MyCurBespeakSeat.aspx"


# floorDict = {
#     "二层南区": "101001",
#     "二层北区": "101002",
#     "三层南区": "101003",
#     "三层北区": "101004",
#     "三层走廊": "101005",
#     "四层南区": "101006",
#     "四层北区": "101007",
#     "四层走廊": "101008",
#     "五层南区": "101009",
#     "五层北区": "101010",
#     "五层走廊": "101011",
#     "六层南区": "101012",
#     "六层北区": "101013",
#     "六层走廊": "101014"
# }


# myInfo[0]全座位号，[1]文字座位信息
def getSeatNum():
    Headers = Cancel.BespeakCancel_nomal.HEADERS
    myInfo = []
    requset = requests.post(SITE, headers=Headers)
    supe = BeautifulSoup(requset.text, "html.parser")
    num = 0

    for i in supe.find_all("input"):
        num += 1
        if num == 7 or num == 9:
            value = i.get("value")
            # 是否有位置，若有则加入，若无则返回假
            if value:
                myInfo.append(value)
            else:
                return False
    return myInfo


# 若有位置，则返回位置代码，若无位置则返回假
def getSeatText(i=1):
    seat = getSeatNum()
    if seat:
        if i:
            print(printLog.get_time(), "\033[1;40;46m已检测到预约信息；当前位置信息：[{}] [{}]号\033[0m".format(seat[1], seat[0][-3:]))
        return seat[0]  # 位置代码
    else:
        if i:
            print(printLog.get_time(), "\033[1;40;41m未检测到预约信息\033[0m")
        return False


