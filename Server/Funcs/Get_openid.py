"""
创建日期：2022.3.25
作者：乔毅
文件名：Get_openid
功能：获取微信用户的openid
备注：代码中被注释掉的print()为 测试时调用，控制台输出没有实际意义
"""

import requests


def get_openid(js_code: str) -> str:
    """
    函数名：get_openid
    作用：获取用户openid
    :param js_code:前端获取的js_code
    :return:openid
    """
    appid = "wx6edc1ebcbea85340"
    secret = "54bf432eabddb286f5922895918fd0e3"
    url = 'https://api.weixin.qq.com/\
    sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'\
        .format(appid=appid, secret=secret, code=js_code)
    res = requests.get(url)
    openid = res.json().get('openid')
    # session_key = res.json().get('session_key')
    return str(openid)
