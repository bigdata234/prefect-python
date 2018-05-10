# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 15:40
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_GuaranOtherLoanCnt.py
# @Software: PyCharm


'''eof
name:为他人其他贷款担保笔数
code:IC_GuaranOtherLoanCnt
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
为他人其他贷款担保笔数
    从对外担保信息汇总（ICRGuaranSummary）提取（GuaranOtherLoanCnt）字段
'''

def IC_GuaranOtherLoanCnt():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRGuaranSummary') and \
                IC['ICRGuaranSummary'] not in null_type_list and \
                len(IC['ICRGuaranSummary']) == 1 and \
                IC['ICRGuaranSummary'][0].has_key('GuaranOtherLoanCnt') and \
                IC['ICRGuaranSummary'][0]['GuaranOtherLoanCnt'] not in null_type_list:
            return int(IC['ICRGuaranSummary'][0]['GuaranOtherLoanCnt'])
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_GuaranOtherLoanCnt()