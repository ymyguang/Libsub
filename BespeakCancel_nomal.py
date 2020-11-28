import requests
import datetime
import re

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
HEADERS = {
    'Cookie': 'Reader_barcode=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserIdentID=WechatTSG=A3B25858882C967416B2B919872B99AC&WeChatUserCenter=1990752170; UserOpenID=WechatTSG=1008220201127223551561013081; UserName=WechatTSG=%e7%a9%86%e4%bf%8a%e5%87%af; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e7%a9%86%e4%bf%8a%e5%87%af; ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def BespeakCancel():
    site = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"
    return re.findall(r"title:\"(.+?)\"", requests.get(site, headers=HEADERS).text)[0]


def feedback(result):
    params = {
        "text": result
    }
    requests.get(url=URL, params=params)


feedback(BespeakCancel())
