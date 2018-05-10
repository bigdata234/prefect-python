# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:58
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_UdestroyCardAccountCnt.py
# @Software: PyCharm

'''eof
name:未销户信用卡账户数
code:IC_UdestroyCardAccountCnt
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
未销户信用卡账户数
    ICRUnpaidLoanCredit UdestroyCardAccountCnt
'''

def IC_UdestroyCardAccountCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRUnpaidLoanCredit') and \
                IC['ICRUnpaidLoanCredit'] not in null_type_list and \
                len(IC['ICRUnpaidLoanCredit']) == 1 and \
                IC['ICRUnpaidLoanCredit'][0].has_key('UdestroyCardAccountCnt') and \
                IC['ICRUnpaidLoanCredit'][0]['UdestroyCardAccountCnt'] not in null_type_list:
            return int(IC['ICRUnpaidLoanCredit'][0]['UdestroyCardAccountCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_UdestroyCardAccountCnt()