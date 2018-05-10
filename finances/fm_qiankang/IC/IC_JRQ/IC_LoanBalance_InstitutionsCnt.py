# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 13:12
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_LoanBalance_InstitutionsCnt.py
# @Software: PyCharm

'''eof
name:未结清贷款机构数
code:IC_LoanBalance_InstitutionsCnt
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
未结清贷款机构数
     近一年的LoanBalance（贷款本金余额）非零的机构去重求和
     ICRLoanInfo	贷款本金余额	LoanBalance
     ICRLoanInfo	贷款贷款机构	LoanFinanceOrg
'''

def IC_LoanBalance_InstitutionsCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRLoanInfo') and IC['ICRLoanInfo'] not in null_type_list and len(IC['ICRLoanInfo']) >= 1:
            for i in IC['ICRLoanInfo']:
                if i.has_key('LoanBalance') and i['LoanBalance'] not in null_type_list and \
                        i.has_key('LoanFinanceOrg') and i['LoanFinanceOrg'] not in null_type_list and \
                        float(i['LoanBalance']) > float(0):
                    res_list.append(i['LoanFinanceOrg'])
            return len(set(res_list))
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result  = IC_LoanBalance_InstitutionsCnt()



