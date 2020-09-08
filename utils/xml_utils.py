# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : test_xml2dict.py	
#   @Created Date: 2020-07-26 8:40
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
__author__ = 'zhiming'

import json

import xmltodict
from dict2xml import dict2xml


def main():
    str_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <message>
        <dic_sex>
            <sex_id>1</sex_id>
            <sex_code>1</sex_code>
            <sex_name>男</sex_name>
            <create_time>2020-04-30 16:00:00</create_time>
            <creator>zhiming</creator>
        </dic_sex>
    </message>"""
    dic_data = xml_to_dict(str_xml)

    print(dic_data)


def dict_to_xml(dict_data: dict) -> dict:
    """
    将字典数据类型转成xml格式的str并返回
    :param dict_data: 字典数据
    :return: str
    wrap：将整个树包装在此标记中
    缩进：等于为每一层嵌套的每一行加上前缀
    换行符：是否使用换行符
    """
    str_xml = dict2xml(dict_data, wrap="", indent=" ")

    return {"error": 0, "data": str_xml, "desc": "处理成功!"}


def xml_to_dict(str) -> dict:
    """
    将str类型的xml转成dict
    :param str: xml字符串
    :return:
    """
    dic_xml = xmltodict.parse(str)
    # dict转成str类型的json
    str_json = json.dumps(dic_xml, ensure_ascii=False)

    return {"error": 0, "data": str_json, "desc": "处理成功!"}


if __name__ == "__main__":
    print(__name__)
    main()
