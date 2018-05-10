# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 13:28
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_1year_SumLoanBalance.py
# @Software: PyCharm

'''eof
name:申请人一年内到期贷款余额
code:IC_1year_SumLoanBalance
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
申请人一年内到期贷款余额
    近一年的LoanBalance（贷款本金余额）求和
    ICRLoanInfo	贷款本金余额 LoanBalance
    报告生成日期 : ICRHeader QueryTime
    贷款信息表中若贷款到期日期(LoanEndDate) < 报告生成日期+12月,本金余额求和
'''

def IC_1year_SumLoanBalance():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRHeader') and IC['ICRHeader'] not in null_type_list and \
                len(IC['ICRHeader']) >= 1 and IC['ICRHeader'][0].has_key('QueryTime') and \
                IC['ICRHeader'][0]['QueryTime'] not in null_type_list:
            cur_date = time.strptime( str(IC['ICRHeader'][0]['QueryTime']) , "%Y-%m-%d")
            y , m , d = cur_date[0:3]
            after_1_year = (datetime.datetime(y,m,d) + pd.tseries.offsets.DateOffset(months=12)).strftime('%Y-%m-%d')
        else:
            after_1_year = u'缺失值'
    except:
        after_1_year = u'缺失值'
    try:
        if IC.has_key('ICRLoanInfo') and \
                IC['ICRLoanInfo'] not in null_type_list and \
                len(IC['ICRLoanInfo']) >= 1 and after_1_year != u'缺失值':
            for i in IC['ICRLoanInfo']:
                if i.has_key('LoanBalance') and \
                        i['LoanBalance'] not in null_type_list and \
                        i.has_key('LoanEndDate') and i['LoanEndDate'] not in null_type_list and i['LoanEndDate'] < after_1_year:
                    res_list.append(float(i['LoanBalance']))
            if len(res_list) >= 1:
                return round(sum(res_list) , 4)
            else:
                return round(float(0) , 4)
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result  = IC_1year_SumLoanBalance()
