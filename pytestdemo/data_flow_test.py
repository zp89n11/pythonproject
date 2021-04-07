# -*- encoding: utf-8 -*-
# @ModuleName: data_flow_test,方法类
# @Function: 
# @Author: 张鹏
# @Time: 2021/4/7 22:20
import yaml


# pip install pyyaml
def get_datas():
    with open("./datas/data.yml", "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas
