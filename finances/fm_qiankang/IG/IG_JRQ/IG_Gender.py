# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 15:12
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IG_Gender.py
# @Software: PyCharm

'''eof
name:性别
code:IG_Gender
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
年龄:
    从身份证号码中提取第17位数字，如果是奇数，则为男，若是偶数则是女
    ICRHeader Certno
'''

def IG_Gender():
    null_type_list = ['', None, 'null', '/', 'Null']
    try:
        if IC.has_key('ICRHeader') and \
                IC['ICRHeader'] not in null_type_list and \
                len(IC['ICRHeader']) == 1 and \
                IC['ICRHeader'][0].has_key('Certno') and \
                IC['ICRHeader'][0]['Certno'] not in null_type_list \
                and len(IC['ICRHeader'][0]['Certno']) == 18:
            if int(IC['ICRHeader'][0]['Certno'][16])%2 == 1:
                return u'男性'
            else:
                return u'女性'
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IG_Gender()