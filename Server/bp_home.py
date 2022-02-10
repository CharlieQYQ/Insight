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


@bp_home.route('/msg_search')
async def message_search(request):
    logger.info(request)
    try:
        query = str(request.args.get('msg', '')).strip()
        wx_id = int(request.args.get('id', ''))
        result = await msg_search(query=query, flag=0.5, wx_id=wx_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)


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


@bp_home.route('/query_record')
async def history_query(request):
    logger.info(request)
    try:
        wx_id = int(request.args.get('id', ''))
        result = await query_record(wx_id=wx_id)
        logger.info(result)
        return json(result, ensure_ascii=False)
    except Exception as e:
        logger.error(e)
        return text(e)

