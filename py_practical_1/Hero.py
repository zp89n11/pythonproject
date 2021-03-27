# -*- encoding: utf-8 -*-
# @ModuleName: House,英雄类。是所有之类英雄的父类，
# @Function: 
# @Author: 张鹏
# @Time: 2021/3/28 0:12


class Hero:
    # 血量
    hp = 0
    # 攻击力
    power = 0
    # 台词
    speakLines = ""
    '''英雄的名'''
    name = ""

    def speak_lines(self):
        print(f"{self.speakLines}")

    def fight(self, enemy_power, enemy_hp):
        # 英雄的名言
        self.speak_lines()
        # 我的血量减去敌人的攻击力获取剩余血量
        my_hp = self.hp - enemy_power
        # 敌人的血量是多少
        enemy_final_hp = enemy_hp - self.power
        if my_hp > enemy_final_hp:
            print(f"{self.name}赢了！！！")
        elif enemy_final_hp > my_hp:
            print("敌人赢了！！！")
        else:
            print("平手")

