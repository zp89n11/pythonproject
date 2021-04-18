# -*- encoding: utf-8 -*-
# @ModuleName: edit_user
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 19:02
from appium.webdriver.common.mobileby import MobileBy
from weixin.page.base.base_page import BasePage


class EditUser(BasePage):

    def delete_user(self):
        # 滑动、删除
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/bei').click()
