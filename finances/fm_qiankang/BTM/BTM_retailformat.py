# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 10:47
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_retailformat.py
# @Software: PyCharm


'''eof
name:烟草商户零售业态
code:BTM_retailformat
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
    直接提取 retailformat

字段说明:
    企业名称: BTM  retailformat  
'''

def BTM_retailformat():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if BTM.has_key('indent') and \
                BTM['indent'] not in null_type_list and \
                BTM.has_key('retailformat') and \
                BTM['retailformat'] not in null_type_list:
            return BTM['retailformat']
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_retailformat()