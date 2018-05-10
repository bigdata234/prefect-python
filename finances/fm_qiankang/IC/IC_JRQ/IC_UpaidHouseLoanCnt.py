# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:32
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_UpaidHouseLoanCnt.py
# @Software: PyCharm

'''eof
name:未结清购房贷款笔数
code:IC_UpaidHouseLoanCnt
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
未结清购房贷款笔数
    从未结清信贷信息汇总（ICRUnpaidLoanCredit）提取（UpaidHouseLoanCnt）字段
'''

def IC_UpaidHouseLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRUnpaidLoanCredit') and \
                IC['ICRUnpaidLoanCredit'] not in null_type_list and \
                len(IC['ICRUnpaidLoanCredit']) == 1 and \
                IC['ICRUnpaidLoanCredit'][0].has_key('UpaidHouseLoanCnt') and \
                IC['ICRUnpaidLoanCredit'][0]['UpaidHouseLoanCnt'] not in null_type_list:
            return int(IC['ICRUnpaidLoanCredit'][0]['UpaidHouseLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_UpaidHouseLoanCnt()