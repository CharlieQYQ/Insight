"""
创建日期：2021.9.3
作者：乔毅
文件名：bp_home.py
功能：sanic后端服务蓝图
"""

# 导入库
import sys
from sanic import Blueprint
from sanic.response import json, text
from Funcs.Message_search import msg_search
from Funcs.Message_info import msg_info_search
from Funcs.Query_record import query_record
from Funcs.Get_openid import get_openid
from Funcs.User_star import add_star, get_user_star_list, remove_star
import logging
import datetime
# import asyncio

# 配置日志
# 获取当前时间以命名日志文件
time_str = datetime.datetime.now().strftime('%Y-%m-%d')
# 创建日志
logger = logging.getLogger(__name__)
# 设置日志等级
logger.setLevel(level=logging.INFO)
# 设置解决器
handler = logging.FileHandler("../Logs/%s.log" % time_str)
handler.setLevel(logging.INFO)
# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 新建蓝图
bp_home = Blueprint('bp_home')
# 开启异步特性
enable_async = sys.version_info >= (3, 6)


# 设置路由
@bp_home.route('/')
async def index(request):
    return text('index page')


# 信息检索
@bp_home.route('/msg_search')
async def message_search(request):
    logger.info(request)
    try:
        query = str(request.args.get('msg', '')).strip()
        wx_id = str(request.args.get('id', '')).strip()
        result = await msg_search(query=query, flag=0.01, wx_id=wx_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)


# 案例信息查询
@bp_home.route('/msg_info')
async def message_info(request):
    logger.info(request)
    try:
        msg_id = int(request.args.get('id', ''))
        result = await msg_info_search(msg_id=msg_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)


# 查询历史记录
@bp_home.route('/query_record')
async def history_query(request):
    logger.info(request)
    try:
        wx_id = str(request.args.get('id', '')).strip()
        result = await query_record(wx_id=wx_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)


# 添加用户收藏
@bp_home.route('/add_star')
async def user_add_star(request):
    logger.info(request)
    try:
        wx_id = str(request.args.get('id', '')).strip()
        msg_id = int(request.args.get('msg_id', ''))
        result = await add_star(wx_id=wx_id, msg_id=msg_id)
        logger.info(result)
        return json(result)
    except Exception as e:
        logger.error(e)
        return text(e)


# 删除用户收藏
@bp_home.route('/remove_star')
async def user_remove_star(request):
    logger.info(request)
    try:
        wx_id = str(request.args.get('id', '')).strip()
        msg_id = int(request.args.get('msg_id', ''))
        result = await remove_star(wx_id=wx_id, msg_id=msg_id)
        logger.info(result)
        return json(result)
    except Exception as e:
        logger.error(e)
        return text(e)


# 获取用户收藏列表
@bp_home.route('/get_star')
async def get_star(request):
    logger.info(request)
    try:
        wx_id = str(request.args.get('id', '')).strip()
        result = await get_user_star_list(wx_id=wx_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)


# 获取用户openid
@bp_home.route('/get_openid')
async def get_openid(request):
    logger.info(request)
    try:
        jscode = str(request.args.get('jscode', '')).strip()
        result = await get_openid(js_code=jscode)
        return text(result)
    except Exception as e:
        logger.error(e)
        return False


