import os
import sys


def tt(t):
    t = str(t) + "\n"
    if os.path.isfile('info.txt') is False:
        os.system("type nul > info.txt")
    file = open('info.txt', 'r+')
    lines = file.readlines()
    print(len(lines))
    if len(lines) > 3:
        file.close()
        os.system("del info.txt")
        print('删除文件')
        os.system("type nul > info.txt")
        file = open('info.txt', 'r+')
        lines = []
    if len(lines) != 0:
        if lines[-1] == str(t):
            print("卡壳了")
            exit()
        else:
            file.write(t)
    else:
        file.write(t)
    file.close()


if __name__ == '__main__':
    l = ['1', ';s', '2', '1', '1', '2']
    for i in l:
        tt(i)
