import backtrader as bt
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math  
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['Source Han Sans CN']#和鲸平台可用的中文字体
plt.rcParams['axes.unicode_minus'] = False

import akshare as ak
ETF_000050=ak.fund_etf_hist_em(symbol="000050",period="daily",start_date="20160104",end_date="20221231",adjust="hfq")

ETF_000050['openinterest']=0

ETF_BT_000050=ETF_000050.loc[ :, ['开盘','最高','最低','收盘','成交量','openinterest','日期']]

ETF_BT_000050.columns = ['open','high','low','close','volume','openinterest','datetime']

ETF_BT_000050=ETF_BT_000050.set_index(pd.to_datetime(ETF_BT_000050['datetime']))

print(ETF_BT_000050)


cerebro=bt.Cerebro()
datafeed=bt.feeds.PandasData(dataname=ETF_BT_000050, fromdate=dt.datetime(2016,1,1),todate=dt.datetime(2022,12,30))
cerebro.adddata(datafeed)

class BollStrategy(bt.Strategy):
    """布林带策略"""
    
    params = (
        ('period', 20),
        ('devfactor', 2.0),
    )
    
    def __init__(self):
        super().__init__()
        
        # 确保在 __init__ 中创建指标
        self.boll = bt.indicators.BBands(
            self.data.close,
            period=20,
            devfactor=2.0
        )
        
    def next(self):
        # 获取当前价格
        current_close = self.data.close[0]
        
        # 获取布林带值
        upper_band = self.boll.top[0]
        middle_band = self.boll.mid[0]
        lower_band = self.boll.bot[0]
        
        # 打印信息
        print(f"日期: {self.datetime.date()}")
        print(f"收盘价: {current_close:.2f}")
        print(f"布林带上轨: {upper_band:.2f}")
        print(f"布林带中轨: {middle_band:.2f}")
        print(f"布林带下轨: {lower_band:.2f}")
 

cerebro.broker.setcash(1000000.0)
cerebro.addstrategy(BollStrategy)
cerebro.run()