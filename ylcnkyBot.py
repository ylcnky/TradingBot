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

def run():
    # get system status
    # Create List of Crypto pairs to watch
    list_of_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC']
    micro_cap_coins = ['ICXBNB', 'BRDBNB', 'NAVBNB', 'RCNBNB']
    #time_horizon = 'Short
    #Risk = 'High'
    print("\n\n---------------------------------------------------------\n\n")
    print("Hello and Welcome to cyptocurency trader bot created by ylcnky ")
    time.sleep(5)
    try:
        # Example visualizations of coins
        save_historical_data_ylcnky.save_historic_klines_csv('BTCUSDT', "1 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_1MINUTE)
        save_historical_data_ylcnky.save_historic_klines_csv('ETHBTC', "6 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)
        save_historical_data_ylcnky.save_historic_klines_csv('BRDBNB', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
        save_historical_data_ylcnky.save_historic_klines_csv('BTCUSDT', "12 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1WEEK)
        save_historical_data_ylcnky.save_historic_klines_csv('ETHUSDT', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)

        # Visualize All Micro Cap Coins for 8 hour period and 3 minute Candlestick
        for coin in micro_cap_coins:
            save_historical_data_ylcnky.save_historic_klines_csv(coin, "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
            save_historical_data_ylcnky.save_historic_klines_csv(coin, "24 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)
            save_historical_data_ylcnky.save_historic_klines_csv(coin, "1 month ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)

    except():
        pass
    # Get Status of Exchange & Account
    try:
        status = client.get_system_status()
        print("\nExchange Status: ", status)

        # Account Withdrawal History Info
        withdraws = client.get_withdraw_history()
        print("\nClient Withdraw History: ", withdraws)

        # Get exchange info
        info = client.get_exchange_info()
        print("\nExchange Info (Limits): ", info)
    except:
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH BINANCE \n \n \n")

    # Get Info about Coins in Watch List
    coinprices(list_of_symbols)
    cointickers(list_of_symbols)
    # for symbol in list_of_symbols:
    #    market_depth(symbol)
    # for coin in micro_cap_coins:
    #    visualize_market_depth(1, 1, coin)

    for coin in micro_cap_coins:
        scalping_orders(coin, 1, 1)

    # get recent trades
    trades = client.get_recent_trades(symbol="BNBBTC")
    print("\nRecent Trades: ", trades)
    print("Local Time: ", time.localtime())
    print("Recent Trades Time: ", convert_time_binance(trades[0]['time']))

    # Get Historical Trades
    try:
        hist_trades = client.get_historical_trades(symbol="BNBBTC")
        print("\nHistorical Trades: ", hist_trades)
    except:
        print('\n \n \nATTENTION: NON VALID CONNECTION WITH BINANCE \n \n \n')

    # Get Aggregate Trades
    agg_trades = client.get_aggregate_trades(symbol="BNBBTC")
    print("\nAggregate Trades: ", agg_trades)

def convert_time_binance(gt):
    #Converts from Binance Time Format (milliseconds) to time-struct
    #From Binance-Trader Comment Section Code
    #gt = client.get_server_time()
    print("Binance Time: ", gt)
    print(time.localtime())
    aa = str(gt)
    bb = aa.replace("{'serverTime': ","")
    aa = bb.replace("}","")
    gg=int(aa)
    ff=gg-10799260
    uu=ff/1000
    yy=int(uu)
    tt=time.localtime(yy)
    #print(tt)
    return tt

def market_depth(sym, num_entries=20):
    # Get market depth
    # Retrieve and format market depth (order book) including timestamp
    i = 0 # Used as a counter for number of entries
    print('Order Book: ', convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    print(depth)
    print(depth['asks'][0])
    ask_tot = 0.0
    ask_price = []
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    print("\n", sym, "\nDepth     ASKS:\n")
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                # Determine Price to place ask order based on highest volume
                max_order_ask = ask[1]
                place_order_ask_price = round(float(ask[0]),5)-0.0001
            # ask_list.append(ask[0], ask[1])
            ask_price.append(float(ask[0]))
            ask_tot += float(ask[1])
            ask_quantity.append(ask_tot)
            #print(ask)
            i += 1
    j = 0   # Secondary Counter for Bids
    print("\n", sym, "\nDepth     BIDS:\n")
    print("Price     Amount")
    for bid in depth['bids']:
        if j<num_entries:
            if float(bid[1])>float(max_order_bid):
                # Determine Price to place ask order based on highest volume
                max_order_bid = bid[1]
                place_order_bid_price = round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price

def scalping_orders(coin, wait=1, tot_time=1):
    # Function for placing scalp orders and visulize them
    ap, aq, bp, bq, place_ask_order, place_bid_order, spread, proj_spread, max_bid, min_ask = visualize_market_depth(wait, tot_time, coin)
    print("Coin: {}\nPrice to Place Ask Order: {}\nPrice to place Bid Order: {}".format(coin, place_ask_order, place_bid_order))
    print("Spread: {} % Projected Spread {} %".format(spread, proj_spread))
    print("Max Bid: {} Min Ask: {}".format(max_bid, min_ask))
    """
    if proj_spread > 0.05:
        quant1=100          #Determine Code Required to calculate 'minimum' quantity
        #Place Bid Order:
        bid_order1 = client.order_limit_buy(
            symbol=coin,
            quantity=quant1,
            price=place_bid_order)
        #Place Ask Order
        ask_order1 = client.order_limit_sell(
            symbol=coin,
            quantity=quant1,
            price=place_ask_order)
    #Place second order if current spread > 0.05% (transaction fee)
    """
def visualize_market_depth(wait_time_sec='1', tot_time='1', sym='ICXBNB', precision=5):
    cycles = int(tot_time)/int(wait_time_sec)
    start_time = time.asctime()
    fig, ax = plt.subplots()
    for i in range(1, int(cycles)+1):
        ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order = market_depth(sym)
        # print(ask_price)
        plt.plot(ask_pri, ask_quan, color='red', label='asks-cycle: {}'.format(i))
        plt.plot(bid_pri, bid_quan, color='blue', label='bids-cycle: {}'.format(i))

        max_bid = max(bid_pri)
        min_ask = min(ask_pri)
        max_quant = max(ask_quan[-1], bid_quan[-1])
        spread = round(((min_ask-max_bid)/min_ask)*100,5) #Spread based on market
        proj_order_spread = round(((ask_order - bid_order) / ask_order) * 100, precision)
        price = round(((max_bid + min_ask) / 2), precision)
        plt.plot([price, price], [0, max_quant], color='green', label='Price - Cycle: {}'.format(i))  # Vertical Line for Price
        plt.plot([ask_order, ask_order], [0, max_quant], color='black', label='Ask - Cycle: {}'.format(i))
        plt.plot([bid_order, bid_order], [0, max_quant], color='black', label='Buy - Cycle: {}'.format(i))
        ax.annotate("Max Bid: {} \nMin Ask: {}\nSpread: {} %\nCycle: {}\nPrice: {}"
                    "\nPlace Bid: {} \nPlace Ask: {}\n Projected Spread: {} %".format(max_bid, min_ask, spread, i,
                        price, bid_order, ask_order, proj_order_spread), xy=(max_bid, ask_quan[-1]), xytext=(max_bid, ask_quan[0]))

        if i==(cycles+1):
            break
        else:
            time.sleep(int(wait_time_sec))
    ax.set(xlabel='Price', ylabel='Quantity',
           title='Binance Order Book: {} \n {}\n Cycle Time: {} seconds - Num Cycles: {}'.format(sym, start_time, wait_time_sec, cycles))
    plt.legend()
    plt.show()
    return ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order, spread, proj_order_spread, max_bid, min_ask

def coin_prices(watch_list):
    # Will print to screen, prices of coins on 'watch list'
    # returns all prices
    prices = client.get_all_tickers()
    print("\nSelected (watch list) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in watch_list:
            print(price)
    return prices

def coin_tickers(watch_list):
    # Prints to screen tickers for 'watch list' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()
    print("\nWatch List Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in watch_list:
            print(tick)
    return tickers

def portfolio_management(deposit='10000', withdraw=0, portfolio_amt='0', portfolio_type='USDT', test_acct='True'):
    """The Portfolio Management Function will be used to track profit/loss of Portfolio in Any Particular Currency (Default: USDT)"""
    pass

def Bollinger_Bands():
    #This Function will calculate Bollinger Bands for Given Time Period
    #EDIT: Will use Crypto-Signal for this functionality
    #https://github.com/CryptoSignal/crypto-signal
    pass

def buy_sell_bot():
    pass

def position_sizing():
    pass

def trailing_stop_loss():
    pass

#Place Limit Order
"""
order = client.order_limit_buy(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')
order = client.order_limit_sell(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')
"""




"""
#trade aggregator (generator)
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
# iterate over the trade iterator
for trade in agg_trades:
    pass
    #print(trade)
    # do something with the trade data
# convert the iterator to a list
# note: generators can only be iterated over once so we need to call it again
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
agg_trade_list = list(agg_trades)
# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
#for kline in klines:
    #print(kline)
"""

#place an order on Binance
"""
order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
"""

if __name__ == "__main__":
    run()