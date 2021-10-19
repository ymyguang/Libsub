# 查找带有电源的走廊位置
import datetime
import requests
from tools import printLog

SITE = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {'Cookie': '', 'X-AjaxPro-Method': 'ShowAllSeats',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
           'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br'}


def seatInfo(seatNumber):
    r = requests.post(SITE, headers=HEADERS, json={"StrRoomNoParm": str(seatNumber)})  # 读取座位信息
    return r.text[1:-4]


def search(place):
    global seatNum
    CORRIDOR = ['三楼走廊05', '四楼走廊08', '五楼走廊11', '六楼走廊14']  # 五楼走廊11
    Room = ['三楼北区04',
            '三楼南区03', '二楼北区02',
            '四楼南区06', '四楼北区07',
            '五楼南区09', '五楼北区10', '六楼北区13']

    All = ['三楼走廊05', '四楼走廊08', '五楼走廊11', '六楼走廊14', '三楼北区04',
           '三楼南区03', '二楼北区02',
           '四楼南区06', '四楼北区07',
           '五楼南区09', '五楼北区10', '六楼北区13']
    # 1是走廊,2是阅览室
    # 默认是走廊
    targetPlace = CORRIDOR
    if place == 2:
        targetPlace = Room
    elif place == 3:
        targetPlace = All

    for i in targetPlace:
        print(i, end=" ")
        roomNumber = "1010" + i[-2:]
        roomName = i[0:4]
        print("[INFO]正在扫描:" + roomName + ":" + str(roomNumber))
        tar = seatInfo(roomNumber)
        seatNumArray = extra(tar, place)  # 当前楼层的可用位置,0全部位置，1位走廊位置
        if seatNumArray != -1:
            seatNumArray.sort()

            # 1是走廊
            if place == 1:
                hour = datetime.datetime.now().hour
                # 上午预约南区
                if hour >= 22 or hour < 10:
                    index = 0
                else:
                    index = -1
                seatNum = seatNumArray[index]  # 返回最大的值（北区）

            # 2是阅览室
            elif place == 2:
                seatNum = seatNumArray[int(len(seatNumArray) / 2)]  # 中间值

            if roomNumber == "101005" and seatNum[-3:] in ('065', '066', '067'):
                print(printLog.get_time('find'), "扫描位置为{}-{}，该位置无电源，已跳过！".format(roomName, seatNum[-3:]))
                seatNum = -1
            elif roomNumber == "101011" and seatNum[-3:] in ('022', ''):
                print(printLog.get_time('find'), "扫描位置为{}-{}，该位置无电源，已跳过！".format(roomName, seatNum[-3:]))
                seatNum = -1
            # 找到有效位置，退出本轮位置寻找
            else:
                break
        else:
            seatNum = -1
    return seatNum


# 本楼层可用的座位号
def extra(total, place):
    l = []
    tar = total.split("|")  # 提取第一个位置字符串，以：|分割
    for i in tar:
        splitStr = i.split(",")  # 未处理单个座位字符串
        # 无有效座位
        if len(splitStr) < 4:
            return -1
        # 判断位置是是否为零，是，取座位号，否继续判断(0就是没人)
        if splitStr[3] == str(0):
            # 是否符合走廊条件
            if place == 1:
                seat = int(splitStr[6][-3:])
                if 48 <= seat <= 77 or 1 <= seat <= 38:
                    l.append(str(splitStr[-1:][0]))  # 座位号

            # 是否满足阅览室条件
            elif place == 2:
                if splitStr[1] == str(2):
                    l.append(str(splitStr[-1:][0]))  # 座位号

            # 返回所有位置，供Maintain位置使用
            else:
                l.append(str(splitStr[-1:][0]))  # 有效座位号
    if l:
        return l
    else:
        return -1
