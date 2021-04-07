# -*- encoding: utf-8 -*-
# @ModuleName: conftest
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/6 23:47
import pytest

from pytestdemo.calculator import Calculator


@pytest.fixture(scope="session")
def login():
    print("登录成功")
    yield Calculator()
    print("退出登录")


@pytest.fixture(scope="session")
def connectDB():
    print("数据库")
