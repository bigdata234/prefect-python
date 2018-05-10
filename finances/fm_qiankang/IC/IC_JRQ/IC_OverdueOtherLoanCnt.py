# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:21
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_OverdueOtherLoanCnt.py
# @Software: PyCharm

'''eof
name:其他贷款逾期笔数
code:IC_OverdueOtherLoanCnt
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
其他贷款逾期笔数
    从逾期(透支)信息汇总（ICROverdueSummary）提取（OverdueOtherLoanCnt）字段
'''

def IC_OverdueOtherLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICROverdueSummary') and \
                IC['ICROverdueSummary'] not in null_type_list and \
                len(IC['ICROverdueSummary']) == 1 and \
                IC['ICROverdueSummary'][0].has_key('OverdueOtherLoanCnt') and \
                IC['ICROverdueSummary'][0]['OverdueOtherLoanCnt'] not in null_type_list:
            return int(IC['ICROverdueSummary'][0]['OverdueOtherLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_OverdueOtherLoanCnt()