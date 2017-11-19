# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
-------------------------------------------------
   File Name: dxut.py
   Author: Dexter Chen
   Date：2017-11-14
-------------------------------------------------
"""

from __future__ import division
import sys
import os
import random
import time
import datetime
from multiprocessing import Pool
from colorama import init, Fore, Back, Style

dict_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
    'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
    'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
    'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
    'UCWEB7.0.2.37/28/999',
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
    'UCWEB7.0.2.37/28/999',
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'
]

dict_header = {
    'User-Agent': "",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "max-age=0",
}

dict_floor_type = {
    u"高层": "H",
    u"中层": "M",
    u"低层": "L"
}

dict_color_code = {
    "info":(Back.GREEN + Fore.BLACK),
    "important":(Back.BLACK + Fore.WHITE),
    "error":(Back.RED + Fore.LIGHTWHITE_EX),
    "notice":(Back.YELLOW + Fore.BLACK),
    "debug":(Back.LIGHTCYAN_EX + Fore.BLACK),
    "time_stamp":(Back.LIGHTBLACK_EX + Fore.LIGHTWHITE_EX)
}

exp_email = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"  # 所有email地址
exp_html = "</?\w+[^>]*>\s?"  # 所有html标签


# client = MongoClient('mongodb://localhost:27017/') 


# 关于网络
def random_header():
    """随机返回一个header"""
    dict_header["User-Agent"] = random.choice(dict_agent)
    return dict_header

# 关于任务


def multi_tasking(process_number, function_name, list_varible):
    """最简单的多线程任务"""
    pool = Pool(process_number)  # 实例化进程池
    pool.map(function_name, list_varible)
    pool.close()  # 关闭进程池
    pool.join()  # 等待所有进程结束

# 关于文本操作


def dict_replace(data_to_replace, dict_replace):
    """使用dict进行文本替换"""
    for (k, j) in dict_replace.items():
        data_replaced = data_to_replace.replace(k, j)
    return data_replaced


def regexp_subtract(data_to_replace, exp_subtract, new_data=""):
    """用正则表达式替换/删除匹配内容"""
    re_content = re.compile(exp_subtract)  # 清除所有html标签
    data_to_replace = re_content.sub(new_data, data_to_replace)
    return data_to_replace


# 关于文件操作
def current_dir():
    """获取当前脚本路径"""
    current_path = sys.path[0]
    return current_path


# 时间相关
def current_time(type="full", delta_min=0):
    """获取当前time_str, type:[full,year,date,time]"""
    if type == "full":
        time_format = '%Y-%m-%d %X'
    if type == "year":
        time_format = "%Y"
    if type == "date":
        time_format = '%Y-%m-%d'
    if type == "time":
        time_format = "%X"
    current_time = datetime.datetime.now()
    time = current_time + datetime.timedelta(minutes=delta_min)
    return time.strftime(time_format)


def time_str_interval(earlier_time_str, later_time_str, time_unit="hour"):
    """计算两个time_str的间隔,time_unit:[second,minute,hour,day]"""
    earlier_time_object = datetime.datetime.strptime(earlier_time_str, "%Y-%m-%d %X")
    later_time_object = datetime.datetime.strptime(later_time_str, "%Y-%m-%d %X")
    duration_delta = later_time_object - earlier_time_object
    duration_in_seconds = int(duration_delta.total_seconds())
    if time_unit == "second":
        return duration_in_seconds
    elif time_unit == "minute":
        return float(duration_in_seconds / 60)
    elif time_unit == "hour":
        return float(duration_in_seconds / 3600)
    elif time_unit == "day":
        return float(duration_in_seconds / 86400)
    else:
        return "error"

# 消息相关
def msg(who, identifier, action, result, info_type, *args):
    '''集中处理各种信息[log,info,stat,debug]'''
    for fn in args:
        fn(ut.time_str("full"), who, identifier, action, result, info_type)

def log(who, identifier, action, result, info_type):
    """记录日志"""
    data = {"ctime": when, "who": who, "identifier": identifier, "action": action, "result": result, "info_type": info_type}
    get_db('log').insert_one(data)


def debug(who, identifier, action, result, info_type):
    """用于调试"""
    data = {"ctime": when, "who": who, "identifier": identifier, "what": result}
    get_db('debug').insert_one(data)


def info(when, who, identifier, action, result, info_type):
    """用于显示"""
    add_new_display(when, who, identifier, action, result, info_type)



def stat(when, who, identifier, action, result, info_type):  # 用于统计的信息
    if result == "succ":
        if who == "index page":
            stats.success_sum_page += 1
        elif who == "record":
            stats.success_record += 1
        elif who == "pmid":
            stats.success_pmid += 1
            stats.c_skipped_pmid = 0
        elif who == "task":
            if result == "start":
                stats.task_start = ut.time_str("full")
            elif result == "finish":
                stats.task_finish = ut.time_str("full")


def get_db(data_type):
    if data_type in ["content", "log"]:
        database = client["test"][data_type]
    else:
        database = "error"
    return database


if __name__ == '__main__':
    print time_str_interval("1984-05-07 23:30:00", "1984-05-17 13:32:44")
