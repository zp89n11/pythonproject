# -*- encoding: utf-8 -*-
# @ModuleName: app
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/18 22:04
from appium import webdriver

from weixin.page.base.base_page import BasePage
from weixin.page.base.main_page import MainPage


class App(BasePage):
    _platformName = "Android"
    _deviceName = "127.0.0.1:7555"
    _appPackage = "com.tencent.wework"
    _appActivity = ".launch.WwMainActivity"

    def new_app(self):
        """
        启动客户端，打开企业微信
        :param driver:
        """
        if self.driver is None:
            desire_cap = {
                "platformName": f"{self._platformName}",
                "deviceName": f"{self._deviceName}",
                "appPackage": f"{self._appPackage}",
                "appActivity": f"{self._appActivity}",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        else:
            self.driver.start_activity(self._appPackage, self._appActivity)
        self.driver.implicitly_wait(10)
        return self

    def main_page(self) -> MainPage:
        return MainPage(self.driver)
