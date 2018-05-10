# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:50
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_CardCnt.py
# @Software: PyCharm

'''eof
name:信用卡账户数
code:IC_CardCnt
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
信用卡账户数
    ICRCreditCue CardCnt
'''

def IC_CardCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRCreditCue') and \
                IC['ICRCreditCue'] not in null_type_list and \
                len(IC['ICRCreditCue']) == 1 and \
                IC['ICRCreditCue'][0].has_key('CardCnt') and \
                IC['ICRCreditCue'][0]['CardCnt'] not in null_type_list:
            return int(IC['ICRCreditCue'][0]['CardCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_CardCnt()