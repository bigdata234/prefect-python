# -*- coding: utf-8 -*-

import hmac
import time
import base64
import urllib
import random
import struct
import hashlib
import urllib
import urllib2
import json

# Basic request URL
URL = 'csec.api.qcloud.com/v2/index.php'
# 密钥,请进行替换,密钥申请地址 https://console.qcloud.com/capi
SECRET_ID = 'AKIDGRVQAldTZUI0XtEFOSM5f4K0b1GLOyY5'
SECRET_KEY = 'a0EHTYVVRchS7c0DE8ua7So8PVZwBHEH'
REGION = 'ap-chengdu'


# Signature algorithm using HMAC-SHA1
def hmac_sha1(key, text):
    return base64.b64encode(hmac.new(key, text, hashlib.sha1).digest())


# Generates an available URL
def make_url(method, action, region, secret_id, secret_key, **args):
    # Fill common parameters and calculate and signature
    args['Nonce'] = random.randint(0, 0x7fffffff)
    args['Action'] = action
    args['Region'] = region
    args['SecretId'] = secret_id
    args['Timestamp'] = int(time.time())
    args['Signature'] = hmac_sha1(secret_key,
                                  '%s%s?%s' % (method, URL, '&'.join('%s=%s' % t for t in sorted(args.items()))))

    # Assemble final request URL
    return 'https://%s?%s' % (URL, '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in args.iteritems()))


# demo section
def anti_fraud(**args):
    '''
    补充用户、行为信息数据,方便我们做更准确的数据模型
    协议参考 https://www.qcloud.com/document/product/295/6584
    '''
    url = make_url('GET', 'AntiFraud', REGION, SECRET_ID, SECRET_KEY, **args)
    data = http_get(url)
    data = json.loads(data.decode("UTF-8"))

    return data


def http_get(url):
    response = urllib2.urlopen(url=url)
    return response.read()


def http_post(url, **args):
    response = urllib2.urlopen(url=url, data=urllib.urlencode(args))
    return response.read()


__all__ = ['anti_fraud', 'make_url']

if __name__ == '__main__':

    data = anti_fraud(
        # 基本字段
        idNumber='',
        phoneNumber='0086-',
        # 可选字段
        name=''
    )

    print data
    for k in data:
        print k, data[k]
