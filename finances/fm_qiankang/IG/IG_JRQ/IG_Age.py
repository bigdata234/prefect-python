# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 14:46
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IG_Age.py
# @Software: PyCharm

'''eof
name:申请人年龄
code:IG_Age
tableName:
columnName:
groups:个人通用
dependencies:EG
type:常用指标
datasourceType:在线指标
description:
eof'''

import sys
import pandas as pd
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

'''
申请人年龄
    申请日期 : 当前日期 
    提取申请人身份证号(legalPersonIdCard)7-14位转化为日期格式，YEAR(申请日期 - 生日)，保留2位小数
'''

def IG_Age():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if ratingRequest['legalPersonIdCard'] not in null_type_list and \
                len(ratingRequest['legalPersonIdCard']) == 18:
            brith_date_str = ratingRequest['legalPersonIdCard'][6: 14]
            brith_date = datetime.datetime.strptime(brith_date_str, '%Y%m%d')
            range_days =  (datetime.datetime.now() - brith_date).days
            return int(round(range_days/float(365) , 0))
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IG_Age()