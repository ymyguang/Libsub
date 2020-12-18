import requests
import os
import time
from sub_nomal import subclass

ROOM = [1010050, 1010080, 1010110, 1010140]  # !
ROOM_NAME = ['三楼走廊', '四楼走廊', '五楼走廊', '六楼走廊']
SITE = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {'Cookie': '', 'X-AjaxPro-Method': 'ShowAllSeats',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
           'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br'}


def search():
    for i in range(0, 4):
        print("正在扫描：" + ROOM_NAME[i] + ":" + str(ROOM[i])[0:6])
        r = requests.post(SITE, headers=HEADERS, json={"StrRoomNoParm": str(ROOM[i])[0:6]})  # 读取座位信息
        tar = r.text[1:-4]
        seatNum = if_available(extra(tar))  # 找到最大的座位号
        if seatNum != -1:
            return seatNum
    return seatNum


def if_available(tar):
    if len(tar) != 0:
        return sorted(tar)[-1]
    return -1


def extra(total):  # 本楼层可用的座位号
    l = []
    tar = total.split("|")  # 提取第一个位置字符串，以：|分割
    for i in tar:
        splitstr = i.split(",")    # 未处理单个座位字符串
        if splitstr[3] == str(0):  # 判断位置是是否为零，是，取座位号，否继续判断
            seat = int(splitstr[6][-3:])
            if 46 <= seat <= 77 or 1 <= seat <= 38:
                l.append(str(splitstr[-1:][0]))  # 座位号
    return l  # 返沪找到的结果

# 返回可用作为
p = subclass()
i = 1
isbreak = 0
while 1:
    if isbreak:
        break
    os.system("cls")
    print("第" + str(i) + "次轮询，" + "未找到有效座位，即将进行下一轮轮询")
    i += 1
    p.seatNum = search()  # 获取座位 -1,未找到！
    if p.seatNum != -1:   # 找到可用位置，
        p.sub(i)
        print(p.seatNum)
        isbreak = 1       # 退出轮询
        break
    time.sleep(1)

