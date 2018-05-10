# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 0:23
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Sum_Card5YearsOverdueMon.py
# @Software: PyCharm

'''eof
name:贷记卡5年内逾期月份数之和
code:IC_Sum_Card5YearsOverdueMon
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
贷记卡5年内逾期月份数之和
    贷记卡信息（ICRCardInfo）提取贷记卡5年内逾期月份数（Card5YearsOverdueMon）字段
'''

def IC_Sum_Card5YearsOverdueMon():
    null_type_list = ['', None, 'null', '/', 'Null']
    res_list = []
    try:
        if IC.has_key('ICRCardInfo') and \
                IC['ICRCardInfo'] not in null_type_list and \
                len(IC['ICRCardInfo']) >= 1:
            for i in IC['ICRCardInfo']:
                if i.has_key('Card5YearsOverdueMon') and \
                        i['Card5YearsOverdueMon'] not in null_type_list:
                    res_list.append(int(i['Card5YearsOverdueMon']))
            if len(res_list) >= 1:
                return sum(res_list)
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_Sum_Card5YearsOverdueMon()