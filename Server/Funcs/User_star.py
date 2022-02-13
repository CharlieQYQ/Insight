"""
创建日期：2022.2.10
作者：乔毅
文件名：User_star.py
功能：添加用户收藏
备注：代码中被注释掉的print()为 测试时调用，控制台输出没有实际意义
"""

# 导入库
import pymysql
import sys
import asyncio
# import json

sys.path.append("..")


async def add_star(wx_id: str, msg_id: int) -> bool:
    """
    函数名：add_star
    作用：根据用户微信ID和案例编号添加用户收藏
    :param wx_id:用户微信ID
    :param msg_id:案例ID
    :return:state:成功状态
    """

    # 打开数据库连接
    db = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="Insight")
    # cursor创建游标对象,字典类型
    cursor = db.cursor(pymysql.cursors.DictCursor)

    try:
        # 插入收藏记录到数据库
        state = cursor.execute("""INSERT INTO user_star (ID, msg_id) VALUES (%s, %d)""" % (wx_id, msg_id))
        db.commit()
        cursor.close()
        db.close()
        return state == 1
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        return False


async def remove_star(wx_id: str, msg_id: int) -> bool:
    """
    函数名：remove_star
    作用：根据用户ID和案例编号删除用户收藏
    :param wx_id:用户微信ID
    :param msg_id:案例ID
    :return:state:成功状态
    """

    # 打开数据库连接
    db = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="Insight")
    # cursor创建游标对象,字典类型
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 检测是否存在该条记录
    is_exist = cursor.execute("""SELECT * FROM user_star WHERE ID = %s AND msg_id = %d""" % (wx_id, msg_id))
    # 如果存在，则删除
    if is_exist == 1:
        try:
            cursor.execute("""DELETE FROM user_star WHERE ID = %s AND msg_id = %d""" % (wx_id, msg_id))
            db.commit()
            cursor.close()
            db.close()
            return True
        except:
            db.rollback()
            cursor.close()
            db.close()
            return False
    else:
        cursor.close()
        db.close()
        return False


async def get_user_star_list(wx_id: str) -> list:
    """
    函数名：get_user_star_list
    作用：通过用户微信ID获取其收藏列表
    :param wx_id:用户微信ID
    :return: result_list：结果列表，每一项是一个字典
    """

    # 结果字典
    result_list = []

    # 打开数据库连接
    db = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="Insight")
    # 创建字典类型游标
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 查询用户数据
    count = cursor.execute("""SELECT msg_info.msg_id, msg_info.msg_text FROM user_star, msg_info WHERE user_star.ID = %s AND user_star.msg_id = msg_info.msg_id""" % wx_id)
    # 如果为空数据，即用户没有加过收藏，即返回空列表
    if count == 0:
        cursor.close()
        db.close()
        return result_list
    else:
        result = cursor.fetchall()
        for row in result:
            data = {
                'msg_id': row['msg_id'],
                'msg_text': row['msg_text']
            }
            result_list.append(data)
        cursor.close()
        db.close()
        return result_list


if __name__ == '__main__':
    WX_id = 1
    Msg_id = 3
    # res = asyncio.get_event_loop().run_until_complete(add_star(wx_id=WX_id, msg_id=Msg_id))
    # res = asyncio.get_event_loop().run_until_complete(remove_star(wx_id=WX_id, msg_id=Msg_id))
    res = asyncio.get_event_loop().run_until_complete(get_user_star_list(wx_id=WX_id))
    print(res)

