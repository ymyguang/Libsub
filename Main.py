import random
import sys
import time
from datetime import datetime

from Cancel import BespeakCancel_nomal
from Find import search
from Sub import sub
from tools import printLog, getInfo
from tools import feedback
from tools import clearScreen
import CheckSeat

F = None
oldTime = 0
i_refresh = 0
name = 'zhou'
# 到馆时间
refresh_time = random.randrange(40, 45)

# 查找走廊可用位置
def findSeat(place):
    print(printLog.get_time(), "正在搜索")
    global F
    F = None
    seatNum = -1
    i = 1
    while seatNum == -1:
        if getInfo.getSeatNum(name):  # 当前有位置
            print(printLog.get_time("findSeat", name), "当前有位置,将退出座位寻找!")
            return
        seatNum = search.search(place)
        # print(printLog.get_time("findSeat", name), "当前循环次数：", i)
        i += 1
        if seatNum == -1:
            time.sleep(5)
    # print(printLog.get_time("findSeat", name), "找到位置可用位置!->座位代码:", seatNum)
    return seatNum


# 刷新预约时间
# 方式:取消后等待130分钟返回,进入下一次维持循环，默认执行取消
def refresh(seatNum, status=1):
    global F
    global name
    global i_refresh
    global oldTime
    # 短时间内预约失败，通知手机端，并结束程序
    i_refresh += 1
    newTime = time.time()
    # print(printLog.get_time("refresh", name), "进入到预约功能", "当前捕获座位号：", seatNum)
    newTime_str = time.strftime("%H:%M:%S", time.localtime(newTime))
    oldTime_str = time.strftime("%H:%M:%S", time.localtime(oldTime))
    if oldTime == 0:
        oldTime_str = "暂无"
    print(printLog.get_time('refresh', name),
          "当前尝试预约次数:{}, 上次预约时间：[{}]，当前时间：[{}]，时间差：{}秒".format(i_refresh, oldTime_str, newTime_str,
                                                              int(newTime - oldTime)))
    if newTime - oldTime < 128 and i_refresh > 128:
        feedback.feedback("预约异常，请手动查看 --" + name)
        exit()
    elif newTime - oldTime > 128 and oldTime != 0:
        print(printLog.get_time('refresh', name), "标记位已置零")
        i_refresh = 0

    now = datetime.now()
    hour = int(now.strftime("%H"))

    # 在有效时间内，取消位置，否者直接跳过
    # 在每天晚上的预约中，由于并发量较大，导致取消时，直接就卡死；同时在闭关期间，不需要一直取消；
    # 8:00 - 21:59 执行取消操作
    if 8 <= hour <= 21:
        print(printLog.get_time(), "取消功能位置生效","执行取消操作")
        flag = None
        if getInfo.getSeatNum(name):
            flag = 1
        cancelRes = str(BespeakCancel_nomal.BespeakCancel(name))
        print(printLog.get_time('refresh', name), "取消结果:", str(cancelRes))
        if flag and cancelRes.find("成功") == -1:
            feedback.feedback(seatNum + "取消失败，请手动查看 --" + name)
            return

    print(printLog.get_time("refresh", name), "正在尝试预约目标位置：", seatNum)

    print(printLog.get_time("refresh", name), "预约信息:", sub.subscribe(seatNum, name).text.split(";")[0])

    # 获取学号信息，并通知手机一次
    if F is None:
        if getInfo.getSeatNum(name):
            studentNUm = getInfo.getUserInfo(name)
            location = str(CheckSeat.check(studentNUm))
            feedback.feedback("已找到位置:" + location + "--" + name)
            # print(printLog.get_time('refresh'), "已找到位置,位置:" + location)
            F = 111

    oldTime = time.time()
    time.sleep(2)
    # 延迟刷新
    if getInfo.getSeatText(name=name):
        # pass
        for i in range(0, refresh_time):
            if i % 30 == 0:
                print(printLog.get_time('refresh', name), '还剩{}分钟后刷新'.format(refresh_time - i))
            time.sleep(60)
    print("------------------------------------------------")


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
    global name

    cancel = BespeakCancel_nomal.BespeakCancel(name)
    while cancel == """操作失败!""":
        print(printLog.get_time(), cancel, "5分钟后将再次尝试取消")
        time.sleep(60 * 5)
        cancel = BespeakCancel_nomal.BespeakCancel(name)
    print(printLog.get_time(), "\033[1;40;42m{}\033[0m".format(cancel))


# 寻找走廊
# st -> status参数，只来源于主函数的信息状态
def corridor(st):
    global name
    flag = True
    while 1:
        if flag:  # 第一次直接采用来自main函数的位置查询信息，减少请求次数
            print(printLog.get_time("corridor", name), st)
            flag = False
            if st:  # 位置不为空
                CheckSeatNum = st[0]
            else:  # 位置为空
                CheckSeatNum = st

        else:
            CheckSeatNum = getInfo.getSeatText(name=name)

        if CheckSeatNum and isOk(CheckSeatNum[:-3]):  # 有位置，且在走廊，保持当前状态
            refresh(CheckSeatNum)  # 默认执行取消
            continue
        elif CheckSeatNum:  # 有位置，但是未在走廊，取消当前位置，重新预约
            Cancel()  # 保证取消成功
        refresh(findSeat(1))


def room():
    global name

    seatNum = getInfo.getSeatText(name=name)
    if seatNum:  # 有位置，但是未在走廊，取消当前位置，重新预约
        Cancel()  # 保证取消成功
    refresh(findSeat(2))  # 未找到位置
    maintain(case=3, num=None)


def all():
    global name

    seatNum = getInfo.getSeatText(name=name)
    if seatNum:  # 有位置，但是未在走廊，取消当前位置，重新预约
        Cancel()  # 保证取消成功
    refresh(findSeat(3))  # 未找到位置
    maintain(case=3, num=None)


def maintain(case, num):
    global name

    global seatNum
    while 1:
        # 指定座位代码
        if case == 2:
            seatNum = num
        # 维持当前座位
        elif case == 3:
            seatNum = getInfo.getSeatText(name=name)
        refresh(seatNum)


def menu(a):
    print("->Now User:", name)
    print("->Now student Card is ", getInfo.getUserInfo(name))
    currentSeat = getInfo.getSeatNum(name)
    if a == "auto":
        print(printLog, "进入自动寻找模式")
        time.sleep(50)
        refresh(findSeat(1), False)  # 直接进入寻找位置，跳过取消
        corridor(getInfo.getSeatNum(name))
    print("You current seat information：", currentSeat)

    option_row = input("Please select state:  \n"
                       "    1.Find seat to bespeak. \n"
                       "    2.Appoint seat number to bespeak.\n"
                       "    3.Maintain current seat.\n"
                       "    4.Cancel current seat\n")
    option = int(option_row)
    if option == 1:
        clearScreen.screen_clear()
        num = input("1 -> corridor; 2 -> room; 3 -> above all\n")
        if int(num) == 1:
            corridor(currentSeat)
        elif int(num) == 2:
            room()
        elif int(num) == 3:
            all()
    elif option == 2:
        clearScreen.screen_clear()
        appointUI()
    elif option == 3:
        clearScreen.screen_clear()
        maintain(case=3, num=000)
    elif option == 4:
        global bl
        cancelResult = BespeakCancel_nomal.BespeakCancel(name)
        print(printLog.get_time(name=name), cancelResult)
        if str(cancelResult).find("成功") == -1 and getInfo.getSeatNum(name):
            bl = input("Whether to forcibly cancel current seat?(yes/no)")
            if bl == "yes" or bl == 'y':
                print(printLog.get_time(name=name), "正在进行强制取消，请耐心等待")
                for i in range(0, 10):
                    time.sleep(60)
                    print(printLog.get_time(name=name), BespeakCancel_nomal.BespeakCancel(name))


def appointUI():
    global name
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
    # 预处理文件
    in_cookie = input(printLog.get_time() + "当前Cookie默认值为:[{}],是否更换？（y/n）".format(name))
    if in_cookie == 'y':
        name = input("The current cookie is {my,yang,gao}")
    menu(a)
