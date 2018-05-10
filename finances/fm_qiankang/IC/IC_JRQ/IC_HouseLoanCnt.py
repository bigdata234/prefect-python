# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:46
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_HouseLoanCnt.py
# @Software: PyCharm


'''eof
name:个人购房贷款笔数
code:IC_HouseLoanCnt
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
个人购房贷款笔数
    从信用提示（ICRCreditCue）提取（HouseLoanCnt）字段
'''

def IC_HouseLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRCreditCue') and \
                IC['ICRCreditCue'] not in null_type_list and \
                len(IC['ICRCreditCue']) == 1 and \
                IC['ICRCreditCue'][0].has_key('HouseLoanCnt') and \
                IC['ICRCreditCue'][0]['HouseLoanCnt'] not in null_type_list:
            return int(IC['ICRCreditCue'][0]['HouseLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_HouseLoanCnt()