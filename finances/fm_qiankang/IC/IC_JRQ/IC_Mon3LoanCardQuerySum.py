# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 20:53
# @Author  : Jiao Ruiqiang
# @Email   : jiaoruiqiang@bbdservice.com
# @File    : IC_Mon3LoanCardQuerySum.py
# @Software: PyCharm

'''eof
name:最近3个月贷款审批与贷记卡审批查询次数
code:IC_Mon3LoanCardQuerySum
tableName:
columnName:
groups:个人征信
dependencies:IC
type:常用指标
dataSourceType:在线指标
description:
eof'''


def IC_Mon3LoanCardQuerySum():
    import datetime
    if IC['ICRRecordDetail'] == []:
        return 0
    num1 = 0
    num2 = 0
    try:
        queryTime = datetime.datetime.strptime(IC["ICRHeader"][0]["QueryTime"], "%Y-%m-%d")
    except:
        return u'缺失值'
    for i in range(len(IC['ICRRecordDetail'])):
        try:
            if (queryTime - datetime.datetime.strptime(IC['ICRRecordDetail'][i]["DetailQueryDate"],
                                                       "%Y-%m-%d")).days <= 90 and IC['ICRRecordDetail'][i][
                'DetailQueryReason'] == u'贷款审批':
                num1 += 1
        except:
            pass
        try:
            if (queryTime - datetime.datetime.strptime(IC['ICRRecordDetail'][i]["DetailQueryDate"],
                                                       "%Y-%m-%d")).days <= 90 and IC['ICRRecordDetail'][i][
                'DetailQueryReason'] == u'信用卡审批':
                num2 += 1
        except:
            pass
    return num1 + num2

result = IC_Mon3LoanCardQuerySum()