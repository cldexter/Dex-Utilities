# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name: screen.py
   Description: 在屏幕上打印的处理
   Author: Dexter Chen
   Date：2017-09-01
-------------------------------------------------
   Development Note：
   1.最上方显示统计数据，状态数据
   2.接收信息，根据信息种类，选择打印颜色与存留时间
-------------------------------------------------

"""

from __future__ import division
import sys
import os
import time
import math
from colorama import init, Fore, Back, Style
import dxut as ut


reload(sys)
sys.setdefaultencoding('utf8')

init(autoreset=True)

color_code = {
    "info": (Back.GREEN + Fore.BLACK),
    "important": (Back.BLACK + Fore.WHITE),
    "error": (Back.RED + Fore.LIGHTWHITE_EX),
    "notice": (Back.YELLOW + Fore.BLACK),
    "debug": (Back.LIGHTCYAN_EX + Fore.BLACK),
    "time_stamp": (Back.LIGHTBLACK_EX + Fore.LIGHTWHITE_EX)
}

message_set = []


def add_new_display(when, who, identifier, action, result, info_type):
    print(color_code["time_stamp"] + " [" + when + "] "),
    print(color_code[info_type] + " [" + info_type + "] "),
    print who, identifier, action, result


def get_window_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return rows, columns


class Screen:
    def __init__(self, project_name):
        self.rows = int(os.popen('stty size', 'r').read().split()[0])
        self.columns = int(os.popen('stty size', 'r').read().split()[1])
        self.project_name = project_name
        self.title_box_length = 20
        self.status_title_length = 12
        self.status_value_length = 12
        self.status_box_length = 30
        # self.status_column = math.floor(self.columns / self.status_box_length)
        self.status_column = 2


    def clean_screen(self):
        os.system("clear")

    def title(self, title_list):
        title_str = "|"
        value_str = "|"
        for item in title_list:
            if len(item[0]) > self.title_box_length:
                title = item[0][0:self.title_box_length - 1]
            else:
                title = item[0].center(self.title_box_length, " ")
            if len(item[1]) > self.title_box_length:
                value = item[1][0:self.title_box_length - 1]
            else:
                value = item[1].center(self.title_box_length, " ")
            title_str = title_str + title + "|"
            value_str = value_str + value + "|"
        title_box_number = len(title_list)
        title_bar_length = title_box_number * (self.title_box_length + 1) + 1
        title_spacer_l_length = int((self.columns - title_bar_length) / 2)
        title_spacer_r_length = self.columns - \
            (title_spacer_l_length + title_bar_length)
        print " " * title_spacer_l_length + (Back.LIGHTYELLOW_EX + Fore.BLACK) + title_str
        print (Fore.YELLOW) + "-" * title_spacer_l_length + \
            value_str + "-" * title_spacer_r_length
        print " " * title_spacer_l_length + (Fore.YELLOW) + "-" * title_bar_length

    def status(self, status_list):
        titles = []
        values = []
        max_title_length = 0
        max_value_length = 0
        status_spacer_lengths = []
        for status in status_list:
            title_length = len(status[0])
            value_length = len(status[1])
            if title_length > max_title_length:
                max_title_length = title_length
            if value_length > max_value_length:
                max_value_length = value_length
            if title_length >= self.status_title_length:
                title = status[0][0:self.status_title_length - 1]
            else:
                title = status[0]
            if value_length >= self.status_value_length:
                value = status[1][0:self.status_value_length - 1]
            else:
                value = status[1]
            status_spacer_length = self.status_box_length - len(title) - len(value) - 2
            titles.append(title)
            values.append(value)
            status_spacer_lengths.append(status_spacer_length)
        status_rows = int(math.ceil(len(status_list) / self.status_column))
        print status_rows
        status_column_spacer_number = self.status_column - 1
        # status_spacer_length = int((self.columns - ((self.status_title_length +
                                                    #  self.status_value_length + 1) * self.status_column)) / status_column_spacer_number)
        status_str_list = []
        i = 1  # 行
        j = 1  # 列
        k = 0  # 个
        while i <= status_rows:
            print "i: " + str(i)
            status_str = ""
            while j <= self.status_column and k < len(status_list):
                status_str = status_str + titles[k] + ": " + values[k] + " " * status_spacer_lengths[k]
                k += 1
                j += 1
                print "k: " + str(k)
                print "j: " + str(j)
            print status_str
            i += 1


if __name__ == '__main__':
    # add_new_display("10:10:10", "dexter", "121131311", "is here", "succ", "debug")
    # add_new_display("10:10:10", "dexter", "121131311", "is here", "succ", "notice")
    # add_new_display("10:10:10", "dexter", "121131311", "is here", "succ", "info")
    # add_new_display("10:10:10", "dexter", "121131311", "is here", "succ", "important")
    # add_new_display("10:10:10", "dexter", "121131311", "is here", "succ", "error")
    # full_screen_box()
    # time_box()
    screen = Screen("dexterisherewaiting")
    # screen.clean_screen()
    screen.title([("file name", "this is a test"),("created date", "2017-07-07")])
    screen.status([("12345678901234", "12345678901234"), ("big", "12345678901234"),
                   ("big", "city"), ("big", "12345678901234"), ("big", "city"), ("hello", "people")])
