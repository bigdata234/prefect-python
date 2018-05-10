# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 12:59
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Sum_OverdueCnt.py
# @Software: PyCharm

'''eof
name:发生过逾期的账户数之和
code:IC_Sum_OverdueCnt
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
发生过逾期的账户数之和
     sum(OverdueCreditCnt(信用卡逾期账户数)+OverdueHouseLoanCnt(购房贷款逾期笔数)+OverdueOtherLoanCnt(其他贷款逾期笔数))
     ICROverdueSummary OverdueCreditCnt OverdueHouseLoanCnt OverdueOtherLoanCnt
'''

def IC_Sum_OverdueCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICROverdueSummary') and \
                IC['ICROverdueSummary'] not in null_type_list and \
                len(IC['ICROverdueSummary']) == 1:
            if IC['ICROverdueSummary'][0].has_key('OverdueCreditCnt') and \
                    IC['ICROverdueSummary'][0]['OverdueCreditCnt'] not in null_type_list:
                res_list.append(int(IC['ICROverdueSummary'][0]['OverdueCreditCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICROverdueSummary'][0].has_key('OverdueHouseLoanCnt') and \
                    IC['ICROverdueSummary'][0]['OverdueHouseLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICROverdueSummary'][0]['OverdueHouseLoanCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICROverdueSummary'][0].has_key('OverdueOtherLoanCnt') and \
                    IC['ICROverdueSummary'][0]['OverdueOtherLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICROverdueSummary'][0]['OverdueOtherLoanCnt']))
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

result = IC_Sum_OverdueCnt()






















