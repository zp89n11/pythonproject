# -*- encoding: utf-8 -*-
# @ModuleName: add_user
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 17:03
from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base.base_page import BasePage


class Add_User(BasePage):

    def save_user(self, userName, userTal):
        """
        添加成员页面
        :param userName:
        :param userTal:
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(userName)
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(userTal)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.save_picture()
