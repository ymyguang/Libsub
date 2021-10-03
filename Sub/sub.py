import requests

cookieDic = {
    "my": "ASP.NET_SessionId=wldmrppkfwpiiu2xo5eirup2; Reader_barcode=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserIdentID=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserOpenID=WechatTSG=1008220200902091753255265176; UserName=WechatTSG=%e5%88%98%e5%bd%aa; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e5%88%98%e5%bd%aa;",
    "other": "ASP.NET_SessionId=ibrq1gah4kf3gcdx432lp4hv; UserType=WechatTSG=0; UserGrade=WechatTSG=; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1630841155,1631015315; Reader_barcode=WechatTSG=52DCB27540694334897FE11C1B91B685&WeChatUserCenter=1790752062; UserIdentID=WechatTSG=52DCB27540694334897FE11C1B91B685&WeChatUserCenter=1790752062; UserOpenID=WechatTSG=1008220210909170756771352538; UserName=WechatTSG=%e5%91%a8%e8%b6%85; Reader_name=WeChatUserCenter=%e5%91%a8%e8%b6%85; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1631178631",
    "zhao": "ASP.NET_SessionId=ymof0atqw4zgs3nkxmlfbazs; Reader_barcode=WechatTSG=A3B25858882C9674C946AF4141FB55E1&WeChatUserCenter=1990752102; UserIdentID=WechatTSG=A3B25858882C9674C946AF4141FB55E1&WeChatUserCenter=1990752102; UserOpenID=WechatTSG=1008220200905174919747633410; UserName=WechatTSG=%e9%83%ad%e4%ba%8c%e9%be%99; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e9%83%ad%e4%ba%8c%e9%be%99; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1630841155,1631015315,1631607432; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1631607432",
    "test" : "s"
}
SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {
    'Cookie': cookieDic["other"],
    # 'X-AjaxPro-Method': 'submitChoose',
    'X-AjaxPro-Method': 'submitBespeak',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
}


def subscribe(seatNum):
    seatNum = str(seatNum)
    implHEADRES = HEADERS.copy()
    implHEADRES["X-AjaxPro-Method"] = "submitBespeak"
    result = requests.post(SEAT, headers=implHEADRES, json={"seatNum": seatNum})  # 读取座位信息/六楼走廊
    return result


def getCookie():
    return HEADERS["Cookie"]
