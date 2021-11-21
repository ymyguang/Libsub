from tools import printLog
import requests

qq = {
    'M': 2096304869,
    "G": 708227196
}

way = {
    "M": "send",
    "G": "group"
}


def feedback(text, case='M'):
    text = str(text)
    print(printLog.get_time("Feedback"), "->【", text + ' 】')
    # return
    params1 = {
        "msg": text,
        "qq": qq[case],
    }

    # QQ推送
    url = "https://qmsg.zendee.cn/" + way[case] + "/d105a92ecd34dab1427db4dc4936e339"
    c = requests.get(url=url, params=params1)
    # print(printLog.get_time("feedback"), "推送目标QQ:{}".format(str(qq[case])))
    status = c.json()['success']
    # print(printLog.get_time("feedback"), "QQ推送状态：{},详情：{}".format(c.json()['success'], c.json()['reason']))
    print(status)

    # QQ推送失败
    if status is False:
        # coolPush推送
        print(printLog.get_time("feedback"), "QQ推送失败，进入coolPush推送")
        t = requests.post("https://push.xuthus.cc/ww/ce4e2dfe9a211ca36f718441f089a88c", data=text.encode("utf-8"))
        status = t.json()['message']
        flag = str(status).find("等待执行")

        # coolPush推送失败
        if flag == -1:

            # server酱推送
            print(printLog.get_time("feedback"), "coolPush推送失败 -> 当前已进入Server酱推送")
            params = {
                "title": text,
            }
            s = requests.get(url="https://sctapi.ftqq.com/SCT33679Td3sATvBjES3VjKQeZgcsbxeB.send", params=params)
            print(printLog.get_time('feedback'), s.json()['message'])

            # Server酱推送失败
            if str(s.json()['message']).find("超过当天的发") != -1:
                # 最后推送
                print(printLog.get_time("feedback"), "Server酱推送失败，执行最后coolPush推送")
                t = requests.post("https://push.xuthus.cc/ww/ce4e2dfe9a211ca36f718441f089a88c",
                                  data=text.encode("utf-8"))
                status = t.json()['message']
                print(printLog.get_time("feedback"), "coolPush推送状态（最终状态）:", status)
        else:
            print(printLog.get_time("feedback"), "coolPush通道推送成功")
    else:
        print("QQ通道推送成功")
