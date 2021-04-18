# -*- encoding: utf-8 -*-
# @ModuleName: test_tow
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 22:20
from weixin.page.base_flow_test import get_tel, get_GBK2312


class TestTow:

    def test_001(self):
        str3 = get_GBK2312(3)
        print(str3)
        num = get_tel()
        print(num)
