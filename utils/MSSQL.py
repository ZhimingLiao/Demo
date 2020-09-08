# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : Administrator
#   @Project     : Demo
#   @File Name   : MSSQL.py	
#   @Created Date: 2020-08-06 8:11
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : MSSQL查询封装
#
# ======================================================================
import pymssql
from loguru import logger

class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有选择数据库")
        # 打开数据库连接
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd
                                    , database=self.db, charset="utf8", timeout=2000)
        # 使用cursor()方法获取操作游标
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "connect database fails")
        else:
            return cur

    def ExecQuery(self, sql):
        try:
            cur = self.__GetConnect()
            # 执行SQL语句
            cur.execute(sql)

            # 获取所有记录列表
            rows = cur.fetchall()

            cur.close()
            # 关闭数据库连接
            self.conn.close()
            return rows

        except Exception as e:
            logger.error("非常抱歉,匹配记录出错,可能是查询没有数据")
            logger.error(e)

def ExecNonQuery(self, sql):
    try:
        cur = self.__GetConnect()
        cur.execute(sql)
        # 提交到数据库执行
        self.conn.commit()
        self.conn.close()
    except:
        # 发生错误时回滚
        self.db.rollback()


def main():
    ms = MSSQL(host="127.0.0.1", user="sa", pwd="demo", db="DictDB_xyyy")
    rows = ms.ExecQuery("SELECT top 5 EMPLOYE_CODE, EMPLOYE_NAME FROM DC_DICT_EMPLOYEE")
    for i in rows:
        logger.info(i)


if __name__ == "__main__":
    main()
