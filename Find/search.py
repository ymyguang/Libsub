# 查找带有电源的走廊位置
import requests
import random
import Main

ROOM = [1010050, 1010080, 1010110, 1010140]  # !1010140是走廊
ROOM_NAME = ['三楼走廊', '四楼走廊', '五楼走廊', '六楼走廊']
SITE = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {'Cookie': '', 'X-AjaxPro-Method': 'ShowAllSeats',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
           'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br'}


def seatInfo(seatNumber):
    r = requests.post(SITE, headers=HEADERS, json={"StrRoomNoParm": str(seatNumber)})  # 读取座位信息
    return r.text[1:-4]


# 返回座位号，若无效则值为-1
def search():
    global seatNum
    for i in range(0, 4):
        print("[INFO]正在扫描:" + ROOM_NAME[i] + ":" + str(ROOM[i])[0:6])
        num = str(ROOM[i])[0:-1]
        tar = seatInfo(num)
        seatNumArray = extra(tar, 1)  # 当前楼层的可用位置,0全部位置，1位走廊位置
        if seatNumArray != -1:
            seatNum = seatNumArray[random.randrange(0, len(seatNumArray))]
            break
        else:
            seatNum = -1
    return seatNum


# 本楼层可用的座位号
def extra(total, corridor=0):
    l = []
    tar = total.split("|")  # 提取第一个位置字符串，以：|分割
    for i in tar:
        splitstr = i.split(",")  # 未处理单个座位字符串
        if len(splitstr) < 4:
            return -1
        if splitstr[3] == str(0):  # 判断位置是是否为零，是，取座位号，否继续判断
            if corridor:
                seat = int(splitstr[6][-3:])
                if 46 <= seat <= 77 or 1 <= seat <= 38:
                    l.append(str(splitstr[-1:][0]))  # 座位号
            else:
                l.append(str(splitstr[-1:][0]))  # 座位号
    if l:
        return l
    else:
        return -1
