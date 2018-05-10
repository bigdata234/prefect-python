# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 17:18
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_Cigarette_Average_Price.py
# @Software: PyCharm

'''eof
name:每条烟的均价
code:BTM_Cigarette_Average_Price
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
每条烟均价
    BTM_Cigarette_Average_Price
需要用到的字段:
    indent indentDate indentAccount indentMoney
'''

def BTM_Cigarette_Average_Price():
    null_type_list = ['', None, 'null', '/', 'Null']
    money_list = [float(0)]
    count_list = [float(0)]
    try:
        if BTM.has_key('indent') and BTM['indent'] not in null_type_list and len(BTM['indent']) >= 1:
            for i in BTM['indent']:
                if i.has_key('indentMoney') and i['indentMoney'] not in null_type_list and \
                        i.has_key('indentAccount') and i['indentAccount']:
                    money_list.append(float(i['indentMoney']))
                    count_list.append(float(i['indentAccount']))
            if sum(count_list) != float(0):
                return round(sum(money_list)/sum(count_list) , 4)
            else:
                return u'缺失值'
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_Cigarette_Average_Price()