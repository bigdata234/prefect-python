# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 17:02
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_LoanCurrOverdueAmt.py
# @Software: PyCharm

'''eof
name:贷款当前逾期金额
code:IC_LoanCurrOverdueAmt
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
贷款当前逾期金额
    贷款信息（ICRLoanInfo）提取贷款当前逾期金额（LoanCurrOverdueAmt）字段
'''

def IC_LoanCurrOverdueAmt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRLoanInfo') and \
                IC['ICRLoanInfo'] not in null_type_list and \
                len(IC['ICRLoanInfo']) >= 1:
            for i in IC['ICRLoanInfo']:
                if i.has_key('LoanCurrOverdueAmt') and \
                        i['LoanCurrOverdueAmt'] not in null_type_list:
                    res_list.append(float(i['LoanCurrOverdueAmt']))
            if len(res_list) >= 1:
                return round(sum(res_list) , 4)
            else:
                return round(float(0) , 4)
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_LoanCurrOverdueAmt()