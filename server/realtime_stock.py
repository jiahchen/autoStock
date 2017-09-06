# -*- coding: utf-8 -*-
'''

GET realtime info of stock.

URL: http://mis.tse.com.tw/stock/api/getStockInfo.jsp?
ex_ch: tse_(number of stock) or otc_(No.)
json: 1
delay: 0
_: (timestamp)

'''

import time
import json
import urllib3
from datetime import datetime

class Realtime(object):

    def __init__(self, stock_no, date):
        if not date:
            date = datetime.now()

        self.param = {
            'no': stock_no,
            'date': date.strftime('%Y%m%d')
        }

    def showdate(self):
        return self.param['date']