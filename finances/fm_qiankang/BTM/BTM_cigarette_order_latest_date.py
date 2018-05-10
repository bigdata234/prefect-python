# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 16:25
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_cigarette_order_latest_date.py
# @Software: PyCharm

'''eof
name:最近一次订烟日期距今的天数
code:BTM_cigarette_order_latest_date
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
最近一次订烟日期距今的天数

字段说明:
    企业名称: BTM indentDate

'''

def BTM_2_months_order_amount():
    null_type_list = ['', None, 'null', '/', 'Null']
    date_list = []
    try:
        if BTM.has_key('indent') and \
            BTM['indent'] not in null_type_list \
            and len(BTM['indent']) >= 1:
            for i in BTM['indent']:
                if i.has_key('indentDate') and \
                        i['indentDate'] not in null_type_list:
                    date_list.append(i['indentDate'])
            data_sort_list = sorted(date_list)
            laster_date = datetime.datetime.strptime(data_sort_list[-1], '%Y-%m-%d')
            return (datetime.datetime.now() - laster_date).days
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_2_months_order_amount()