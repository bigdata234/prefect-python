# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 16:19
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_apply_leg_name.py
# @Software: PyCharm

'''eof
name:申请人与企业法定代表人不一致
code:BTM_apply_leg_name
tableName:
columnName:
groups:烟商
dependencies:EG
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
申请人与企业法定代表人不一致
'''

def BTM_apply_leg_name():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if ratingRequest.has_key('legalPerson') and ratingRequest['legalPerson'] not in null_type_list and \
                EG.has_key('result') and EG['result'] not in null_type_list and len(EG['result']) >= 1 and \
                EG['result'][0].has_key('jbxx') and EG['result'][0]['jbxx'] not in null_type_list and \
                EG['result'][0]['jbxx'].has_key('frname') and EG['result'][0]['jbxx']['frname'] not in null_type_list:
            if EG['result'][0]['jbxx']['frname'] == ratingRequest['legalPerson']:
                return 1
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_apply_leg_name()