# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 15:56
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_high_fraud_risk_region.py
# @Software: PyCharm

'''eof
name:烟草店铺所处地区具有较高欺诈风险
code:BTM_high_fraud_risk_region
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
烟草店铺所处地区具有较高欺诈风险
    高风险地区包括：西藏,青海,宁夏,新疆,内蒙古,海南,甘肃,吉林,黑龙江,辽宁,广西
    0指不是，1指是

字段说明:
    企业名称: BTM  province
'''
hight_risk_province_list = [u'西藏' , u'青海' , u'宁夏' , u'新疆' , u'内蒙古' , u'海南' ,
                            u'甘肃' , u'吉林' , u'黑龙江' , u'辽宁' , u'广西']

def BTM_high_fraud_risk_region():
    null_type_list = ['', None, 'null', '/' , 'Null']
    try:
        if BTM.has_key('province') and \
                BTM['province'] not in null_type_list:
            if BTM['province'] in hight_risk_province_list:
                return 1
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_high_fraud_risk_region()