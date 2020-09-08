# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : Administrator
#   @Project     : Demo
#   @File Name   : cad_utils.py	
#   @Created Date: 2020-08-06 8:47
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
import sys, os
import json
from loguru import logger

from utils.MSSQL import MSSQL


def main():
    with open("config.json", 'r', encoding="utf8") as f:
        json_data = json.load(f)

    ms = MSSQL(host=json_data.get("host"), user=json_data.get("user")
               , pwd=json_data.get("pwd"), db=json_data.get("db"))
    sql = json_data.get("sql")
    rows_data = ms.ExecQuery(sql=sql)


    # import sqlite3

    # conn = sqlite3.connect(r'C:\Users\Administrator\OneDrive\文档\database\dic.sqlite')
    # c = conn.cursor()
    # cursor = c.execute("SELECT sex_code, sex_name, creator from dic_sex")
    # rows_data = cursor.fetchall()

    # logger.info(f'记录总数:{cur.rowcount}')

    if not rows_data:
        logger.error("非常抱歉,我们没有查询到数据,请重新编辑sql语句并且写到配置文件中...")
        return
        # 创建文件夹
    if not os.path.exists("CDA文档"):
        os.mkdir("CDA文档")

    i = 0
    for rows in rows_data:
        i += 1
        # 创建文件夹
        if not os.path.exists(f'CDA文档\{rows[2]}'):
            os.mkdir(f'CDA文档\{rows[2]}')

        str_file = f"CDA文档\{rows[2]}\{rows[0]}-T{('000' + str(i))[-3:]}.xml"
        logger.info(f'正在输出文件:{str_file}')
        with open(file=str_file, mode="w", encoding="utf8") as f:
            f.writelines(rows[1])


if __name__ == "__main__":

    if hasattr(sys, 'frozen'):
        os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

    main()
    input("按任意键关闭本窗口")
