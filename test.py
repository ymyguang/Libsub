import time

from tools import fileExam

i = 1
def dsx():
    while 1:
        global i
        print("当前i值:", i)
        i = input()
        time.sleep(1)


if __name__ == '__main__':
    dsx()
