def getCurntSeatNum():
    strResult = """"3对不起，您已预约了[[[[[][][][][()()六层南区(())()和其他空间座位(不对号入座)] [075]座位。请在规定的时间内刷卡确认,或者取消该预约。";/*"""
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

    for i in list(floorDict.keys()):
        if i in strResult:
            floor = i
    end = strResult.find("]座位")
    seat = strResult[end - 3:end]
    # print(floor, seat, strResult)
    # seatNum = floorDict[floor] + str(seat)
    # return seatNum, floor, seat
    print(floor, seat)
