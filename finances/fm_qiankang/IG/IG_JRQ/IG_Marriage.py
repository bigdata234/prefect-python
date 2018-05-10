# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 15:21
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IG_Marriage.py
# @Software: PyCharm

'''eof
name:婚姻状况
code:IG_Marriage
tableName:
columnName:
groups:个人征信
dependencies:IC
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
婚姻状况:
    ICRIdentity MaritalState
'''

def IG_Marriage():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRIdentity') and \
                IC['ICRIdentity'] not in null_type_list and \
                len(IC['ICRIdentity']) == 1 and \
                IC['ICRIdentity'][0].has_key('MaritalState') and \
                IC['ICRIdentity'][0]['MaritalState'] not in null_type_list:
            return IC['ICRIdentity'][0]['MaritalState']
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IG_Marriage()