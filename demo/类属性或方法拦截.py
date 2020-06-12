# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : 类属性或方法拦截.py	
#   @Created Date: 2020-06-07 8:48
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 使用拦截器的应用:如果有哪个用户调用了该属性或者方法,可以存入log日志中
#
# ======================================================================


class Demo(object):
    def __init__(self, object1):
        self.subject1 = object1
        self.subject2 = "subject2"

    def __getattribute__(self, item):
        # item为该对象的属性或者方法(使用该对象拥有的对象或方法进行比较,使用动态增加的方法或属性也可;)
        if item == "subject1":
            print("因为您设定的属性或方法符合要求,所以执行了本代码;")
            return "python3"
        else:
            # 放行,使用父类的原获取属性或方法的方法
            return object.__getattribute__(self, item)


def main():
    d = Demo("python2")
    print(d.subject1, d.subject2)


if __name__ == "__main__":
    main()
