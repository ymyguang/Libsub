from tools import printLog
import requests


def feedback(text, case='M'):
    print(printLog.get_time(), "@@@@@@@@@@@@@@@@@COME IN FEEDBACK@@@@@@@@@@@@@@@@@@@@")
    print(printLog.get_time(), "feedback message ---> 【", text + ' 】')
    return
    URL = "https://sctapi.ftqq.com/SCT33679Td3sATvBjES3VjKQeZgcsbxeB.send"

    if case == 'M':
        params1 = {
            "msg": text,
            "qq": 2096304869,
        }
        requests.get("https://qmsg.zendee.cn/send/d105a92ecd34dab1427db4dc4936e339", params=params1)

        # params = {
        #     "title": text,
        # }
        # requests.get(url=URL, params=params)

    elif case == 'G':
        params1 = {
            "msg": text,
            "qq": 708227196,
        }
    requests.get("https://qmsg.zendee.cn/group/d105a92ecd34dab1427db4dc4936e339", params=params1)