# -*- encoding: utf-8 -*-
# @ModuleName: base_page
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 15:32
import time

import allure
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _platformName = "Android"
    _deviceName = "127.0.0.1:7555"
    _appPackage = "com.tencent.wework"
    _appActivity = ".launch.WwMainActivity"

    def __init__(self, driver: WebDriver = None):
        """
        启动客户端，打开企业微信
        :param driver:
        """
        desire_cap = {
            "platformName": f"{self._platformName}",
            "deviceName": f"{self._deviceName}",
            "appPackage": f"{self._appPackage}",
            "appActivity": f"{self._appActivity}",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        if driver is None:
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        else:
            self.driver = driver
        self.driver.implicitly_wait(10)

    def save_picture(self, path=None):
        """
        保存截图
        :param path:
        :return:
        """
        if path is not None:
            path = path
        else:
            path = time.time()
        self.driver.save_screenshot(f"./result/{path}.png")
        allure.attach.file(f"./result/{path}.png", attachment_type=allure.attachment_type.PNG)

    def move(self):
        """
        滑动屏幕
        :return:
        """
        window_size = self.driver.get_window_rect()
        width = window_size["width"]
        height = window_size["height"]
        TouchAction(self.driver).press(x=int(width / 2), y=int(height * 0.8)).wait(200).move_to(x=int(width / 2), y=int(height * 0.2)).release().perform()

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_list(self, by, value):
        return self.driver.find_elements(by, value)
