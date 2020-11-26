import requests

URL = "https://sc.ftqq.com/SCU130108Ta4c5f2a9e57c45b7f7224242b46ae1585fbfa4b860f6c.send"
HEADERS = {
    'Cookie': 'Reader_barcode=WechatTSG=A3B25858882C96748B640873190B1D4F&WeChatUserCenter=1990752134; UserIdentID=WechatTSG=A3B25858882C96748B640873190B1D4F&WeChatUserCenter=1990752134; UserOpenID=WechatTSG=1008220201108173938977205291; UserName=WechatTSG=%e6%9d%8e%e6%a8%8a; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e6%9d%8e%e6%a8%8a;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}

def BespeakCancel():
    site = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"
    return requests.get(site, headers=HEADERS).text  # 取消座位

def feedback(result):
    params = {
        "text": result[1:]
    }
    requests.get(url=URL, params=params)


def main():
    i = 100
    while i > 0:
        i -= 2
        feedback(BespeakCancel() + str(i))
