from datetime import datetime


def get_time(text="INFO", name=""):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S[") + text + " -" + name + "]"
    return str(current_time)
