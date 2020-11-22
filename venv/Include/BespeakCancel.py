import requests


class BespeakCancel(object):
    def der(self, p):
        site = "http://tsgic.hebust.edu.cn/seat/BespeakCancel.aspx"
        requests.get(site, headers=p.headers)  # 取消座位
        print("取消成功")
