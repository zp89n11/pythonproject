# -*- encoding: utf-8 -*-
# @ModuleName: test_one
# @Function:
# @Author: 张鹏
# @Time: 2021/4/17 15:49

import pytest
from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base.app import App
from weixin.page.base_flow_test import get_datas


class TestOne:

    def setup(self):
        print("开始启动app")
        self.main = App().new_app()

    @pytest.mark.parametrize("userName,userTal", get_datas())
    def test_0001(self, userName, userTal):
        self.main.main_page().address_list().save_user(userName, userTal).assertResult(userName)

    def test002(self):
        self.main.main_page().user_detail().delete_user()
