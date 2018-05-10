# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 18:07
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Max_CardCurrOverdueAmt.py
# @Software: PyCharm


'''eof
name:贷记卡当前逾期金额最大值
code:IC_Max_CardCurrOverdueAmt
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
贷记卡当前逾期金额最大值
    贷款信息（ICRCardInfo）提取贷款当前逾期金额（CardCurrOverdueAmt）字段
'''

def IC_Max_CardCurrOverdueAmt():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRCardInfo') and \
                IC['ICRCardInfo'] not in null_type_list and \
                len(IC['ICRCardInfo']) >= 1:
            for i in IC['ICRCardInfo']:
                if i.has_key('CardCurrOverdueAmt') and \
                        i['CardCurrOverdueAmt'] not in null_type_list:
                    res_list.append(float(i['CardCurrOverdueAmt']))
            if len(res_list) >= 1:
                return round(max(res_list) , 4)
            else:
                return round(float(0) , 4)
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_Max_CardCurrOverdueAmt()