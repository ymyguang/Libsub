import time
import CheckSeat
from tools import printLog, feedback

people = {
    '陶雨晴': 1891103126,
    'my': 1990752135
}
keys = list(people.keys())


def Find(name):
    first = None
    second = None
    s = None
    i = 1
    while 1:
        result = CheckSeat.check(people.get(name))
        if result:
            info = str(result[2][0:2])
            if first != result:
                if info == '预约':
                    print(printLog.get_time(),"上次状态(F):{}\n当前状态:{}".format(second, result[0][-5:-1] + "," + result[1][0:4] + "," + result[2]))
                    print(printLog.get_time(), name, "->[已预约]", result)
                    feedback.feedback(str(printLog.get_time())[11:-6] + "," + name + "->[已预约] " + result[0][-5:-1] + "," + result[1][0:4] + "," + result[2], 'M')
                    first = result

                # 插入数据库并作标记：是否是预约开始时间：0|1

            if second != result:
                if info == '选座':
                    print(printLog.get_time(),"上次状态(S):{}\n当前result:{}".format(second, result[0][-5:-1] + "," + result[1][0:4] + "," + result[2]))
                    print(printLog.get_time(), name, "->[已进馆]", result)
                    feedback.feedback(str(printLog.get_time())[11:-6] + "," + name + "->[已进馆] " + result[0][-5:-1] + "," + result[1][0:4] + "," + result[2], 'M')
                    second = result
                # 插入数据库并作标记：是否是进馆开始时间：0|1
            i += 1
            if i % 100 == 0:
                print(printLog.get_time(), name + "->" + str(result))
            # 插入数据库
        else:
            i += 1
            if i % 100 == 0 or s is None:
                print(printLog.get_time(), "未在图书馆")
            s = 1
            if first is not None or second is not None:
                print(printLog.get_time() + ":已离开图书馆")
                feedback.feedback(printLog.get_time() + name + "->[已离开]图书馆", "M")
                # 此时插入数据库并作标记：是否是离开图书馆时间：0|1
                first = None
                second = None
        time.sleep(5)


if __name__ == '__main__':
    # diy()
    Find('陶雨晴')
