# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 21:20
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_UndestroyCardAmtUsedRatio.py
# @Software: PyCharm

'''eof
name:未销户贷记卡授信额度使用占比
code:IC_UndestroyCardAmtUsedRatio
tableName:
columnName:
groups:个人征信
dependencies:IC
type:常用指标
dataSourceType:在线指标
description:
eof'''

'''
IC_UndestroyCardAmtUsedRatio的逻辑：
    1、取出ICRCardInfo 的CardState字段不包含（“注销” or “未激活”）的记录 
    2、计算授信总额度 sumamt=sum（CardLimitAmt）
    3、计算已使用总额度sumusedlimit=sum（CardUsedLimitAmt） 
    4、计算已使用额度占总额度的比率 IC_UndestroyCardAmtUsedRatio= sumusedlimit/sumamt
'''

def IC_UndestroyCardAmtUsedRatio():
    null_type_list = ['', None, 'null', '/', 'Null']
    CardLimitAmt_list = [float(0)]
    CardUsedLimitAmt_list = [float(0)]
    try:
        if IC.has_key('ICRCardInfo') and \
                IC['ICRCardInfo'] not in null_type_list and len(IC['ICRCardInfo']) >= 1:
            for i in IC['ICRCardInfo']:
                if i.has('CardState') and \
                        i['CardState'] not in [u'注销' , u'未激活' , u'尚未激活' , '', None, 'null', '/', 'Null']:
                    print i['CardState']
                    if i.has_key('CardLimitAmt') and i['CardLimitAmt'] not in null_type_list:
                        CardLimitAmt_list.append(float(i['CardLimitAmt']))
                    else:
                        pass
                    if i.has_key('CardLimitAmt') and i['CardLimitAmt'] not in null_type_list:
                        CardUsedLimitAmt_list.append(float(i['CardLimitAmt']))
                    else:
                        pass
                else:
                    pass
            if sum(CardLimitAmt_list) != float(0)
                return round(sum(CardUsedLimitAmt_list)/sum(CardLimitAmt_list) , 4)
            else:
                return u'缺失值'
        else:
            return u'缺失值'
    except:
        return u'缺失值'

result = IC_UndestroyCardAmtUsedRatio()


