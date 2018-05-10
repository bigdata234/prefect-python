# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 12:19
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_CreditCnt.py
# @Software: PyCharm

'''eof
name:贷款及其他账户总数
code:IC_CreditCnt
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
贷款及其他账户总数
    ICRCreditCue HouseLoanCnt , 
    sum(个人购房贷款笔数(HouseLoanCnt)+信用卡账户数(CardCnt)+其他贷款笔数(OtherLoanCnt))
'''

def IC_CreditCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRCreditCue') and \
                IC['ICRCreditCue'] not in null_type_list and \
                len(IC['ICRCreditCue']) == 1:
            if IC['ICRCreditCue'][0].has_key('HouseLoanCnt') and \
                    IC['ICRCreditCue'][0]['HouseLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICRCreditCue'][0]['HouseLoanCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICRCreditCue'][0].has_key('CardCnt') and \
                    IC['ICRCreditCue'][0]['CardCnt'] not in null_type_list:
                res_list.append(int(IC['ICRCreditCue'][0]['CardCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICRCreditCue'][0].has_key('OtherLoanCnt') and \
                    IC['ICRCreditCue'][0]['OtherLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICRCreditCue'][0]['OtherLoanCnt']))
            else:
                res_list.append(u'缺失值')

            if len(res_list) >=1:
                res_non_list = [i for i in res_list if i != u'缺失值']
                if len(res_non_list) >= 1:
                    return sum(res_non_list)
                else:
                    return 0
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_CreditCnt()