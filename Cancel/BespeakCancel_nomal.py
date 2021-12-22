import requests
import sys
import re
from tools import feedback
sys.path.append('/root/Libsub/')
from Sub import sub

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
SITE = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"


def BespeakCancel(name):
    try:
        result = re.findall(r"title:\"(.+?)\"", requests.get(SITE, headers=sub.getHeader(name)).text)[0]
        cause = re.findall(r"text:\"(.+?)\"", requests.get(SITE, headers=sub.getHeader(name)).text)[0]
        if str(result).find("成功") != -1:
            return result
        else:
            return result + "错误原因:" + cause
    except Exception as e:
        print(e, "---BespeakCancel")
        feedback.feedback("BespeakCancel--产生异常"+ str(e))

# 批量取消
if __name__ == '__main__':
    l = ['zhou', 'yang', 'gao']
    for i in l:
        print("当前取消用户：{}".format(i))
        print(BespeakCancel(i))
        print("-------------------------------")
