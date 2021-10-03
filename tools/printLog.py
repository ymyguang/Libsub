from datetime import datetime


def get_time(text="INFO"):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S[") + text + "]"
    return str(current_time)
