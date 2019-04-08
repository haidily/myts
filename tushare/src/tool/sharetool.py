# coding = utf-8
from settings import settings
import tushare

class ShareTool(object):

    def __init__(self):
        self.__ts = tushare
        self.__ts.set_token(settings.TS_TOKEN)

    def print_test(self):
        pro = self.__ts.pro_api()

        # 查询当前所有正常上市交易的股票列表
        data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        print(data)