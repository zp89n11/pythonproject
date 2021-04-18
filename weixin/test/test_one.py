# -*- encoding: utf-8 -*-
# @ModuleName: test_one
# @Function:
# @Author: 张鹏
# @Time: 2021/4/17 15:49

import pytest

from weixin.page.base.main_page import MainPage
from weixin.page.base_flow_test import get_datas


class TestOne:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize("userName,userTal", get_datas())
    def test_0001(self, userName, userTal):
        self.main.address_list().save_user(userName, userTal)

    def test002(self):
        self.main.user_detail("张三").delete_user()
