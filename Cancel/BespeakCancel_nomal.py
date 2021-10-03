import requests
import re
from Sub import sub
from tools import printLog

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
SITE = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"

HEADERS = {
    'Cookie': sub.getCookie(),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def BespeakCancel():
    result = re.findall(r"title:\"(.+?)\"", requests.get(SITE, headers=HEADERS).text)[0]
    cause = re.findall(r"text:\"(.+?)\"", requests.get(SITE, headers=HEADERS).text)[0]
    if str(result).find("成功") != -1:
        return result
    else:
        return result + "错误原因:" + cause
