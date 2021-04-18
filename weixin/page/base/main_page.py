# -*- encoding: utf-8 -*-
# @ModuleName: main_page
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 16:56
from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base.base_page import BasePage
from weixin.page.other.add_user import Add_User
from weixin.page.other.edit_user import EditUser


class MainPage(BasePage):

    def address_list(self, maxNum: int = 3):
        """
        主页点击通讯录标签
        :return: 添加成员页面
        """
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        for i in range(0, maxNum):
            try:
                self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()
                break
            except:
                self.move()
        return Add_User(self.driver)

    def user_detail(self, name: str):
        """
        通讯页面进入用户个人信息页面。编辑页面
        :param name:  需要删除的人员
        :return:  返回编辑页面
        """
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 进入详情页面
        for i in range(0, 3):
            els2_list = self.find_list(MobileBy.XPATH, f'//*[@text="{name}"]')
            if len(els2_list) != 0:
                break
            self.move()
        els2_list[0].click()
        self.find(MobileBy.ID, "com.tencent.wework:id/h8g").click()
        # 点击编辑按钮
        self.find(MobileBy.ID, "com.tencent.wework:id/b49").click()
        return EditUser(self.driver)
