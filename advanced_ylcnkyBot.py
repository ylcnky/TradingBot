"""
The purpose of the ylcnkyBot Python program is to create an automated TradingBot on Binance
Utilized Python-Binance ( https://github.com/sammchardy/python-binance )
Advanced-Version capable of all exchanges, all coins (using cctx)
"""
#from binance.client import Client
#from binance.enums import *
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib import cm
#import matplotlib.pyplot as plt
#import save_historical_data_ylcnky
#from BinanceKeys import BinanceKey1


import ccxt
import time
import random
#from Keys import Key1

"""
Fetch the api keys from BinanceKeys.py file
"""

#api_key = BinanceKey1['api_key']
#api_secret = BinanceKey1['api_secret']
#client = Client(api_key, api_secret)

# get a deposit address for BTC
#address = client.get_deposit_address(asset='BTC')

def run():
        # Initialize function - Set initial conditions for Bot
        arbitrage()
        time.sleep(10)
        initialize()
        # Diversify function - Collect all balances across exchange, then diversify them
        #diversify()
        portfolio = 10 #BTC
        # Active Trader: Scalping, SwingTrading, Arbitrage
        while 1:
            ActiveTrader()

def arbitrage():
    # Create Triangular Arbitrage Function
    print('Arbitrage Function Running')
    coins = ['BTC', 'LTC', 'ETH'] #Coins to arbitrage
    for exch in ccxt.exchanges:
        exchange1 = ccxt.binance() #Initialize exchange
        symbols = exchange1.symbols
        if symbols is None:
            print('--------------Next Exchange-------------')
        elif len(symbols)<15:
            print('--------------Need More Pairs (Next Exchange)-------------')
        else:
            print(exchange1)
            exchange1_info = dir(exchange1)
            print('---------Exchange: ', exchange1.id)
            #print(exchange1_info)
            print (exchange1.symbols)
            time.sleep(5)
            #Find Currencies Trading Pairs to Trade
            pairs = []
            for sym in symbols:
                for symbol in coins:
                    if symbol in sym:
                        pairs.append(sym)
            print(pairs)
            # From coin1 to coin2 ETH/BTC - Bid
            # From coin2 to coin3 ETH/LTC - Ask
            # From coin3 to coin1 BTC/LTC - Bid
            arb_list = ['ETH/BTC'] #, 'ETH/LTC', 'BTC/LTC']
            # Find closed loop of currency pairs
            j = 0
            while 1:
                if j == 1:
                    final = arb_list[0][-3:] + '/' + str(arb_list[1][-3:])
                    print(final)
                    # if final in symbols:
                    arb_list.append(final)
                    break
                for sym in symbols:
                    if sym in arb_list:
                        pass
                    else:
                        if j % 2 == 0:
                            if arb_list[j][0:3] == sym[0:3]:
                                if arb_list[j] == sym:
                                    pass
                                else:
                                    arb_list.append(sym)
                                    print(arb_list)
                                    j += 1
                                    break
                        if j % 2 == 1:
                            if arb_list[j][-3:] == sym[-3:]:
                                if arb_list[j] == sym:
                                    pass
                                else:
                                    arb_list.append(sym)
                                    print(arb_list)
                                    j += 1
                                    break
                time.sleep(.5)
            print('List of Arbitrage Rates: ',arb_list)
            time.sleep(15)

        # Determine rates for our 3 currency pairs - order book
            i = 0
            exch_rate_list = []
            for sym in arb_list:
                if sym in symbols:
                    depth = exchange1.fetch_order_book(symbol=sym)
                    print(depth)
                    time.sleep(3)
                    exch_rate_list.append(depth['bids'][0][0])
                else:
                    exch_rate_list.append(0)
            print(exch_rate_list)
        # Compare the determine if Arbitgrage opportunity exists


def diversify():
    # Diversity TODO: (It will diversify the portfolio)
        # Collect amounts in wallets (available for trading)
    for exch2 in ccxt.exchanges:
        # TODO Change to incorporate API's keys and phrases (from Keys python script)
        exch = getattr(ccxt, exch2) ()
        exch.fetchBalance()
    # Diversify into pre-described amounts
            # 50% BTC, 5% each of 8 next top coins, 10x 1% micro-caps
        pass

def ActiveTrader():
    # Active Trader function - Continuous loop of calling trader functions such as Scalping and Artitrage Bot
    # Scalping Function
    # Swing Trading Function - Signals
    # Arbitrage Function
    pass

def initialize():

        # Get system status
        # Create List of Crypto pairs to watch
    all_symbols = []
    micro_cap_coins = []
    #time_horizon = 'Short
    #Risk = 'High'
    print("\n-------------------------WELCOME-------------------------\n")
    print("Hello and Welcome to advanced |ylcnky-cyptocurency| trader bot ")
    print("For questions and comments, please contact mehmet@ylcnky.com")
    print("----------------------------------------------------------")

    time.sleep(5)
    i = 0
    try:
            # Get Status of Exchange & Account
        print("\n-------------------Exchange Status----------------------\n")
        print('Number of Exchanges: ', len(ccxt.exchanges))
        print(ccxt.exchanges)
        print("----------------------------------------------------------")

            # Get exchange info
        for exch1 in ccxt.exchanges:
            list_of_symbols=[]
            if i > 0:
                break   # Break out of statement
            exch = getattr(ccxt, exch1) ()
            print("----------------------------------------------------------")
            print("Exchange: ", exch.id)
            print("Set Exchange Info (Limits): ", exch.rateLimit)
            print("Load Market: ", exch.load_markets)
            symbols = exch.symbols
            if symbols is None:
                print("No Symbols Loaded")
            else:
                print("Number of Symbols:", len(symbols))
                print("Exchange & Symbols: ")
                print("-------------------------")
                for sym in symbols:
                    list_of_symbols.append(sym) #Create a list of Symbols
                    all_symbols.append(sym) #Create a list of ALL symbols

                currencies = exch.currencies

                time.sleep(3)

                #Get market depth
                #for symbol in list_of_symbols:
                #    market_depth(symbol)
                # Test Market Order - Visualize - Scalping Functions: Testing with random symbol
                rand_sym = random.choice(list_of_symbols)
                market_depth(rand_sym, exch)
                visualize_market_depth(sym=rand_sym, exchange=exch)
                scalping_orders(exch, rand_sym)
                i += 1      # Break out of Initialize Statement
                time.sleep(4)
                """
                for symbol in exch.markets:
                print("Order Book for Symbol: ", symbol)
                print(exch.fetch_order_book(symbol))
                time.sleep(3)
                """

            # Place a test order, to place an actual order use the create_order function


            # Get Info about Coins in Watch List
        # coin_prices(list_of_symbols)
        # coin_tickers(list_of_symbols)
        # for symbol in list_of_symbols:
            # market_depth(symbol)

        # for coin in micro_cap_coins:
        #    visualize_market_depth(1, 1, coin)

        # for coin in micro_cap_coins:
        #    scalping_orders(coin, 1, 1)

            # Get recent trades
        # trades = client.get_recent_trades(symbol="BNBBTC")
        # print("\nRecent Trades: ", trades)
        # print("Local Time: ", time.localtime())
        # print("Recent Trades Time: ", convert_time_binance(trades[0]['time']))

            # Get Historical Trades
        # hist_trades = client.get_historical_trades(symbol="BNBBTC")
        # print("\nHistorical Trades: ", hist_trades)

            # Get Aggregate Trades
        # agg_trades = client.get_aggregate_trades(symbol="BNBBTC")
        # print("\nAggregate Trades: ", agg_trades)


        # Example visualizations of coins
        """
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
        """
        print("INITIALIZE SUCCESSFUL")
    except():
        print('\n \n \nATTENTION: NON VALID CONNECTION WITH CRYPTOCURRENCY BOT \n \n \n')

        # Account Withdrawal History Info
        #withdraws = client.get_withdraw_history()
        #print("\nClient Withdraw History: ", withdraws)








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

def market_depth(sym, exchange=ccxt.binance(), num_entries=20):
    #Get market depth
    #Retrieve and format market depth (order book) including time-stamp
    i=0     #Used as a counter for number of entries
    print("Order Book: ") #convert_time_binance(client.get_server_time()))   #Transfer to CCXT
    exchange.verbose = True
    depth = exchange.fetch_order_book(symbol=sym)               #Transf'd to CCXT
    #pprint(depth)
    print(depth['asks'][0])
    ask_tot=0.0
    ask_price =[]
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    print("\n", sym, "\nDepth     ASKS:\n")         #Edit to work with CCXT
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                #Determine Price to place ask order based on highest volume
                max_order_ask=ask[1]
                #print("Max Order ASK: ", max_order_ask)
                place_order_ask_price=round(float(ask[0]),5)-0.0001
            #ask_list.append([ask[0], ask[1]])
            ask_price.append(float(ask[0]))
            ask_tot+=float(ask[1])
            ask_quantity.append(ask_tot)
            #print(ask)
            i+=1
    j=0     #Secondary Counter for Bids
    print("\n", sym, "\nDepth     BIDS:\n")
    print("Price     Amount")
    for bid in depth['bids']:
        if j<num_entries:
            if float(bid[1])>float(max_order_bid):
                #Determine Price to place ask order based on highest volume
                max_order_bid=bid[1]
                #print("Max Order BID: ", max_order_bid)
                place_order_bid_price=round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            #print(bid)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price
    #Plot Data

def scalping_orders(exchange = ccxt.binance(), coin='BTC/USDT', wait=1, tot_time=1):
    #Function for placing 'scalp orders'
    #Calls on Visualizing Scalping Orders Function
    ap, aq, bp, bq, place_ask_order, place_bid_order, spread, proj_spread, max_bid, min_ask = visualize_market_depth(wait, tot_time, coin, 5, exchange)
    print("Coin: {}\nPrice to Place Ask Order: {}\nPrice to place Bid Order: {}".format(coin, place_ask_order, place_bid_order))
    print("Spread: {} % Projected Spread {} %".format(spread, proj_spread))
    print("Max Bid: {} Min Ask: {}".format(max_bid, min_ask))
    #Place Orders based on calculated bid-ask orders if projected > 0.05% (transaction fee)
    #Documentation: http://python-binance.readthedocs.io/en/latest/account.html#orders
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


def visualize_market_depth(wait_time_sec='1', tot_time='1', sym='BTC/USDT', precision=5, exchange=ccxt.binance()):
    cycles = int(tot_time)/int(wait_time_sec)
    start_time = time.asctime()         #Trans CCXT
    fig, ax = plt.subplots()
    for i in range(1,int(cycles)+1):
        ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order = market_depth(sym, exchange)

        #print(ask_price)
        plt.plot(ask_pri, ask_quan, color = 'red', label='asks-cycle: {}'.format(i))
        plt.plot(bid_pri, bid_quan, color = 'blue', label = 'bids-cycle: {}'.format(i))

        #ax.plot(depth['bids'][0], depth['bids'][1])
        max_bid = max(bid_pri)
        min_ask = min(ask_pri)
        max_quant = max(ask_quan[-1], bid_quan[-1])
        spread = round(((min_ask-max_bid)/min_ask)*100,5)   #Spread based on market
        proj_order_spread = round(((ask_order-bid_order)/ask_order)*100, precision)
        price=round(((max_bid+min_ask)/2), precision)
        plt.plot([price, price],[0, max_quant], color = 'green', label = 'Price - Cycle: {}'.format(i)) #Vertical Line for Price
        plt.plot([ask_order, ask_order],[0, max_quant], color = 'black', label = 'Ask - Cycle: {}'.format(i))
        plt.plot([bid_order, bid_order],[0, max_quant], color = 'black', label = 'Buy - Cycle: {}'.format(i))
        #plt.plot([min_ask, min_ask],[0, max_quant], color = 'grey', label = 'Min Ask - Cycle: {}'.format(i))
        #plt.plot([max_bid, max_bid],[0, max_quant], color = 'grey', label = 'Max Buy - Cycle: {}'.format(i))
        ax.annotate("Max Bid: {} \nMin Ask: {}\nSpread: {} %\nCycle: {}\nPrice: {}"
                    "\nPlace Bid: {} \nPlace Ask: {}\n Projected Spread: {} %".format(max_bid, min_ask, spread, i, price, bid_order, ask_order, proj_order_spread),
                    xy=(max_bid, ask_quan[-1]), xytext=(max_bid, ask_quan[0]))
        if i==(cycles+1):
            break
        else:
            time.sleep(int(wait_time_sec))
    #end_time = time.asctime()
    ax.set(xlabel='Price', ylabel='Quantity',
       title='{} Order Book: {} \n {}\n Cycle Time: {} seconds - Num Cycles: {}'.format(exchange.id, sym, start_time, wait_time_sec, cycles))
    plt.legend()
    plt.show()
    return ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order, spread, proj_order_spread, max_bid, min_ask


def coin_prices(watch_list):
    #Will print to screen, prices of coins on 'watch list'
    #returns all prices
    prices = client.get_all_tickers()           #Trans CCXT
    print("\nSelected (watch list) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in watch_list:
            print(price)
    return prices


def coin_tickers(watch_list):
    # Prints to screen tickers for 'watch list' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()            #Trans CCXT
    print("\nWatch List Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in watch_list:
            print(tick)
    return tickers

def portfolio_management(deposit = '10000', withdraw=0, portfolio_amt = '0', portfolio_type='USDT', test_acct='True'):
    """The Portfolio Management Function will be used to track profit/loss of Portfolio in Any Particular Currency (Default: USDT)"""
    #Maintain Portfolio Statistics (Total Profit/Loss) in a file
    pass

def Bollinger_Bands():
    #This Function will calculate Bollinger Bands for Given Time Period
    pass

def buy_sell_bot():
    pass

def position_sizing():
    pass

def trailing_stop_loss():
    pass

if __name__ == "__main__":
    run()