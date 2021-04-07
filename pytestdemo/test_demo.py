# -*- encoding: utf-8 -*-
# @ModuleName: test_demo
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/6 22:28
import allure
import pytest

from pytestdemo.data_flow_test import get_datas


@allure.feature("计算器测试用例")
class TestCal:

    @allure.story("加法测试，整数")
    @pytest.mark.parametrize("a,b,expect", get_datas()["add_int"]["data"])
    def test_add_int(self, a, b, expect, login):
        with allure.step("结果校验"):
            assert expect == login.add(a, b)

    @allure.story("加法测试，浮点型")
    @pytest.mark.parametrize("a,b,expect", get_datas()["add_float"]["data"])
    def test_add_float(self, a, b, expect, login):
        with allure.step("结果校验"):
            assert expect == round(login.add(a, b), 2)

    @allure.story("加法校验，字符串")
    @pytest.mark.parametrize("a,b,expect", get_datas()["add_str"]["data"])
    def test_add_str(self, a, b, expect, login):
        with allure.step("结果校验"):
            assert expect == login.add(a, b)

    @allure.story("除法测试，整数")
    @pytest.mark.parametrize("a,b,expect", get_datas()["div_int"]["data"])
    def test_div_int(self, a, b, expect, login):
        with allure.step("结果校验"):
            assert expect == login.div(a, b)

    @allure.story("除法测试，字符串")
    @pytest.mark.parametrize("a,b,expect", get_datas()["div_str"]["data"])
    def test_div_str(self, a, b, expect, login):
        with allure.step("结果校验"):
            assert expect == login.div(a, b)
