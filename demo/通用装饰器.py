# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : 通用装饰器.py	
#   @Created Date: 2020-06-07 9:21
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 集合了通用装饰器及带有参数的装饰器;应用场景:记录日志,权限验证
#
# ======================================================================


# 不带参数的装饰器
def func(function_name):
    def func_in(*args, **kwargs):
        print("------记录日志------")
        ret = function_name(*args, **kwargs)
        return ret

    return func_in


# 带参数的装饰器
def func_arg(arg1):
    def func_i(function_name):
        def func_in(*args, **kwargs):
            print("------记录日志(arg=%s)------" % arg1)
            if arg1 == "abc":
                ret = function_name(*args, **kwargs)
                ret = function_name(*args, **kwargs)
            else:
                ret = function_name(*args, **kwargs)
            return ret

        return func_in

    return func_i


@func_arg(arg1="abc")
def test(a):
    print("---test---")


@func
def test2(ab=23):
    print("---test---")


def main():
    t = test(1)
    t2 = test2(ab=56)


if __name__ == "__main__":
    main()
