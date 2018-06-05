# -*- coding: utf-8 -*-
from antiFraud.AntiFraud import *

if __name__ == '__main__':
    data = anti_fraud(
        # 基本字段
        idNumber='413026198812127330',
        phoneNumber='0086-13548067118',

        # 可选字段
        #name=''
    )

    print data
    for k in data:
        print k, data[k]