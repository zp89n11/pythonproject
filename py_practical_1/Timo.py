# -*- encoding: utf-8 -*-
# @ModuleName: Timo,子英雄类提莫队长
# @Function: 
# @Author: 张鹏
# @Time: 2021/3/28 0:19
from py_practical_1.Hero import Hero


class Timo(Hero):
    # 提莫默认血量是一千
    hp = 1000
    # 攻击力默认是100
    power = 100
    # 台词
    speakLines = "提莫队长正在待命"
    '''英雄的名'''
    name = "提莫"
