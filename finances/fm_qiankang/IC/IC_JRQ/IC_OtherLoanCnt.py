# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 12:15
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_OtherLoanCnt.py
# @Software: PyCharm

'''eof
name:其他贷款笔数
code:IC_OtherLoanCnt
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
其他贷款笔数
    从信用提示（ICRCreditCue）提取（OtherLoanCnt）字段
'''

def IC_OtherLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRCreditCue') and \
                IC['ICRCreditCue'] not in null_type_list and \
                len(IC['ICRCreditCue']) == 1 and \
                IC['ICRCreditCue'][0].has_key('OtherLoanCnt') and \
                IC['ICRCreditCue'][0]['OtherLoanCnt'] not in null_type_list:
            return int(IC['ICRCreditCue'][0]['OtherLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_OtherLoanCnt()