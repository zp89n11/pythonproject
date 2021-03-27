# -*- encoding: utf-8 -*-
# @ModuleName: HouseFactory 英雄工厂类
# @Function: 
# @Author: 张鹏
# @Time: 2021/3/28 0:29
from py_practical_1.HeroEum import HeroEnum
from py_practical_1.Police import Police
from py_practical_1.Timo import Timo


class HeroFactory:

    def hero_init(self, name):
        # for member in HeroEnum.value:
        #     if member[0] == name:
        #         return member[1]
        # return Exception(f"英雄{name}不存在！！")

        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            return Exception(f"英雄{name}不存在！！")


# 实例化timo类
timo_init = HeroFactory().hero_init("timo")
# 实例化女警类
police_init = HeroFactory().hero_init("police")
# 调用打架的方法
timo_init.fight(police_init.power, police_init.hp)
police_init.fight(timo_init.power, timo_init.hp)
