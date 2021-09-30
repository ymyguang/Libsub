import os
import sys
import time
from Cancel import BespeakCancel_nomal
from Find import search
from Sub import sub
from tools import printLog
import getInfo
import requests
from tools import clearScreen
import CheckSeat

F = None
# 查找走廊可用位置
def findSeat(place):
    seatNum = -1
    i = 1
    while seatNum == -1:
        if getInfo.getSeatNum():  # 当前有位置
            print(printLog.get_time(), "当前有位置,将退出座位寻找!")
            return
        seatNum = search.search(place)
        print(printLog.get_time(), "当前循环次数：", i)
        i += 1
        if seatNum == -1:
            time.sleep(5)
    print(printLog.get_time(), "找到位置可用位置!->座位代码:", seatNum)
    return seatNum


def feedback(text, case='M'):
    print(printLog.get_time(), "@@@@@@@@@@@@@@@@@COME IN FEEDBACK@@@@@@@@@@@@@@@@@@@@")
    URL = "https://sctapi.ftqq.com/SCT33679Td3sATvBjES3VjKQeZgcsbxeB.send"

    if case == 'M':
        params1 = {
            "msg": text,
            "qq": 2096304869,
        }
        requests.get("https://qmsg.zendee.cn/send/d105a92ecd34dab1427db4dc4936e339", params=params1)

        # params = {
        #     "title": text,
        # }
        # requests.get(url=URL, params=params)

    elif case == 'G':
        params1 = {
            "msg": text,
            "qq": 708227196,
        }
    requests.get("https://qmsg.zendee.cn/group/d105a92ecd34dab1427db4dc4936e339", params=params1)


# 刷新预约时间
# 方式:取消后等待10分钟返回,进入下一次维持循环
def refresh(seatNum):
    global F
    print(printLog.get_time(), "取消结果:", str(BespeakCancel_nomal.BespeakCancel()))
    sub.subscribe(seatNum)
    if F is None:
        if getInfo.getSeatNum():
            index = sub.getCookie().find("WeChatUserCenter=") + len("WeChatUserCenter") + 1
            studentNUm = sub.getCookie()[index:index + 10]
            location = str(CheckSeat.check(studentNUm))
            feedback("已找到位置,位置:" + location)
            print(printLog.get_time(), "已找到位置,位置:" + location)
            F = 111

    t = str(seatNum) + "\n"
    if os.path.isfile('info.txt') is False:
        os.system("type nul > info.txt")
    file = open('info.txt', 'r+')
    lines = file.readlines()
    print(printLog.get_time(), "**************当前日志文件大小：", len(lines), "**************")
    if len(lines) > 300:
        file.close()
        os.system("del info.txt")
        print(printLog.get_time(), '**************删除文件', "**************")
        os.system("type nul > info.txt")
        file = open('info.txt', 'r+')
        lines = []
    if len(lines) != 0:
        if lines[-1] == str(t):
            print(printLog.get_time(), "重复命中")
        else:
            file.write(t)
    else:
        file.write(t)
    file.close()

    if getInfo.getSeatText():
        time.sleep(10)
        # start = time.time()
        # for i in range(0, 120):
        #     now = time.time()  # 当前时间
        #     print(printLog.get_time(), "到馆时间将于{}分钟后刷新".format(120 - i))
        #     if now - start >= 120 * 30.1:  # 若开始时间距离现在时间大于10分钟后，取消循环等待，直接退出，进行下一次预约操作
        #         break
        #     else:
        #         time.sleep(60)


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
    while cancel == """操作失败!""":
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
        refresh(findSeat(1))  # 未找到位置


def room():
    seatNum = getInfo.getSeatText()
    if seatNum:  # 有位置，但是未在走廊，取消当前位置，重新预约
        Cancel()  # 保证取消成功
    refresh(findSeat(2))  # 未找到位置
    maintain(case=3, num=None)


def maintain(case, num):
    global seatNum
    while 1:
        # 指定座位代码
        if case == 2:
            seatNum = num
        # 维持当前座位
        elif case == 3:
            seatNum = getInfo.getSeatText()
        refresh(seatNum)


def menu(a):
    currentSeat = getInfo.getSeatNum()
    if a == "auto":
        print(printLog, "进入自动寻找模式")
        corridor()
    print("You current seat information：", currentSeat)
    option_row = input("Please select state:  \n"
                       "    1.Find seat to bespeak. \n"
                       "    2.Appoint seat number to bespeak.\n"
                       "    3.Maintain current seat.\n"
                       "    4.Cancel current seat\n")
    option = int(option_row)
    if option == 1:
        clearScreen.screen_clear()
        num = input("1 -> corridor; 2 -> room\n")
        if int(num) == 1:
            corridor()
        else:
            room()
    elif option == 2:
        clearScreen.screen_clear()
        appointUI()
    elif option == 3:
        clearScreen.screen_clear()
        maintain(case=3, num=000)
    elif option == 4:
        global bl
        cancelResult = BespeakCancel_nomal.BespeakCancel()
        print(printLog.get_time(), cancelResult)
        if str(cancelResult).find("成功") == -1 and getInfo.getSeatNum():
            bl = input("Whether to forcibly cancel current seat?(yes/no)")
            if bl == "yes" or bl == 'y':
                print(printLog.get_time(), "正在进行强制取消，请耐心等待")
                for i in range(0, 10):
                    time.sleep(60)
                    print(printLog.get_time(), BespeakCancel_nomal.BespeakCancel())


def appointUI():
    global isCorridor
    # 默认不在走廊
    isCorridor = 0
    num = (input(""" 
    ###########     FLOOR MAP     ############
    ******      二楼南区1  二楼北区2     *******
    *****   三楼南区3  三楼北区4  三楼走廊5  *****
    *****   四楼南区6  四楼北区7  四楼走廊8  *****
    *****   五楼南区9  五楼北区10 五楼走廊11 *****
    *****   六楼南区12 六楼北区13 六楼走廊14 *****
    ##########################################
    """
                 "\nPlease input seat number(The number consist of floor and site):\n"))
    num = "1010" + "0" * (2 - len(num)) + num
    if num[-2:] in ["05", "08", "11", "14"]:
        print("Hit the corridor")
        isCorridor = 1
    validSeat = search.extra(search.seatInfo(num), isCorridor)
    sortValidSeat = sorted(validSeat)
    print("可用座位号:")
    cnt = 0
    for seat in sortValidSeat:
        cnt += 1
        if cnt % 8 == 0:
            last = "号\n"
        else:
            last = "号, "
        print(seat[-3:], end=last)
    subnum = input("\nSELECT SEAT NUMBER\n")
    num = num + "0" * (3 - len(subnum)) + subnum
    print("选中作为号:", num)
    maintain(case=2, num=num)


if __name__ == '__main__':
    a = sys.argv[-1]
    menu(a)
    # print(findSeat(2))
