# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 16:10
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_apply_reg_name.py
# @Software: PyCharm

'''eof
name:申请人与烟草登记负责人不一致
code:BTM_apply_reg_name
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
申请人与烟草登记负责人不一致
'''

def BTM_apply_reg_name():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if BTM.has_key('principal') and BTM['principal'] not in null_type_list and \
                ratingRequest.has_key('legalPerson') and ratingRequest['legalPerson'] not in null_type_list:
            if BTM['principal'] == ratingRequest['legalPerson']:
                return 1
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_apply_reg_name()

