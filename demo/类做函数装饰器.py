# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : 类做函数的装饰器.py
#   @Created Date: 2020-06-07 9:38
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================


class Test(object):
    def __init__(self, func):
        print(f"对象初始化,含有方法:{func.__name__}")
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__func()


@Test
def test():
    print("---test---")


def main():
    t = test()


if __name__ == "__main__":
    main()
