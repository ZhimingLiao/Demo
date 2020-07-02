# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : Administrator
#   @Project     : Demo
#   @File Name   : test_excelutils.py	
#   @Created Date: 2020-07-01 10:55
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================

from utils.ExeclUtils import ExcelUtils as xlsx
from utils.ExeclUtils import get_pinyin

def excel_to_py():
    file_path = r"C:\Users\Administrator\Desktop\科室字典.xlsx"
    data = xlsx.execl_to_list_for_openpyxl(file_path).get("data")
    # 标题
    header = data[0]
    # 剔除标题
    data.pop(0)
    list_data = list()
    # 得到含有拼音的列表
    for tmp_data in data:
        tmp_dict_data = dict(zip(header, tmp_data))
        tmp_dict_data["py"] = get_pinyin(tmp_dict_data.get("ksmc"))
        list_data.append(list(tmp_dict_data.values()))

    import os
    filepath, fullflname = os.path.split(file_path)
    fname, ext = os.path.splitext(fullflname)
    fname = fname + "-result" + ext
    # 得到需要保存的路径名称
    file_path_to_save = os.path.join(filepath, fname)
    # 保存数据
    result = xlsx.list_to_execl(list_data=list_data, file_path_to_save=file_path_to_save)
    print(result.get("msg"))


def main():
    excel_to_py()

def getpy_for_xlsx(data: dict, col: int) -> dict:
    """
    将xlsx内容的指定的列中文得到拼音码
    :param data: 字典数据
    :return:
    """


if __name__ == "__main__":
    main()
