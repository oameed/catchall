
import pandas   as pd
import numpy    as np
import yfinance as yf

def rCSV(filename, column):    
    return pd.read_csv(filename)[column].tolist()

def wFILE(filename, dataframe):
    with open(filename, 'w') as fobj:
        fobj.write(dataframe)

def split_symbols(symbols):
    info          = [yf.Ticker(x).fast_info['quoteType'] for x in symbols]
    indicesETF    = [i for i in range(len(symbols)) if info[i] == 'ETF'  ]
    symbolsETF    = [symbols[i] for i in indicesETF]
    symbolsEQUITY = [x for x in symbols if not x in symbolsETF]
    if len(symbolsEQUITY) == 0:
        print('watchlist has no EQUITY items!')
    if len(symbolsETF   ) == 0:
        print('watchlist has no ETF items!'   )
    return symbolsEQUITY, symbolsETF

def remove_young(symbols,params):
    age = [params[0][0] - yf.Ticker(x).history(period = 'max')['Open'].keys()[0].year for x in symbols]
    return [x for i,x in enumerate(symbols) if age[i] > params[0][1]]

def get_valuations(symbols):
    info      = [yf.Ticker(x).get_valuation_measures()['Current'].to_dict() for x in symbols]
    PE        = [x['Trailing P/E'] for x in info]
    PB        = [x['Price/Book'  ] for x in info]
    PS        = [x['Price/Sales' ] for x in info]
    info      = [yf.Ticker(x).get_info() for x in symbols]
    sector    = [x['sectorDisp'  ] for x in info]
    industry  = [x['industryDisp'] for x in info]
    indices   = np.argsort(PE).tolist()
    symbols   = [symbols [i] for i in indices]
    PE        = [PE      [i] for i in indices]
    PB        = [PB      [i] for i in indices]
    PS        = [PS      [i] for i in indices]
    sector    = [sector  [i] for i in indices]
    industry  = [industry[i] for i in indices]
    dataframe = {'Symbols' : symbols ,
                 'P/E'     : PE      ,
                 'P/B'     : PB      ,
                 'P/S'     : PS      ,
                 'sector'  : sector  ,
                 'industry': industry }
    dataframe = pd.DataFrame(dataframe)
    filename  = 'valuation_measures' + '.txt'
    wFILE(filename, dataframe.to_string(index = False, na_rep = '-')) 

def get_dividend_table(symbols,params):
    def get_key_value(dict,key):
        try:
            value = dict[key]
        except KeyError:
            value = None
        return value
    info      = [yf.Ticker(x).get_info() for x in symbols]
    indices   = [i for i,x in enumerate(info) if not get_key_value(x,'dividendYield') == None]
    symbols   = [symbols[i] for i in indices]
    info      = [info   [i] for i in indices]
    ETF       = [x['quoteType'         ] if x['quoteType'] == 'ETF' else None for x in info ]
    sector    = [get_key_value(x,'sector'  ) for x in info]
    industry  = [get_key_value(x,'industry') for x in info]
    Price     = [x['regularMarketPrice'] for x in info]
    Yield     = [x['dividendYield'     ] for x in info]
    Dividend  = [p*(y/100) for p,y in zip(Price   ,Yield)]
    NumStock  = [int(np.ceil(params[1][0]/x)) for x in Dividend]
    ReqFunds  = [n*p       for n,p in zip(NumStock,Price)]
    indices   = np.argsort(ReqFunds).tolist()
    symbols   = [symbols [i] for i in indices]
    ETF       = [ETF     [i] for i in indices]
    ReqFunds  = [ReqFunds[i] for i in indices]
    NumStock  = [NumStock[i] for i in indices]
    Price     = [Price   [i] for i in indices]
    Dividend  = [Dividend[i] for i in indices]
    sector    = [sector  [i] for i in indices]
    industry  = [industry[i] for i in indices]
    dataframe = {'Symbol'  : symbols ,
                 'ETF'     : ETF     ,
                 'ReqFunds': ReqFunds,
                 'NumStock': NumStock,
                 'Price'   : Price   ,
                 'Dividend': Dividend,
                 'Sector'  : sector  ,
                 'Industry': industry }
    dataframe = pd.DataFrame(dataframe)
    filename  = 'dividend_table' + '_' + str(params[1][0])+ '_' + 'USD' + '.txt'
    wFILE(filename, dataframe.to_string(index = False, na_rep = '-')) 

def initialize_run():
    # params[0][0]: current year
    # params[0][1]: company age limit
    # params[1][0]: annual dividend pay
    import argparse
    import datetime
    parser  = argparse.ArgumentParser()
    parser.add_argument('-n', type = str, required = True)
    parser.add_argument('-a', type = int, default  = 3   )
    parser.add_argument('-d', type = int, default  = 10  )
    args    = parser.parse_args()
    time    = datetime.datetime.now()
    params  = [[time.year,args.a],
               [args.d          ] ]
    symbols = rCSV(args.n,'Symbol')
    return params, symbols

def main():
    params, symbols           = initialize_run()
    
    symbolsEQUITY, symbolsETF = split_symbols(symbols)
    if len(symbolsEQUITY) > 0:
        symbolsEQUITY         = remove_young(symbolsEQUITY,params)
    symbols                   = symbolsEQUITY + symbolsETF
    
    if len(symbolsEQUITY) > 0:
        get_valuations(symbolsEQUITY)
    
    get_dividend_table(symbols,params)
    
if __name__ == "__main__":
    main()
