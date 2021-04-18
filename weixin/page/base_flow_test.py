# -*- encoding: utf-8 -*-
# @ModuleName: base_flow_test
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 22:09
import random


def get_tel():
    num = random.randint(10000000, 99999999)
    return f"176{num}"


def get_GBK2312(num: int = 3):
    list_str = []
    for i in range(0, num):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        list_str.append(bytes.fromhex(val).decode('gb2312'))
    return "".join(list_str)


def get_datas():
    str3 = get_GBK2312(3)
    num = get_tel()
    return [[str3, num]]