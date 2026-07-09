
import os
import numpy    as np
import pandas   as pd
import yfinance as yf
import argparse

def wFILE(filename, dataframe):
    with open(filename, 'w') as fobj:
        fobj.write(dataframe.to_string())

def get_get_dividend_paying(symbols,info):
    divrate = [x.get('dividendRate') for x in info] 
    indices = [i for i in range(len(divrate)) if not divrate[i] == None]
    return [symbols[i] for i in indices], [info[i] for i in indices]

def main():
    parser        = argparse.ArgumentParser()
    parser.add_argument('-n', type = str  , required = True)
    parser.add_argument('-r', type = float, default  = 10  )
    args          = parser.parse_args()
    
    symbols       = pd.read_csv(args.n, header = None)[0].tolist()
    info          = [yf.Ticker(x).info for x in symbols]
    
    symbols, info = get_get_dividend_paying(symbols,info)
    
    price         = [x.get('currentPrice') for x in info] 
    dividends     = [x.get('dividendRate') for x in info] 
    
    num_stocks    = [int(np.ceil(args.r/x)) for x in dividends]
    funds_needed  = [x*y for x,y in zip(price,num_stocks)  ]
    
    indices       = np.argsort(funds_needed).tolist()
    symbols       = [symbols     [i] for i in indices] 
    funds_needed  = [funds_needed[i] for i in indices]
    num_stocks    = [num_stocks  [i] for i in indices]
    price         = [price       [i] for i in indices]
    dividends     = [dividends   [i] for i in indices]
    
    dataframe     = {'symbols'     : symbols     ,
                     'funds_needed': funds_needed,
                     'num_stocks'  : num_stocks  ,
                     'price'       : price       ,
                     'dividends'   : dividends    }
    dataframe     = pd.DataFrame(dataframe)
    
    wFILE('list' + '_' + str(args.r)+ '_' + 'USD' + '.txt', dataframe)
    

if __name__ == "__main__":
    main()


# python divcalc.py -n <name of the watch list>
#
# yfinance Documentation:
# ranaroussi.github.io/yfinance/
