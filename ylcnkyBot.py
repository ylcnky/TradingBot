"""
The purpose of the ylcnkyBot Python program is to create an automated TradingBot on Binance
Utilized Python-Binance ( https://github.com/sammchardy/python-binance )
Advanced-Version capable of all exchanges, all coins (using cctx)
"""
from binance.client import Client
import time
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import save_historical_data_ylcnky
from BinanceKeys import BinanceKey1

"""
Fetch the api keys from BinanceKeys.py file
"""
api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')