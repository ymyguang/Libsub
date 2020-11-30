import requests
import os
import time
from sub_nomal import subclass

seatlist = []
ROOM = [1010140, 1010050, 1010080, 1010110]  # !
ROOM_s = ["1010140", "1010050", "1010080", "1010110"]

ROOM_NAME = ['六楼走廊', '三楼走廊', '四楼走廊', '五楼走廊']
SITE = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {'Cookie': '', 'X-AjaxPro-Method': 'ShowAllSeats',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
           'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br'}

l = []


def search(i):
    print("正在扫描：" + ROOM_NAME[i] + ":" + str(ROOM[i])[0:6])
    r = requests.post(SITE, headers=HEADERS, json={"StrRoomNoParm": str(ROOM[i])[0:6]})  # 读取座位信息
    tar = r.text[1:-4]
    extra(tar)


def extra(total):  # 本楼层可用的座位号
    tar = total.split("|")  # 提取第一个位置字符串，以：|分割
    for i in tar:
        splitstr = i.split(",")  # 未处理单个座位字符串
        if splitstr[3] == str(0):  # 判断位置是是否为零，是，取座位号，否继续判断
            seat = int(splitstr[6][-3:])
            if 46 <= seat <= 77 or 1 <= seat <= 38:
                l.append(str(splitstr[-1:][0]))  # 座位号


# 返回可用作为

def feedback(step):
    params = {
        "msg": step,
        "qq": 971209322
    }
    requests.get("https://qmsg.zendee.cn/group/d105a92ecd34dab1427db4dc4936e339", params=params)


i = 0
while 1:
    os.system("cls")
    l = []
    search(i)
    str1 = ""
    if len(l) != 0:  # 找到可用位置
        for beankseat in l:
            str1 = str1 + "走廊空座:" + ROOM_NAME[ROOM_s.index(str(beankseat)[0:7])] + str(beankseat)[-2:] + "号\n"
        feedback(str1 + "-------------------------------------")
    i = (i + 1) % 4
    time.sleep(3)
