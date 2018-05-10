#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    null_type_list = ['', None, 'null', '/', 'Null']
    if not IC.has_key('ICRRecordDetail') or \
            ( IC.has_key('ICRRecordDetail') and \
              (len(IC['ICRRecordDetail']) < 1 ) or IC['ICRRecordDetail'] in null_type_list):
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


