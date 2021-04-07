# -*- encoding: utf-8 -*-
# @ModuleName: calculator
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/6 22:29

# 计算器
class Calculator:

    def add(self, a, b):
        if not isinstance(a, str) and not isinstance(b, str):
            return a + b
        return "参数类型错误"

    def div(self, a, b):
        if not isinstance(a, str) and not isinstance(b, str):
            if b != 0:
                return a/b
            else:
                return "参数b不可以为零！！"
        return "参数类型错误"
