# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : 装饰器消除副作用.py	
#   @Created Date: 2020-06-07 9:09
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 装饰器消除副作用
#
# ======================================================================
import functools


def note(func):
    """装饰器的说明文档"""

    @functools.wraps(func)
    def wrapper():
        """wrapper function装饰器的说明文档"""
        print("装饰器在此次完成需要完成的功能")
        return func()

    return wrapper


@note
def test():
    """test 说明文档"""
    print("test")


def main():
    # 打印函数文档
    print(test.__doc__)


if __name__ == "__main__":
    main()
