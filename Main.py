import random
import time
from Cancel import BespeakCancel_nomal
from Find import search
from Sub import sub
import printLog
import getInfo


def isOk(floor):
    arr = ["101005", "101008", "101011", "101014"]
    return arr.count(floor)


# 查看当前状态,返回返回内容
def init():
    # 随机生成一个位置，尽量保证位置可用
    seatNum = "101012" + str(random.randrange(100, 380))
    result = sub.subscribe(seatNum)
    print(printLog.get_time(), "服务器返回消息：", result.text, "come from init()")
    return result


# 查找走廊可用位置
def findSeat():
    seatNum = -1
    i = 1
    while seatNum == -1:
        time.sleep(5)
        seatNum = search.search()
        print(printLog.get_time(),  "当前循环次数：", i)
        i += 1
    print(printLog.get_time(), "座位代码：", seatNum)
    return seatNum  # 座位号，若无，则返回-1


# 预约成功后执行取消+预约 这里就是指定位置了
def run(seatNum):
    while True:
        result = sub.subscribe(seatNum)
        print(printLog.get_time(), result.text)
        getInfo.getSeatText(result.text, result.text[1])
        delay = random.randrange(10, 19)
        print(printLog.get_time(), "{}分钟后，将重新预约座位".format(delay))
        time.sleep(60 * delay)
        BespeakCancel_nomal.BespeakCancel()


def main():
    strResult = init().text  # 返回内容
    stateCode = strResult[1]
    while stateCode == "1":  # 若结果为一，即位置无效，则重新申请
        strResult = init().text
        print(printLog.get_time(), "位置无效，将重新申请")
        stateCode = strResult[1]

    if stateCode == "3" or stateCode == "4":  # 已有位置||预约成功
        seatNum, floor_num = getInfo.getSeatNum(strResult, stateCode)
        if isOk(floor_num):  # 如果满足条件，则一直循环占用
            print(printLog.get_time(), "\033[1;40;42m已在走廊，将进行循环预约，进行占用\033[0m")
            run(seatNum)    # 防止快到预约时间了，仍然延迟10分钟
        else:  # 若不满足，则取消后搜索可用座位  "\033[31m未在走廊，将取消当前座位重新寻找。取消状态：{}\033[0m"
            print(printLog.get_time(), "\033[1;40;41m未在走廊，将取消当前座位重新寻找。\033[0m")
            Cancel()
            availableNum = findSeat()
            run(availableNum)


def Cancel():
    cancel = BespeakCancel_nomal.BespeakCancel()
    while cancel == """操作失败！""":
        print(printLog.get_time(), cancel, "10分钟后将再次尝试取消")
        time.sleep(60 * 10)
        cancel = BespeakCancel_nomal.BespeakCancel()
    print(printLog.get_time(), "\033[1;40;41m{}\033[0m".format(cancel))


if __name__ == '__main__':
    main()
