import time
import CheckSeat
import Main
from tools import printLog

# def diy():
#     for i in range(0, len(keys)):
#         _thread.start_new_thread(Find, (keys[i],))

people = {
    'xjj': 1891103126,
    'my': 1990752135
}
keys = list(people.keys())


def Find(name):
    global first
    global second
    first = None
    second = None
    i = 1
    while 1:
        result = CheckSeat.check(people.get(name))
        if result:
            info = str(result[2][0:2])
            if first != result:
                if info == '预约':
                    print(printLog.get_time(), '【通知手机端】:', people.get(name), "->[已预约]", result)
                    Main.feedback(printLog.get_time() + name + str(people.get(name)) + "->[已预约]" + str(result), 'M')
                    first = result
                # 插入数据库并作标记：是否是预约开始时间：0|1

            if second != result:
                if info == '选座':
                    print(printLog.get_time(), '【通知手机端】:', people.get(name), "->[已进馆]", result)
                    Main.feedback(printLog.get_time() + name + str(people.get(name)) + "->[已进馆]" + str(result), 'M')
                    second = result
                # 插入数据库并作标记：是否是进馆开始时间：0|1
            i += 1
            if i % 200 == 0:
                print(printLog.get_time(), name + "->" + str(result))
            # 插入数据库
        else:
            print(printLog.get_time(), "未在图书馆")
            if first is not None:
                print(printLog.get_time(), '【通知手机端】' + ":已离开图书馆")
                Main.feedback(printLog.get_time() + name + str(people.get(name)) + "->[已离开]图书馆", "M")

                # 此时插入数据库并作标记：是否是离开图书馆时间：0|1
                first = None
                second = None
        time.sleep(10)


if __name__ == '__main__':
    # diy()
    Find('xjj')
