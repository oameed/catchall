
import os
import numpy    as np
import pandas   as pd
import yfinance as yf
import argparse

def wFILE(filename, dataframe):
    with open(filename, 'w') as fobj:
        fobj.write(dataframe.to_string(na_rep = '-'))

def get_dividend_paying_equities(symbols,info):
    indices_EQUITY             = [i for i in range(len(info)) if info[i]['quoteType'   ] == 'EQUITY']
    indices_EQUITY_no_dividend = [i for i in indices_EQUITY   if info[i].get('dividendRate') == None]
    symbols = [symbols[i] for i in range(len(info)) if not i in indices_EQUITY_no_dividend]
    info    = [info   [i] for i in range(len(info)) if not i in indices_EQUITY_no_dividend]
    return symbols, info

def get_price_dividends(info):
    # EQUITY
    #   price
    #       'currentPrice', 'regularMarketPrice'
    #   dividends
    #       'dividendRate', 'dividendYield'
    # ETF
    #   price:
    #       'regularMarketPrice'
    #   dividends
    #       'yield', 'dividendYield'
    price          = [x['regularMarketPrice'] for x in info] 
    indices_EQUITY = [i for i in range(len(info)) if info[i]['quoteType'] == 'EQUITY']
    dividends      = []
    for i in range(len(info)):
        if i in indices_EQUITY:
            div = info[i]['dividendRate']
            dividends.append(div)
        else:
            prc = info[i]['regularMarketPrice']
            div = info[i]['yield'] * prc
            dividends.append(div)
    return price, dividends

def initialize_run():
    # params[0][0]: name of the file containing symbols
    # params[0][1]: annual dividend rate
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type = str, required = True)
    parser.add_argument('-r', type = int, default  = 10  )
    args   = parser.parse_args()
    params = [[args.n,args.r]]
    return params

def main():
    params           = initialize_run()
    symbols          = pd.read_csv(params[0][0], header = None)[0].tolist()
    info             = [yf.Ticker(x).info for x in symbols]
    symbols, info    = get_dividend_paying_equities(symbols,info)
    ETFtag           = [x['quoteType'] if x['quoteType'] == 'ETF' else None for x in info]
    
    price, dividends = get_price_dividends(info)
    
    num_stocks       = [int(np.ceil(params[0][1]/x)) for x in dividends]
    funds_needed     = [x*y for x,y in zip(price,num_stocks)  ]
    indices          = np.argsort(funds_needed).tolist()
    
    symbols          = [symbols     [i] for i in indices]
    ETFtag           = [ETFtag      [i] for i in indices]
    price            = [price       [i] for i in indices]
    dividends        = [dividends   [i] for i in indices]
    num_stocks       = [num_stocks  [i] for i in indices]
    funds_needed     = [funds_needed[i] for i in indices]
        
    dataframe        = {'symbols'     : symbols     ,
                        'ETF'         : ETFtag      ,
                        'funds_needed': funds_needed,
                        'num_stocks'  : num_stocks  ,
                        'price'       : price       ,
                        'dividends'   : dividends    }
    dataframe        = pd.DataFrame(dataframe)
    
    wFILE('list' + '_' + str(params[0][1])+ '_' + 'USD' + '.txt', dataframe)
    
if __name__ == "__main__":
    main()

# python divcalc.py -n <name of the watch list>
#
# yfinance Documentation:
# ranaroussi.github.io/yfinance/
