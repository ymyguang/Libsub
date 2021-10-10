import requests
import re
from Sub import sub
from Sub import sub

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
SITE = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"


def BespeakCancel(name):
    result = re.findall(r"title:\"(.+?)\"", requests.get(SITE, headers=sub.getHeader(name)).text)[0]
    cause = re.findall(r"text:\"(.+?)\"", requests.get(SITE, headers=sub.getHeader(name)).text)[0]
    if str(result).find("成功") != -1:
        return result
    else:
        return result + "错误原因:" + cause
