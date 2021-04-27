# 展示使用
import printLog

floorDict = {
    "二层南区": "101001",
    "二层北区": "101002",
    "三层南区": "101003",
    "三层北区": "101004",
    "三层走廊": "101005",
    "四层南区": "101006",
    "四层北区": "101007",
    "四层走廊": "101008",
    "五层南区": "101009",
    "五层北区": "101010",
    "五层走廊": "101011",
    "六层南区": "101012",
    "六层北区": "101013",
    "六层走廊": "101014"
}


def getSeatText(strResult, stateCode):
    # 楼层
    global floor_text, seat
    for i in list(floorDict.keys()):
        if i in strResult:
            floor_text = i
    # 座位号
    if stateCode == "3":
        end = strResult.find("]座位")
        seat = strResult[end - 3:end]
    elif stateCode == "4":
        end = strResult.find("号，请")
        seat = strResult[end - 3:end]  # "
    print(printLog.get_time(), "\033[1;40;46m当前位置信息：[{}] [{}]号\033[0m".format(floor_text, seat))
    return floor_text, seat


def getSeatNum(strResult, stateCode):
    floor_text, seat = getSeatText(strResult, stateCode)
    return floorDict[floor_text] + str(seat), floorDict[floor_text]
