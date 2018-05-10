# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 15:18
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_shop_enterp_address.py
# @Software: PyCharm

'''eof
name:烟草登记店铺地址与企业地址不一致
code:BTM_shop_enterp_address
tableName:
columnName:
groups:烟商
dependencies:BTM,EG
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
烟草登记店铺地址与企业地址不一致
    将烟草登记店铺地址与企业地址进行精确匹配
    0指不一致，1指一致

字段说明:
    烟草登记店铺地址: BTM address
    企业地址: EG results address
'''

def BTM_shop_enterp_address():
    null_type_list = ['', None, 'null', '/' , 'Null']
    try:
        if BTM.has_key('address') and \
                BTM['address'] not in null_type_list and \
                EG.has_key('results') and \
                len(EG['results']) >= 1 and \
                EG['results'][0].has_key('jbxx') and \
                EG['results'][0]['jbxx'] and \
                EG['results'][0]['jbxx'].has_key('address') and  \
                EG['results'][0]['jbxx']['address'] not in null_type_list:
            if BTM['address'] == EG['results'][0]['jbxx']['address']:
                return 1
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_shop_enterp_address()