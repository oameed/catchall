
import os
import numpy    as np
import pandas   as pd
import yfinance as yf
import argparse

def wFILE(filename, dataframe):
    with open(filename, 'w') as fobj:
        fobj.write(dataframe.to_string(index = False))

def main():
    parser       = argparse.ArgumentParser()
    parser.add_argument('-n', type = str  , required = True)
    parser.add_argument('-r', type = float, default  = 100 )
    args         = parser.parse_args()
    symbols      = pd.read_csv(args.n, header = None)[0].tolist()
    
    price        = [yf.Ticker(x).info.get('currentPrice', 'N/A') for x in symbols] 
    dividends    = [yf.Ticker(x).info.get('dividendRate', 'N/A') for x in symbols] 
    
    num_stocks   = [int(np.ceil(args.r/x)) for x in dividends]
    funds_needed = [x*y for x,y in zip(price,num_stocks)  ]
    
    indices      = np.argsort(funds_needed).tolist()
    symbols      = [symbols     [i] for i in indices] 
    funds_needed = [funds_needed[i] for i in indices]
    num_stocks   = [num_stocks  [i] for i in indices]
    
    dataframe    = {'symbols'     : symbols     ,
                    'funds_needed': funds_needed,
                    'num_stocks'  : num_stocks   }
    dataframe    = pd.DataFrame(dataframe)
    
    wFILE('list' + '.txt', dataframe)
    

if __name__ == "__main__":
    main()


# python divcalc.py -n <name of the watch list>
#
# yfinance Documentation:
# ranaroussi.github.io/yfinance/
