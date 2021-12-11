from tools import printLog
import requests


def push_QQ(text, case):
    # -1是请求异常
    # false是推送异常
    print("-- 进入QmsgPUSH --")

    qq = {
        'M': 2096304869,
        "G": 1042333099
        # 以下是宿舍
        # "G": 708227196
    }
    way = {
        "M": "send",
        "G": "group"
    }
    params1 = {
        "msg": text,
        "qq": qq[case],
    }
    url = "https://qmsg.zendee.cn/" + way[case] + "/d105a92ecd34dab1427db4dc4936e339"

    try:
        c = requests.get(url=url, params=params1)
        status = c.json()['success']
        print(status)
        return status, c.text
    except Exception as e:
        print(e)
        return -1, e


# coolPush
def weChatPush(text, e):
    print("-- 进入WeCharPUSH --")
    text = "QQ推送失败\n" + "异常信息：" + str(e) + "\n" + text
    text = str(text)
    try:
        t = requests.post("https://push.xuthus.cc/ww/ce4e2dfe9a211ca36f718441f089a88c", data=text.encode("utf-8"))
        status = t.json()['message']
        print(status)
        return status, t.text
    except Exception as e:
        print(e)
        return -1, e


# ServicePush
def weCharPushS(text, e):
    params = {
        "title": text + "\n异常信息:" + e,
    }
    s = requests.get(url="https://sctapi.ftqq.com/SCT33679Td3sATvBjES3VjKQeZgcsbxeB.send", params=params)
    print(printLog.get_time('feedback'), s.text)


def feedback(text, case='M'):
    print("->【", text + ' 】')
    flag = False
    qq_status, e = push_QQ(text, case)

    # QQ状态检查
    if qq_status == -1:
        print("发送异常")
        flag = True
    elif qq_status is False:
        print("推送失败，进入coolPush推送")
        flag = True
    else:
        print("QQ推送成功")

    # coolPush状态检查
    if flag:
        cool_status, e_coo = weChatPush(text, e)
        if cool_status == -1:
            print("发生异常")
            weCharPushS(text, e_coo)

        elif str(cool_status).find("等待执行") == -1:
            print("coolPush推送失败，")
            weCharPushS(text, e_coo)
        else:
            print("coolPush推送成功")

        # coolPush推送失败
    #     if flag == -1:
    #
    #         # server酱推送
    #         print(printLog.get_time("feedback"), "coolPush推送失败 -> 当前已进入Server酱推送")
    #
    #         # Server酱推送失败
    #         if str(s.json()['message']).find("超过当天的发") != -1:
    #             # 最后推送
    #             print(printLog.get_time("feedback"), "Server酱推送失败，执行最后coolPush推送")
    #             t = requests.post("https://push.xuthus.cc/ww/ce4e2dfe9a211ca36f718441f089a88c",
    #                               data=text.encode("utf-8"))
    #             status = t.json()['message']
    #             print(printLog.get_time("feedback"), "coolPush推送状态（最终状态）:", status)
    #     else:
    #         print(printLog.get_time("feedback"), "coolPush通道推送成功")
    # else:
    #     print("QQ通道推送成功")
