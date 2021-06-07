import time
from Cancel import BespeakCancel_nomal
from Find import search
from Sub import sub
import printLog
import getInfo
import requests


# 查找走廊可用位置
def findSeat():
    seatNum = -1
    i = 1
    while seatNum == -1:
        if getInfo.getSeatNum():  # 当前有位置
            return
        seatNum = search.search()
        print(printLog.get_time(), "当前循环次数：", i)
        i += 1
        if seatNum == -1:
            time.sleep(5)
    print(printLog.get_time(), "座位代码:", seatNum)
    feedback()
    return seatNum


def feedback():
    params1 = {
        "msg": "有位置，请检查",
        "qq": 2096304869,
    }
    requests.get("https://qmsg.zendee.cn/send/d105a92ecd34dab1427db4dc4936e339", params=params1)


# 刷新预约时间
def refresh(seatNum):
    print(printLog.get_time(), "取消结果：", BespeakCancel_nomal.BespeakCancel())
    sub.subscribe(seatNum)
    # 循环等待10分钟，避免取消失败
    if getInfo.getSeatText():
        start = time.time()
        for i in range(0, 15):
            now = time.time()  # 当前时间
            print(printLog.get_time(), "到馆时间将于{}分钟后刷新".format(11 - i))
            if now - start >= 60 * 10.1:  # 若开始时间距离现在时间大于10分钟后，取消循环等待，直接退出，进行下一次预约操作
                break
            else:
                time.sleep(60)


# 是否在走廊
def isOk(floor):
    arr = ["101005", "101008", "101011", "101014"]
    if arr.count(floor):
        print(printLog.get_time(), "\033[1;40;42m已在走廊，将进行循环预约，进行占用\033[0m")
        return True
    else:
        print(printLog.get_time(), "\033[1;40;41m未在走廊，将取消当前座位重新寻找。\033[0m")
        return False


# 可靠取消
def Cancel():
    cancel = BespeakCancel_nomal.BespeakCancel()
    while cancel == """操作失败！""":
        print(printLog.get_time(), cancel, "5分钟后将再次尝试取消")
        time.sleep(60 * 5)
        cancel = BespeakCancel_nomal.BespeakCancel()
    print(printLog.get_time(), "\033[1;40;42m{}\033[0m".format(cancel))


# 寻找走廊
def corridor():
    while 1:
        seatNum = getInfo.getSeatText()
        if seatNum and isOk(seatNum[:-3]):  # 有位置，且在走廊，保持当前状态
            refresh(seatNum)
            continue
        elif seatNum:  # 有位置，但是未在走廊，取消当前位置，重新预约
            Cancel()  # 保证取消成功
        refresh(findSeat())  # 未找到位置


def maintain():
    while 1:
        seatNum = getInfo.getSeatText()
        refresh(seatNum)


def main():
    currentSeat = getInfo.getSeatNum()
    print("You current seat information：", currentSeat)

    if currentSeat:  # 有座位
        option_row = input("Please select state  \n1.corridor \n2.maintain(You must have seat yet)\n")
        option = int(option_row)
        if option == 1:
            corridor()
        elif option == 2:
            maintain()
    else:  # 没有座位
        corridor()


if __name__ == '__main__':
    corridor()
