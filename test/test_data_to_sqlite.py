# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : Administrator
#   @Project     : Demo
#   @File Name   : test_data_to_sqlite.py	
#   @Created Date: 2020-07-28 10:56
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
from loguru import logger


def read_data_from_txt(file_path: str) -> dict:
    with open(file_path, encoding='utf8') as f:
        tmp_data = f.readline().replace('\n', '').replace('\r', '')

        list_result = list()
        while tmp_data:
            dict_data = dict()

            t_data = tmp_data.split("–")
            logger.debug(t_data)
            tmp_data = f.readline().replace('\n', '').replace('\r', '')
            dict_data['name'] = t_data[0]
            dict_data['desc'] = t_data[1]

            list_result.append(dict_data)
    return {"error": 0, "msg": "处理成功!", "data": list_result}


def write_data_to_sqlite3(db_path: str, data: dict) -> dict:
    import sqlite3
    error, msg = 0, None
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute("insert into utils_for_python(utils_name, utils_desc) values(?, ?)", ('杂项 ', ''))
        # 得到受影响的行的id
        utils_id = cur.lastrowid
        for data_tmp in data:
            cur.execute('insert into utils_for_python_detail(utils_id, demo, desc) values(?, ?, ?)'
                        , (utils_id, data_tmp.get('name').strip(), data_tmp.get('desc').strip()))
    except(Exception, ) as e:
        error = 1
        msg = e
        logger.debug(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()
    return {"error": error if error else 0, 'msg': f"处理成功!详情请查看数据库:{db_path}" if not msg else msg}


def main():
    file_path, db_path = 'data.txt', r'C:\Users\Administrator\OneDrive\文档\database\zhiming.sqlite'
    data = read_data_from_txt(file_path=file_path).get('data')
    result = write_data_to_sqlite3(db_path=db_path, data=data)
    logger.info(result)


if __name__ == "__main__":
    main()
