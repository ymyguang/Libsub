import requests
from tools import feedback
cookieDic = {
    "my": "ASP.NET_SessionId=wldmrppkfwpiiu2xo5eirup2; Reader_barcode=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserIdentID=WechatTSG=A3B25858882C9674246B16B06F7EC204&WeChatUserCenter=1990752135; UserOpenID=WechatTSG=1008220200902091753255265176; UserName=WechatTSG=%e5%88%98%e5%bd%aa; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e5%88%98%e5%bd%aa;",
    "zhou": "ASP.NET_SessionId=ibrq1gah4kf3gcdx432lp4hv; UserType=WechatTSG=0; UserGrade=WechatTSG=; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1630841155,1631015315; Reader_barcode=WechatTSG=52DCB27540694334897FE11C1B91B685&WeChatUserCenter=1790752062; UserIdentID=WechatTSG=52DCB27540694334897FE11C1B91B685&WeChatUserCenter=1790752062; UserOpenID=WechatTSG=1008220210909170756771352538; UserName=WechatTSG=%e5%91%a8%e8%b6%85; Reader_name=WeChatUserCenter=%e5%91%a8%e8%b6%85; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1631178631",
    "guo": "ASP.NET_SessionId=ymof0atqw4zgs3nkxmlfbazs; Reader_barcode=WechatTSG=A3B25858882C9674C946AF4141FB55E1&WeChatUserCenter=1990752102; UserIdentID=WechatTSG=A3B25858882C9674C946AF4141FB55E1&WeChatUserCenter=1990752102; UserOpenID=WechatTSG=1008220200905174919747633410; UserName=WechatTSG=%e9%83%ad%e4%ba%8c%e9%be%99; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e9%83%ad%e4%ba%8c%e9%be%99; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1630841155,1631015315,1631607432; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1631607432",
    'yang': 'ASP.NET_SessionId=a3vvchz0511w4wekglinqemp; Reader_barcode=WechatTSG=A3B25858882C9674C8AA70EC9728F918&WeChatUserCenter=1990752144; UserIdentID=WechatTSG=A3B25858882C9674C8AA70EC9728F918&WeChatUserCenter=1990752144; UserOpenID=WechatTSG=1008220201120111135203122355; UserName=WechatTSG=%e6%9d%a8%e7%bf%94%e5%ae%87; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e6%9d%a8%e7%bf%94%e5%ae%87; Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1631607432,1632146438,1633069860,1633828441; Hm_lpvt_a75caadd7b293bc3cfd97cd8de8e742a=1633828441',
    'gao':"Hm_lvt_a75caadd7b293bc3cfd97cd8de8e742a=1631607432,1632146438,1633069860,1633828441; ASP.NET_SessionId=riu5tlv1f04jbwwmaoaee20u; Reader_barcode=WechatTSG=A3B25858882C9674337D225FD054C32C&WeChatUserCenter=1990752130; UserIdentID=WechatTSG=A3B25858882C9674337D225FD054C32C&WeChatUserCenter=1990752130; UserOpenID=WechatTSG=1008220201010174645751178952; UserName=WechatTSG=%e9%ab%98%e4%b8%96%e8%b1%aa; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e9%ab%98%e4%b8%96%e8%b1%aa",
    'tao':"ASP.NET_SessionId=vp0xeytvesfdgivx2ayosqza; Reader_barcode=WechatTSG=235A5A7E061039C91831D624823CB9D4&WeChatUserCenter=1891103126; UserIdentID=WechatTSG=235A5A7E061039C91831D624823CB9D4&WeChatUserCenter=1891103126; UserOpenID=WechatTSG=1008220210905152618860341696; UserName=WechatTSG=%e9%99%b6%e9%9b%a8%e6%99%b4; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_name=WeChatUserCenter=%e9%99%b6%e9%9b%a8%e6%99%b4",
    'wuwei':"ASP.NET_SessionId=vp0xeytvesfdgivx2ayosqza; UserType=WechatTSG=0; UserGrade=WechatTSG=; Reader_barcode=WechatTSG=A3B25858882C9674D88E645328A2247C&WeChatUserCenter=1990752142; UserIdentID=WechatTSG=A3B25858882C9674D88E645328A2247C&WeChatUserCenter=1990752142; UserOpenID=WechatTSG=1008220200830143241442993859; UserName=WechatTSG=%e5%90%b4%e5%8d%ab; Reader_name=WeChatUserCenter=%e5%90%b4%e5%8d%ab"

}
SEAT = "http://tsgic.hebust.edu.cn/ajaxpro/WechatTSG.Web.Seat.BespeakSeat.BespeakSeatList,WechatTSG.Web.ashx"
HEADERS = {}


def init(name):
    global HEADERS
    HEADERS = {
        'Cookie': cookieDic[name],
        'X-AjaxPro-Method': 'submitBespeak',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br'
    }


def subscribe(seatNum, name):
    init(name)
    seatNum = str(seatNum)
    implHEADRES = HEADERS.copy()
    implHEADRES["X-AjaxPro-Method"] = "submitBespeak"
    try:
        result = requests.post(SEAT, headers=implHEADRES, json={"seatNum": seatNum})  # 读取座位信息/六楼走廊
        return result
    except Exception as e:
        s = "sub-subscribe--产生异常" + str(e)
        print(s)
        feedback.feedback(s)


def getCookie(name):
    init(name)
    return HEADERS["Cookie"]


def getHeader(name):
    init(name)
    return HEADERS
