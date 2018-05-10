# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 21:57
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_Cont_not_order_month_num.py
# @Software: PyCharm


'''eof
name:最近一年最大连续未订烟月份数
code:BTM_Cont_not_order_month_num
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
import datetime , time

reload(sys)
sys.setdefaultencoding('utf-8')

'''
最近一年最大连续未订烟月份数
    把最近一年连续订单额为0的月数

字段说明:
    企业名称: BTM indent indentDate  indentAccount 订单数量

'''

last_year_months_list = [(datetime.datetime.now() - pd.tseries.offsets.DateOffset(months=i)).strftime('%Y-%m-%d')[:7] \
                    for i in xrange(12 , -1 , -1)]

def BTM_Cont_not_order_month_num():
    null_type_list = ['', None, 'null', '/' , 'Null']
    active_month_dict ={}
    month_list = []
    try:
        if BTM.has_key('indent') and \
                BTM['indent'] not in null_type_list and \
                len(BTM['indent']) >= 1:
            for i in BTM['indent']:
                if i.has_key('indentDate') and \
                        i['indentDate'] not in null_type_list and \
                        i.has_key('indentAccount') and \
                        i['indentAccount'] not in null_type_list and \
                        i['indentDate'] >= last_year_months_list[0] + "-01" and \
                        i['indentDate'] < last_year_months_list[-1] + "-01":
                    active_month_dict.update({i['indentDate'] : i['indentAccount']})
        else:
            active_month_dict.update({})
    except:
        active_month_dict.update({})

    if active_month_dict:
        month_list = [j[:7] for j in active_month_dict if float(active_month_dict[j]) > 0]
        not_active_month = list(set(last_year_months_list[:12]) - set(month_list))
        not_active_month.sort()
        month_index = [0]
        if not_active_month:
            for m in xrange(len(not_active_month) - 1):
                cur_month = datetime.datetime.strptime(not_active_month[m], '%Y-%m')
                after_month = (cur_month + pd.tseries.offsets.DateOffset(months=1)).strftime('%Y-%m-%d')[:7]
                if after_month != not_active_month[m + 1]:
                    month_index.append(m + 1)
            month_index.append(len(not_active_month))
            return max([month_index[k + 1] - month_index[k] for k in xrange(len(month_index) - 1)])
        else:
            return 0
    else:
        return 12

result = BTM_Cont_not_order_month_num()

