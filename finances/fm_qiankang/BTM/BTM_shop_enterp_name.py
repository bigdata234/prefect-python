# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 13:36
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : BTM_shop_enterp_name.py
# @Software: PyCharm

'''eof
name:烟草登记店铺名称与企业名称不一致
code:BTM_shop_enterp_name
tableName:
columnName:
groups:烟商
dependencies:BTM,EG
type:常用指标
datasourceType:在线指标
description:
eof'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
烟草登记店铺名称与企业名称不一致
     若是一致，返回为1，否则返回0

字段说明:
    烟草登记店铺名称: BTM altek
    企业名称:  
'''

def BTM_shop_enterp_name():
    null_type_list = ['', None, 'null', '/' , 'Null']
    try:
        if BTM.has_key('altek') and \
                BTM['altek'] not in null_type_list and \
                EG.has_key('results') and \
                len(EG['results']) >= 1 and \
                EG['results'][0].has_key('jbxx') and \
                EG['results'][0]['jbxx'] and \
                EG['results'][0]['jbxx'].has_key('company_name') and  \
                EG['results'][0]['jbxx']['company_name'] not in null_type_list:
            if BTM['address'] == EG['results'][0]['jbxx']['company_name']:
                return 1
            else:
                return 0
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = BTM_shop_enterp_name()