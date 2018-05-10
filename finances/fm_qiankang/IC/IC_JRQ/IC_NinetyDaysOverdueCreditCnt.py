# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 16:26
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_NinetyDaysOverdueCreditCnt.py
# @Software: PyCharm

'''eof
name:90天以上信用卡逾期账户数
code:IC_NinetyDaysOverdueCreditCnt
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
90天以上信用卡逾期账户数
    从逾期(透支)信息汇总（ICROverdueSummary）提取（NinetyDaysOverdueCreditCnt）字段
'''

def IC_NinetyDaysOverdueCreditCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICROverdueSummary') and \
                IC['ICROverdueSummary'] not in null_type_list and \
                len(IC['ICROverdueSummary']) == 1 and \
                IC['ICROverdueSummary'][0].has_key('NinetyDaysOverdueCreditCnt') and \
                IC['ICROverdueSummary'][0]['NinetyDaysOverdueCreditCnt'] not in null_type_list:
            return int(IC['ICROverdueSummary'][0]['NinetyDaysOverdueCreditCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_NinetyDaysOverdueCreditCnt()