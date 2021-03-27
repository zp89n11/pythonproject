# -*- encoding: utf-8 -*-
# @ModuleName: HeroEum
# @Function: 
# @Author: 张鹏
# @Time: 2021/3/28 1:19
from enum import Enum

from py_practical_1.Police import Police
from py_practical_1.Timo import Timo


class HeroEnum(Enum):
    """
    这是英雄枚举
    """
    timo_enum = ["timo", Timo()]
    police_enum = ["Police", Police()]
