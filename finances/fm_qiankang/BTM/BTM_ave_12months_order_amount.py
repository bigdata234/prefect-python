# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 17:28
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_ave_12months_order_amount.py
# @Software: PyCharm

'''eof
name:最近一年月均订烟额
code:BTM_ave_12months_order_amount
tableName:
columnName:
groups:烟商
dependencies:BTM
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
最近一年月均订烟额
    将最近一年的每个月的订烟额求和，再除以12

字段说明:
    企业名称: BTM  indentMoney  indentDate
'''

last_year_months_list = [(datetime.datetime.now() - pd.tseries.offsets.DateOffset(months=i)).strftime('%Y-%m-%d')[:7] \
                    for i in [12 , 0]]

def BTM_ave_12months_order_amount():
    null_type_list = ['', None, 'null', '/', 'Null']
    money_list = [float(0)]
    try:
        if BTM.has_key('indent') and \
                BTM['indent'] not in null_type_list \
                and len(BTM['indent']) >= 1:
            for i in BTM['indent']:
                if i.has_key('indentDate') and \
                        i['indentDate'] not in null_type_list and \
                        i.has_key('indentMoney')  and \
                        i['indentMoney'] not in null_type_list and \
                        i['indentDate'] >= last_year_months_list[0] + "-01" and \
                        i['indentDate'] < last_year_months_list[-1] + "-01":
                    money_list.append(float(i['indentMoney']))
            return round(sum(money_list)/float(12) , 4)
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result =  BTM_ave_12months_order_amount()