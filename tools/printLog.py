from datetime import datetime


def get_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S[INFO]")
    return str(current_time)