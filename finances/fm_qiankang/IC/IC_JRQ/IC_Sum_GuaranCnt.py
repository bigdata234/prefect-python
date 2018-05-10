# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 13:07
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Sum_GuaranCnt.py
# @Software: PyCharm


'''eof
name:为他人担保笔数
code:IC_Sum_GuaranCnt
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
担保笔数之和
      sum(GuaranCreditCnt(为他人信用卡担保数量)+GuaranHouseLoanCnt(为他人购房贷款担保笔数)+GuaranOtherLoanCnt(为他人其他贷款担保笔数))
      ICRGuaranSummary	为他人信用卡担保数量	GuaranCreditCnt
      ICRGuaranSummary	为他人购房贷款担保笔数	GuaranHouseLoanCnt
      ICRGuaranSummary	为他人其他贷款担保笔数	GuaranOtherLoanCnt
'''

def IC_Sum_GuaranCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRGuaranSummary') and \
                IC['ICRGuaranSummary'] not in null_type_list and \
                len(IC['ICRGuaranSummary']) == 1:
            if IC['ICRGuaranSummary'][0].has_key('GuaranCreditCnt') and \
                    IC['ICRGuaranSummary'][0]['GuaranCreditCnt'] not in null_type_list:
                res_list.append(int(IC['ICRGuaranSummary'][0]['GuaranCreditCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICRGuaranSummary'][0].has_key('GuaranHouseLoanCnt') and \
                    IC['ICRGuaranSummary'][0]['GuaranHouseLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICRGuaranSummary'][0]['GuaranHouseLoanCnt']))
            else:
                res_list.append(u'缺失值')
            if IC['ICRGuaranSummary'][0].has_key('GuaranOtherLoanCnt') and \
                    IC['ICRGuaranSummary'][0]['GuaranOtherLoanCnt'] not in null_type_list:
                res_list.append(int(IC['ICRGuaranSummary'][0]['GuaranOtherLoanCnt']))
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

result = IC_Sum_GuaranCnt()