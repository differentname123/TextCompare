# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from common.file_deal import read_all


def fenli(str):
    temp = str.split(',')
    temp.sort(key=None, reverse=False)
    for xx in temp:
        print xx


# 将commom目录下的test.txt文件进行解析排序
if __name__ == '__main__':
    originStr = read_all(sys.path[0] + '/' + 'common/' + 'test.txt')
    fenli(originStr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
