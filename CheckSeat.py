import requests
from bs4 import BeautifulSoup
from Sub import sub
from tools import printLog

SITE = "http://tsgic.hebust.edu.cn/seat/FriendSeats/friendSeat.aspx?"
def check(number):
    payload = {'friend_cardid': number}
    print(number)
    r = requests.get(SITE, headers=sub.HEADERS, params=payload)  # 读取座位信息
    if r.status_code == 200:
        print(printLog.get_time(), "学号:", number)
        supe = BeautifulSoup(r.text, "html.parser")
        l = []
        for i in supe.find_all("input"):
            l.append(i.get("value"))
        print(printLog.get_time(), "当前位置：", l[-3:], end="=>")
        return 1

# 1990600101, 1991451099
num = 0
for i in range(1990752170, 1990752171):
    number = i
    if check(number):
        num += 1
        print("第{}位".format(num))
print("扫描完成")
