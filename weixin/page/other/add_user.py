# -*- encoding: utf-8 -*-
# @ModuleName: add_user
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 17:03
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as f
from selenium.webdriver.support.wait import WebDriverWait

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
        # 退回到通讯录页面,先等待元素出现
        elem_1 = (MobileBy.ID, "com.tencent.wework:id/h86")
        WebDriverWait(self.driver, 10).until(f.visibility_of_element_located(elem_1))
        self.find(*elem_1).click()
        # 查询新增的人员
        self.find(MobileBy.ID, "com.tencent.wework:id/h8q").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/g1n").send_keys(userName)
        return self

    def assertResult(self, userName):
        text: str = self.find(MobileBy.XPATH,
                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                              ".LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                              ".widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android"
                              ".widget.RelativeLayout["
                              "2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget"
                              ".RelativeLayout/android.view.ViewGroup/android.widget.TextView").text
        assert text == userName
