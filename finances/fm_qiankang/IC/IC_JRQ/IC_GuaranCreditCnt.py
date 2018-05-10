# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:36
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_GuaranCreditCnt.py
# @Software: PyCharm

'''eof
name:为他人信用卡担保数量
code:IC_GuaranCreditCnt
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
为他人信用卡担保数量 
    对外担保信息汇总（ICRGuaranSummary）提取（GuaranCreditCnt）字段
'''

def IC_GuaranCreditCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRGuaranSummary') and \
                IC['ICRGuaranSummary'] not in null_type_list and \
                len(IC['ICRGuaranSummary']) == 1 and \
                IC['ICRGuaranSummary'][0].has_key('GuaranCreditCnt') and \
                IC['ICRGuaranSummary'][0]['GuaranCreditCnt'] not in null_type_list:
            return int(IC['ICRGuaranSummary'][0]['GuaranCreditCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_GuaranCreditCnt()