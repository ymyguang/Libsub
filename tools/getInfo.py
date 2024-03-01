# 展示使用g=utf-8
#! codin
import time

from tools import printLog
import requests
from bs4 import BeautifulSoup
from Sub import sub
from tools import feedback

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
def getUserInfo(name):
    index = sub.getCookie(name).find("WeChatUserCenter=") + len("WeChatUserCenter") + 1
    studentNUm = sub.getCookie(name)[index:index + 10]
    return studentNUm

def getSeatNum(name):
    Headers = sub.getHeader(name)
    myInfo = []
    r = 0
    # 网络超时情况下重试
    while r < 10:
        try:
            requset = requests.post(SITE, headers=Headers)
            supe = BeautifulSoup(requset.text, "html.parser")
            r = 1000
        except Exception as e:
            print(e)
            r += 1
            time.sleep(60)
            if r == 10:
                feedback.feedback("始终产生异常，程序退出【getSeatNum】")
            else:
                feedback.feedback("getSeatNum-产生异常：" + str(e) + "\n当前正在重试！【getSeatNum】")

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
def getSeatText(i=1, name=None):
    seat = getSeatNum(name)
    if seat:
        if i == -1:
            return "{} [{}]号".format(seat[1], seat[0][-3:])
        elif i:
            print(printLog.get_time('getSeat'),
                  "\033[1;40;46m已检测到预约信息；当前位置信息：[{}] [{}]号\033[0m".format(seat[1], seat[0][-3:]))
        return seat[0]  # 位置代码
    else:
        if i:
            print(printLog.get_time('getSeat'), "\033[1;40;41m未检测到预约信息\033[0m")
        return False
