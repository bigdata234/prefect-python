# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 16:58
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_cigarette_order_increase_half_year.py
# @Software: PyCharm


'''eof
name:最近半年订烟增长率
code:BTM_cigarette_order_increase_half_year
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
最近半年订烟增长率低于一定比例
    最近6个月订单额减去上6个月订单额，比上上6个月订单额

字段说明:
    企业名称: BTM  indentMoney  indentDate

'''

last_year_months = [(datetime.datetime.now() - pd.tseries.offsets.DateOffset(months=i)).strftime('%Y-%m-%d')[:7] \
                    for i in [12 , 6 , 0]]

def BTM_cigarette_order_increase_half_year():
    null_type_list = ['', None, 'null', '/', 'Null']
    after_6_month_list = []
    ago_6_month_list = []
    try:
        if BTM.has_key('indent') and \
                BTM['indent'] not in null_type_list \
                and len(BTM['indent']) >= 1:
            for i in BTM['indent']:
                if i.has_key('indentDate') and \
                        i['indentDate'] not in null_type_list and \
                        i.has_key('indentMoney')  and \
                        i['indentMoney'] not in null_type_list:
                    if i['indentDate'] >=  last_year_months[0] + "-01" and \
                            i['indentDate'] <  last_year_months[1] + "-01":
                        ago_6_month_list.append(float(i['indentMoney']))
                    elif i['indentDate'] >=  last_year_months[1] + "-01" and \
                            i['indentDate'] <  last_year_months[2] + "-01":
                        after_6_month_list.append(float(i['indentMoney']))
                    else:
                        pass
                else:
                    pass
            if sum(ago_6_month_list) != float(0):
                return round((sum(after_6_month_list) - sum(ago_6_month_list))/float(sum(ago_6_month_list)) , 4)
            else:
                return u'缺失值'
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result =  BTM_cigarette_order_increase_half_year()




