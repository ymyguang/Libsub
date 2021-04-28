import random
import time
from Cancel import BespeakCancel_nomal
from Find import search
from Sub import sub
import printLog
import getInfo


# 查找走廊可用位置
def findSeat():
    seatNum = -1
    i = 1
    while seatNum == -1:
        seatNum = search.search()
        print(printLog.get_time(), "当前循环次数：", i)
        i += 1
        if seatNum == -1:
            time.sleep(5)
    print(printLog.get_time(), "座位代码:", seatNum)
    return seatNum


# 刷新预约时间
def refresh(seatNum):
    print(printLog.get_time(), BespeakCancel_nomal.BespeakCancel())
    sub.subscribe(seatNum)
    getInfo.getSeatText()
    delay = random.randrange(10, 19)
    # delay = 5
    print(printLog.get_time(), "到馆时间将于{}分钟后刷新".format(delay))
    time.sleep(60 * delay)


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


# 检测位置状态
def main():
    while 1:
        seatNum = getInfo.getSeatText()
        if seatNum and isOk(seatNum[:-3]):
            refresh(seatNum)
            continue
        elif seatNum:
            Cancel()  # 保证取消成功
        refresh(findSeat())


if __name__ == '__main__':
    main()
# findSeat()
# Deprecated Code

# 1 位置有效
# 2 有位置，无效
# 3 无位置

# 查看当前状态,返回返回内容
# def init():
#     # 随机生成一个位置，尽量保证位置可用
#     seatNum = search.search()
#     if seatNum == -1:
#         seatNum = "101012" + str(random.randrange(100, 380))
#     result = sub.subscribe(seatNum)
#     print(printLog.get_time(), "服务器返回消息：", result.text, "come from init()")
#     return result
