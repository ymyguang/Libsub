import os
import time

import requests
from bs4 import BeautifulSoup
from Sub import sub

SITE = "http://tsgic.hebust.edu.cn/seat/FriendSeats/friendSeat.aspx?"

HEADERS = {
    'Cookie': 'ASP.NET_SessionId=ssehadfrepre1di1ye3tds0r; UserIdentID=WechatTSG=52DCB27540694334876C71FF278DEEA3&WeChatUserCenter=1790752063; Reader_barcode=WechatTSG=52DCB27540694334876C71FF278DEEA3&WeChatUserCenter=1790752063; UserOpenID=WechatTSG=1008220200901163028331442051; UserName=WechatTSG=%e5%91%a8%e8%89%af%e6%b5%a9; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e5%91%a8%e8%89%af%e6%b5%a9; ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def state(number):
    payload = {'friend_cardid': number}
    try:
        r = requests.get(SITE, headers=sub.HEADERS, params=payload)  # 读取座位信息
    except Exception as e:
        print(e)
    if r.status_code == 200:
        supe = BeautifulSoup(r.text, "html.parser")
        l = []
        for i in supe.find_all("input"):
            l.append(i.get("value"))
        return l[-3:]


# 判
def isExist(fileName):
    print("[INFO]正在判断文件是否存在")
    if os.path.exists(fileName):
        return True
    else:
        return False


# 查
def isEmpty(fileNme):
    print("[INFO]正在判断文件是否为空")
    stats = os.stat(fileNme)
    return not stats.st_size


# 读
def show(fileName):
    file = None
    try:
        file = open(fileName, encoding='utf-8')
        print("[INFO]number.txt文件中前三行的内容为：")
        lines = file.readlines()
        count = 1
        for i in lines:
            if count <= 3 and i is not None:
                count += 1
                print("    ", i.replace("\n", ""))
            else:
                break
    except():
        print("读取文件失败,请联系开发者")
    finally:
        file.close()


# 写
def writeContent(fileName, method):
    file = None
    try:
        file = open(fileName, method, encoding="utf-8")
        file.write("""1990752132,康兴旺\n1990752133,李 晨\n1990752134,李 樊\n1990752135,刘 彪\n1990752136,刘明一\n1990751026,刘奕君""")
    except():
        print("写入失败")
    finally:
        file.close()


# 展
def init():
    file = 'number.txt'
    if isExist(file):
        time.sleep(2)
        print("[INFO]>>文件存在")
        if isEmpty(file):
            time.sleep(2)
            print("[INFO]>>文件为空")
            writeContent(file, "w")
        else:
            time.sleep(2)
            print("[INFO]>>文件不为空")
    else:
        time.sleep(2)
        print("[INFO]>>文件不存在,正在创建文件")
        time.sleep(2)
        print("[INFO]>>正在写入测试样例")
        writeContent(file, "x")
    time.sleep(2)
    show(file)
    time.sleep(2)
    print("[INFO]即将开始探测\n"
          "---------——————-【查   询   结   果】---------------")


def check():
    num = 0
    file = open('number.txt', encoding="utf-8")
    lines = file.readlines()

    for i in lines:
        if ',' in i:
            devi = i.split(',')
        elif '，' in i:
            devi = i.split('，')
        number = devi[0]
        result = state(number)
        if result:
            num += 1
            strr = "第{}位:[{}] -> {}".format(("0" * (2 - len(str(num))) + str(num)),
                                            devi[1].replace("\n", ""), result)
            print(strr)
    file.close()
    if not num:
        print("[INFO]本次查询未找到任何内容，即（number.txt文件中的人员均未在图书馆！）")
    print('--------------------------------------------------')
    print("[INFO]扫描完成")



if __name__ == '__main__':
    print("【使用说明】:程序会自动读取当前目录文件下的：num"
          "ber.txt的文件，若不存在将会自动创建(包含测试样例)\n"
          "因此您需要将待查询的信息填写到当本目录下的number.txt文件\n"
          "【格式】学号,姓名\n【例如】1990752135,刘彪（学号L改为9，分隔符为英文逗号）\n"
          "--------------------------------------------------------------")
    input("按任意键继续")
    init()
    check()
    input()
    input()
    input()
