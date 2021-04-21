# -*- encoding: utf-8 -*-
# @ModuleName: base_page
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/17 15:32
import time

import allure
import yaml
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class BasePage:
    driver: WebDriver
    _black_list = [()]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

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
        TouchAction(self.driver).press(x=int(width / 2), y=int(height * 0.8)).wait(200).move_to(x=int(width / 2), y=int(
            height * 0.2)).release().perform()

    """查找元素，包含异常处理，——black_list中是一些弹窗的定位方式"""

    def find(self, by, location):
        try:
            return self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, location)
        except:
            for black in self._black_list:
                ele = self.driver.find_elements(*black)
                if len(ele) > 0:
                    ele[0].click()
                    break
            return self.find(by, location)

    def find_list(self, by, value):
        return self.driver.find_elements(by, value)

    """
    执行指定文件中的步骤，指定文件的格式是yaml
    """
    def steps(self, step_yaml_path, value=None):
        element: WebDriver = None
        with open(step_yaml_path, "utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
               element = self.find(step["by"], step["location"])
            if 'action' in step.keys():
                if step["action"] == 'click':
                   element.click()
                if step['action'] == 'send':
                    if step['value'] == '${value}':
                        value = value
                    else:
                        value = step['value']
                    element.send_keys(value)
