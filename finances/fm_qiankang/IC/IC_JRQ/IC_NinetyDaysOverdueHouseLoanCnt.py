# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 16:28
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_NinetyDaysOverdueHouseLoanCnt.py
# @Software: PyCharm

'''eof
name:90天以上购房贷款逾期笔数
code:IC_NinetyDaysOverdueHouseLoanCnt
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
90天以上购房贷款逾期笔数
    从逾期(透支)信息汇总（ICROverdueSummary）提取（NinetyDaysOverdueHouseLoanCnt）字段
'''

def IC_NinetyDaysOverdueHouseLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICROverdueSummary') and \
                IC['ICROverdueSummary'] not in null_type_list and \
                len(IC['ICROverdueSummary']) == 1 and \
                IC['ICROverdueSummary'][0].has_key('NinetyDaysOverdueHouseLoanCnt') and \
                IC['ICROverdueSummary'][0]['NinetyDaysOverdueHouseLoanCnt'] not in null_type_list:
            return int(IC['ICROverdueSummary'][0]['NinetyDaysOverdueHouseLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_NinetyDaysOverdueHouseLoanCnt()