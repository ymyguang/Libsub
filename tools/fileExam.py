import os

from tools import printLog


def handelFile(fileName):
    # 若不存在,则创建文件
    if os.path.isfile(fileName) is False:
        cmd = "type nul >" + fileName
        os.system(cmd)

    # 检测文件大小
    file = open(fileName, 'r+')
    lines = file.readlines()

    # 删除文件
    if len(lines) > 300:
        file.close()
        # 删除
        cmd = "del " + fileName
        os.system(cmd)
        print(printLog.get_time(), '当前过大,将删除该文件\n**************删除文件', "**************")
        # 创建文件
        cmd = "type nul >" + fileName
        os.system(cmd)
        # 添加初始值
        write(fileName, "zhou")
    file.close()


def write(fileName, content):
    handelFile(fileName)
    content = '\n' + content
    file = open(fileName, 'a', encoding='utf-8')
    file.write(content)
    file.close()


def readLastLine(fileName):
    handelFile(fileName)
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.readlines()
    if len(lines) != 0:
        return lines[-1]
