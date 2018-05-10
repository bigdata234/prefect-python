# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 13:41
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_order_ciga_acti_month_num.py
# @Software: PyCharm

'''eof
name:最近一年订烟活跃月份数
code:BTM_order_ciga_acti_month_num
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
最近一年订烟活跃月份数
首先判断近一年的每个月是否为订烟活跃月(订单非0为活跃月)，然后将是的进行累加。

字段说明:
    企业名称: BTM indent indentDate  indentAccount 订单数量
'''
last_year_months_list = [(datetime.datetime.now() - pd.tseries.offsets.DateOffset(months=i)).strftime('%Y-%m-%d')[:7] \
                    for i in xrange(12 , -1 , -1)]

def BTM_order_ciga_acti_month_num():
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
        return len(set(month_list))
    else:
        return u'缺失值'

result = BTM_order_ciga_acti_month_num()