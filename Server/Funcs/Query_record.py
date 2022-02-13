"""
创建日期：2022.2.9
作者：乔毅
文件名：Query_record.py
功能：通过微信ID获取该用户的搜索历史
备注：代码中被注释掉的print()为 测试时调用，控制台输出没有实际意义
"""

# 导入库
import pymysql
import asyncio
import sys
import time
import datetime

sys.path.append("..")


async def query_record(wx_id: str) -> list:
    """
    函数名：Query_record
    作用：根据微信ID获取用户所有搜索记录并返回
    :param wx_id:用户微信ID
    :return:result_list:记录列表
    """

    # 结果列表
    result_list = []
    try:
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="Insight")
        # cursor创建游标对象,字典类型
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 依据微信ID查询数据库
        cursor.execute("""SELECT * FROM query_record WHERE ID = %s""" % wx_id)
        record_cursor = cursor.fetchall()

        # 整理结果
        for row in record_cursor:
            # print(row)
            record_data = {
                'time': row['Time'].strftime('%Y-%m-%d %H:%M:%S'),
                'query': row['Query']
            }
            result_list.append(record_data)

        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        db.close()
    except Exception as e:
        print("ERROR as -> ", e)

    return result_list

if __name__ == '__main__':
    WX_id = 1
    res = asyncio.get_event_loop().run_until_complete(query_record(wx_id=WX_id))
    for i in range(0, len(res)):
        print(res[i])


