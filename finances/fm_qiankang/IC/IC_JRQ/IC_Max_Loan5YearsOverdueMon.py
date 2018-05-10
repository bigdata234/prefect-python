# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 18:12
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Max_Loan5YearsOverdueMon.py
# @Software: PyCharm

'''eof
name:贷款5年内逾期月份数最大值
code:IC_Max_Loan5YearsOverdueMon
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
贷款5年内逾期月份数最大值
    贷款信息（ICRLoanInfo）提取贷款当前逾期金额（Loan5YearsOverdueMon）字段
'''

def IC_Max_Loan5YearsOverdueMon():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRLoanInfo') and \
                IC['ICRLoanInfo'] not in null_type_list and \
                len(IC['ICRLoanInfo']) >= 1:
            for i in IC['ICRLoanInfo']:
                if i.has_key('Loan5YearsOverdueMon') and \
                        i['Loan5YearsOverdueMon'] not in null_type_list:
                    res_list.append(int(i['Loan5YearsOverdueMon']))
            if len(res_list) >= 1:
                return max(res_list)
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_Max_Loan5YearsOverdueMon()