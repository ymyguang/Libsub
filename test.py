import requests
import time
import random

from datetime import datetime


def get_time():
    now = datetime.now()
    current_time = now.strftime(":【%Y-%m-%d %H:%M:%S】")
    return str(current_time)


# 微信提醒，未填报体温
def feedback():
    params1 = {
        "msg": "The currently time is {}".format(get_time()),
        "qq": 2096304869,
    }
    requests.get("https://qmsg.zendee.cn/send/d105a92ecd34dab1427db4dc4936e339", params=params1)


print(random.randrange(0, 2))
