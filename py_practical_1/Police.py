# -*- encoding: utf-8 -*-
# @ModuleName: Police 女警
# @Function: 
# @Author: 张鹏
# @Time: 2021/3/28 0:22
from py_practical_1.Hero import Hero


class Police(Hero):
    # 女警默认血量是900
    hp = 900
    # 攻击力默认是110
    power = 110
    # 台词
    speakLines = "见识一下法律的子弹"
    '''英雄的名'''
    name = "女警"
