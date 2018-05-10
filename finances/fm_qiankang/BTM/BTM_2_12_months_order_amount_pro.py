# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 17:42
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_2_12_months_order_amount_pro.py
# @Software: PyCharm

'''eof
name:最近2个月订烟额占比
code:BTM_2_12_months_order_amount_pro
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
最近两个月订烟额
    将最近两个月的订烟额进行累加

字段说明:
    企业名称: BTM  indentMoney  indentDate
'''

last_year_months = [(datetime.datetime.now() - pd.tseries.offsets.DateOffset(months=i)).strftime('%Y-%m-%d')[:7] \
                    for i in [12 , 2 , 0]]

def BTM_2_12_months_order_amount_pro():
    null_type_list = ['', None, 'null', '/', 'Null']
    indent_money_list = [float(0)]
    other_month_list = [float(0)]
    try:
        if BTM.has_key('indent') and \
                BTM['indent'] not in null_type_list \
                and len(BTM['indent']) >= 1:
            last_date_list = [i['indentDate']  for i in BTM['indent'] if i.has_key('indentDate') \
                         and i['indentDate'] not in null_type_list]
            for i in BTM['indent']:
                if i.has_key('indentDate') and \
                        i['indentDate'] not in null_type_list and \
                        i.has_key('indentMoney') and \
                        i['indentMoney'] not in null_type_list:
                    if i['indentDate'] >= last_year_months[1] + "-01" and i['indentDate'] < last_year_months[2] + "-01":
                        indent_money_list.append(float(i['indentMoney']))
                    elif i['indentDate'] >= last_year_months[0] + "-01" and i['indentDate'] < last_year_months[1] + "-01":
                        other_month_list.append(float(i['indentMoney']))
            other_month_list.extend(indent_money_list)
            if sum(other_month_list) != float(0):
                return round(float(sum(indent_money_list))/float(sum(other_month_list)) , 4)
            else:
                return u'缺失值'
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_2_12_months_order_amount_pro()