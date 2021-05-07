# coding=utf-8
# 读出文件所有内容并返回
def read_all(filename):
    with open(filename, 'r') as f:
        return f.read()