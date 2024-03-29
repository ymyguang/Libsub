import time
import _thread
import requests
from bs4 import BeautifulSoup
from Sub import sub
from tools import printLog

SITE = "http://tsgic.hebust.edu.cn/seat/FriendSeats/friendSeat.aspx?"

def check(number):
    payload = {'friend_cardid': number}
    r = requests.post(SITE, headers=sub.getHeader('zhou'), params=payload)  # 读取座位信息
    if r.status_code == 200:
        supe = BeautifulSoup(r.text, "html.parser")
        l = []
        for i in supe.find_all("input"):
            l.append(i.get("value"))
        return l[-3:]


def comment():
    num = 0
    file = open('number.txt', mode='r', encoding='utf-8-sig')
    Lines = file.readlines()
    for i in Lines:
        devi = i.split(',')
        number = devi[0]
        result = check(number)
        if result:
            num += 1
            strr = printLog.get_time("comment") + "第{}位:{} -> {}".format(("0" * (2 - len(str(num))) + str(num)), devi, result)
            print(strr)
            # Main.feedback(strr, case='G')
    print("扫描完成")


people = {
    'wjj': 1891103126,
}
keys = list(people.keys())


def longFind(threadName):
    while 1:
        # print("Thread-" + threadName + ":", end="")
        result = check(people.get(threadName))
        if result:
            # Main.feedback(threadName + "->" + str(result), case=threadName[-1])
            print(threadName + "->" + str(result))
            # exit()
        else:
            print("当前无位置")
        time.sleep(5)


def diy():
    for i in range(0, len(keys)):
        _thread.start_new_thread(longFind, (keys[i],))


def test():
    params1 = {
        "msg": "测试，你好@at=2315143636@，hello",
        "qq": 708227196,

    }
    requests.get("https://qmsg.zendee.cn/group/d105a92ecd34dab1427db4dc4936e339", params=params1)


if __name__ == '__main__':
    # diy()
    comment()
    # test()
    input()
