##import talib as ta
##from ta.utils import dropna
import yfinance as yf
from yfinance import Ticker as yf2
import pandas as pd
import sys
##import re
import numpy as np
##from talib import stream

from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
##today = date.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
##import mpl_finance
##import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc

from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import sys
import re

##global n2,n4,breakz
n2=2
n4=2
##breakz=10000

def test(i):
    import streamlit as st
    st.legacy_caching.clear_cache()
    
    print("inside test - Earnings_backup22.py")
    #########################################
    #starting rows, ending rows
##    n2=2
##    n4=2
    n2=2
    n4=2
    breakz=i-1
    print('******************* breakz is :',i)
    ##########################################
        
    perda='90d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3

##    f=open('/home/az2/t7.txt', 'r') 
    f=open('/home/az2/t65.txt', 'r')
    
    ticker=[]
##    ticker=ticker.upper()
    i=0
    for x in f:
        i=i+1
        if re.findall('-',x):
            ticker.append(x.split('-')[0].strip(' '))
            if i > breakz:
                break

    print('***************',ticker)
    perd=perda
    intervl=intervla
    ##ticker=['ZTS' , 'ZBH' , 'YTRA' , 'XXII' , 'XTNT' , 'XRAY' , 'XOMA' , 'XFOR' , 'WMS' , 'WFCF' , 'WD' , 'WCC' , 'W' , 'VSTO' , 'VSAT' , 'VNT' , 'VMC' , 'VIACA' , 'VIAC' , 'VG' , 'USPH' , 'UONEK' , 'UONE' , 'UNIT' , 'UFS' , 'UFCS' , 'TWI' , 'TTSH' , 'TRGP' , 'TNK' , 'TM' , 'TK' , 'THR' , 'TGTX' , 'TGP' , 'TGNA' , 'TEF' , 'TCRR' , 'TARA' , 'STRA' , 'STOR' , 'STFC' , 'SSYS' , 'SRLP' , 'SO' , 'SMMNY' , 'SMLP' , 'SHYF' , 'SGMO' , 'SGA' , 'SELB' , 'SATS' , 'RGS' , 'RFP' , 'REYN' , 'REPL' , 'REGN' , 'RAVE' , 'QRTEB' , 'QRTEA' , 'PZZA' , 'PWR' , 'PWP' , 'PWFL' , 'PSNL' , 'PRVB' , 'PRMW' , 'PPL' , 'PLX' , 'PLNT' , 'PH' , 'PESI' , 'PENN' , 'PEI' , 'PBH' , 'PASG' , 'PALT' , 'PAE' , 'ORGS' , 'OPCH' , 'OGE' , 'OBSV' , 'NVMI' , 'NTLA' , 'NTCT' , 'NSIT' , 'NS' , 'NRG' , 'NREF' , 'NOVN' , 'NOMD' , 'NMM' , 'NKLA' , 'NEO' , 'MYE' , 'MUR' , 'MTSI' , 'MTBC' , 'MRNA' , 'MLAB' , 'MITO' , 'MGTX' , 'MGTA' , 'MDGL' , 'MBUU' , 'MASS' , 'LXP' , 'LSXMK' , 'LSXMB' , 'LSXMA' , 'LQDA' , 'LNTH' , 'LNG' , 'LITE' , 'LCUT' , 'LBRDK' , 'LBRDB' , 'LBRDA' , 'LAZY' , 'LAUR' , 'LAC' , 'LABP' , 'KVHI' , 'KTB' , 'KRTX' , 'KRP' , 'KOP' , 'KALA' , 'K' , 'JNCE' , 'ITRI' , 'ITIC' , 'ISPC' , 'IRWD' , 'IRM' , 'INS' , 'INOD' , 'IMUX' , 'IMRA' , 'IHC' , 'IFRX' , 'IDCC' , 'ICL' , 'IBP' , 'HZN' , 'HWM' , 'HSKA' , 'HMPT' , 'HMHC' , 'HL' , 'HIMX' , 'HII' , 'HBI' , 'GTN' , 'GPRE' , 'GPP' , 'GOLF' , 'GOLD' , 'GOGO' , 'GNL' , 'GNE' , 'GLTO' , 'GIL' , 'GEO' , 'GEL' , 'GDP' , 'FWONK' , 'FWONB' , 'FWONA' , 'FULC' , 'FOLD' , 'FOCS' , 'FIS' , 'ETTX' , 'EPAM' , 'ENG' , 'DYN' , 'DWSN' , 'DUK' , 'DSPG' , 'DRNA' , 'DOCN' , 'DNB' , 'DLX' , 'DISH' , 'DIN' , 'DEN' , 'DBRG' , 'CYBR' , 'CWEN' , 'CTXS' , 'CTRM' , 'CS' , 'CRON' , 'CRAI' , 'CQP' , 'CPE' , 'COMM' , 'CNQ' , 'CNP' , 'CNHI' , 'CMT' , 'CMRX' , 'CLDT' , 'CIR' , 'CI' , 'CHH' , 'CFX' , 'CDZI' , 'CCOI' , 'CBIO' , 'CARS' , 'BXRX' , 'BRG' , 'BPMP' , 'BOSSY' , 'BLUE' , 'BLPH' , 'BLL' , 'BLI' , 'BLDR' , 'BEPC' , 'BDX' , 'BCYC' , 'BCOR' , 'BCE' , 'BBIO' , 'BATRK' , 'BATRB' , 'BATRA' , 'BALY' , 'AYRO' , 'AVRO' , 'AUMN' , 'ATRS' , 'ATRA' , 'ATNX' , 'ASPS' , 'ARW' , 'ARVN' , 'ARDX' , 'APTV' , 'APT' , 'APD' , 'ALE' , 'ALBO' , 'AKBA' , 'AIH' , 'AHCO' , 'AGLE' , 'AFCG' , 'AES' , 'ADAP' , 'ACIW' , 'ABEO']

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

##
##    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
##    
##    df.reset_index(inplace=True,drop=False)
##    print(df['Close'])
    ##sys.exit()
##    df=pd.DataFrame(df['Volume'])
    ##    print(df.tail(4))
    df=pd.DataFrame(ticker)
    df.columns=['ticker']
    


    print(df)
##    sys.exit()
    df['ms_sector']=''
##    df['ms_fullTimeEmployees']=''
##    df['ms_earningsGrowth']=''
##    df['ms_totalCash']=''
##    df['ms_totalDebt']=''
##    df['ms_totalRevenue']=''
    df['ms_totalCashPerShare']=''
##    df['ms_sharesOutstanding']=''
##    df['ms_sharesShort']=''
##    df['ms_sharesPercentSharesOut']=''
##    df['ms_heldPercentInstitutions']=''
##    df['ms_trailingEps']=''
##    df['ms_heldPercentInsiders']=''
##    df['ms_shortRatio']=''
##    df['ms_floatShares']=''
##    df['ms_earningsQuarterlyGrowth']=''
##    df['ms_dateShortInterest']=''
##    df['ms_shortPercentOfFloat']=''
##    df['ms_sharesShortPriorMonth']=''
##    df['ms_averageVolume10days']=''
##    df['ms_askSize']=''
##    df['ms_bidSize']=''
    df['ms_volume']=''
##    df['ms_averageVolume']=''
##    df['ms_regularMarketVolume']=''
##    df['ms_averageVolume10days']=''
##    df['ms_dateShortInterest']=''
    df['ms_forwardEps']=''
##    df['ms_recommendationMean']=''
##    df['ms_targetMedianPrice']=''
##    df['ms_targetLowPrice']=''
##    df['ms_recommendationKey']=''
##    df['ms_freeCashflow']=''
##    df['ms_sharesOutstanding']=''
    df['ms_trailingEps']=''
##    df['ms_shortName']=''
##    df['ms_fullTimeEmployees']=''
##    df['ms_forwardEps']=''
##    df['ms_trailingEps']=''
    df['ms_recommendationKey']=''
##    df['ms_targetMedianPrice']=''
##    df['ms_targetLowPrice']=''
##    df['ms_recommendationMean']=''
##    df['ms_totalCash']=''
    df['ms_totalDebt']=''
    df['ms_totalRevenue']=''
##    df['ms_totalCashPerShare']=''
##
##    df['ms_earningsQuarterlyGrowth']=''
##    df['ms_earningsGrowth']=''
##    df['ms_sharesOutstanding']=''
##    df['ms_freeCashflow']=''
##    df['ms_sharesOutstanding']=''

##    df['ms_shortName']=''
##    
##from yfinance import Ticker import info as yf
    i=0


##
##    for x in df.index:
##            df['volume'].loc[x]=df['volume'].loc[x] 
##        df['totalRevenue'].loc[x]=numerize.numerize(np.float64(df['totalRevenue'].loc[x].item()))

            



    for x in df.index:
        i=i+1
        if i > breakz:
            
            break
##        print(x)    
            
##        df['ms_sector'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sector']
##        df['ms_fullTimeEmployees'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['fullTimeEmployees']
##
##        df['ms_sharesShort'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShort']
##        df['ms_sharesPercentSharesOut'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesPercentSharesOut']
##        df['ms_heldPercentInstitutions'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInstitutions']
##        df['ms_trailingEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['trailingEps']
##        df['ms_heldPercentInsiders'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInsiders']
##        df['ms_shortRatio'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortRatio']
##        df['ms_floatShares'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['floatShares']
##        
##        df['ms_dateShortInterest'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['dateShortInterest']
##        df['ms_shortPercentOfFloat'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortPercentOfFloat']
##        df['ms_sharesShortPriorMonth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShortPriorMonth']
##        df['ms_averageVolume10days'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']
##        df['ms_askSize'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['askSize']
##        df['ms_bidSize'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['bidSize']
        df['ms_volume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['volume']
##        df['ms_averageVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume']
##        df['ms_regularMarketVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['regularMarketVolume']
##        df['ms_averageVolume10days'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']
##        df['ms_dateShortInterest'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['dateShortInterest']
##
        df['ms_forwardEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['forwardEps']
        df['ms_trailingEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['trailingEps']
        df['ms_recommendationKey'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['recommendationKey']
##        df['ms_recommendationMean'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['recommendationMean']
##        df['ms_targetMedianPrice'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['targetMedianPrice']
##        df['ms_targetLowPrice'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['targetLowPrice']
##        df['ms_earningsQuarterlyGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsQuarterlyGrowth']
##        df['ms_earningsGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsGrowth']
##        df['ms_totalCash'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCash']
        df['ms_totalDebt'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalDebt']
        df['ms_totalRevenue'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalRevenue']
        df['ms_totalCashPerShare'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCashPerShare']
##        df['ms_sharesOutstanding'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesOutstanding']
##        df['ms_freeCashflow'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['freeCashflow']
##        df['ms_sharesOutstanding'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesOutstanding']
##


##        import humanize

##    print(numerize.numerize(np.float32(df33['ms_volume'].loc[x]).item())
##        print(df['ms_volume'].loc[x], 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
##        for x in df.index:
####            df['ms_volume'].loc[x]=np.float64(np.float64(df['ms_volume'].loc[x]))/float(6)
##            df['ms_volume'].loc[x]=df['ms_volume'].loc[x]
            
##            df['ms_volume'].loc[x]=numerize.numerize(np.float64(df['ms_volume'].loc[x].item()))
            
##            df['ms_volume'].loc[x]=humanize.naturalsize(df['ms_volume'].loc[x])
##            df['ms_volume'].loc[x]=numerize.numerize(np.float32(df['ms_volume'].loc[x]))
##        df['ms_totalDebt'].loc[x]=numerize.numerize(float(df['ms_totalDebt'].loc[x]))
##        df['ms_totalRevenue'].loc[x]=numerize.numerize(float(df['ms_totalRevenue']).loc[x])
##        df['ms_totalRevenue'].loc[x]=numerize.numerize(float(df['ms_totalRevenue']).loc[x])


##        df33['Diff_Vol'].loc[x]=numerize.numerize(np.float32(df33['Diff_Vol'].loc[x]).item())

            
    print('\n\n')
    


    print(df)    
    f.close()
    print('\n\n')
    print('*********************************************************************************************')
    print('test completed')
    print('*********************************************************************************************')
    print('\n\n')
  





def volume(mm,fa):
    breakz=int(mm)
    print("inside [volume/Part1], read all tickers from [t65.txt] file and get yahoo downloads. Output gpes to [dfp33.csv] file :")
    #########################################
    #starting rows, ending rows
##    n2=2
##    n4=2
    ##########################################
        
    perda='90d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3

##    f=open('/home/az2/t7.txt', 'r') 
    f=open('/home/az2/t65.txt', 'r')
    
    ticker=[]
##    ticker=ticker.upper()
    i=0
    for x in f:
        i=i+1
        if re.findall('-',x):
            ticker.append(x.split('-')[0].strip(' '))
            if i > breakz:
                break


    perd=perda
    intervl=intervla
    ##ticker=['ZTS' , 'ZBH' , 'YTRA' , 'XXII' , 'XTNT' , 'XRAY' , 'XOMA' , 'XFOR' , 'WMS' , 'WFCF' , 'WD' , 'WCC' , 'W' , 'VSTO' , 'VSAT' , 'VNT' , 'VMC' , 'VIACA' , 'VIAC' , 'VG' , 'USPH' , 'UONEK' , 'UONE' , 'UNIT' , 'UFS' , 'UFCS' , 'TWI' , 'TTSH' , 'TRGP' , 'TNK' , 'TM' , 'TK' , 'THR' , 'TGTX' , 'TGP' , 'TGNA' , 'TEF' , 'TCRR' , 'TARA' , 'STRA' , 'STOR' , 'STFC' , 'SSYS' , 'SRLP' , 'SO' , 'SMMNY' , 'SMLP' , 'SHYF' , 'SGMO' , 'SGA' , 'SELB' , 'SATS' , 'RGS' , 'RFP' , 'REYN' , 'REPL' , 'REGN' , 'RAVE' , 'QRTEB' , 'QRTEA' , 'PZZA' , 'PWR' , 'PWP' , 'PWFL' , 'PSNL' , 'PRVB' , 'PRMW' , 'PPL' , 'PLX' , 'PLNT' , 'PH' , 'PESI' , 'PENN' , 'PEI' , 'PBH' , 'PASG' , 'PALT' , 'PAE' , 'ORGS' , 'OPCH' , 'OGE' , 'OBSV' , 'NVMI' , 'NTLA' , 'NTCT' , 'NSIT' , 'NS' , 'NRG' , 'NREF' , 'NOVN' , 'NOMD' , 'NMM' , 'NKLA' , 'NEO' , 'MYE' , 'MUR' , 'MTSI' , 'MTBC' , 'MRNA' , 'MLAB' , 'MITO' , 'MGTX' , 'MGTA' , 'MDGL' , 'MBUU' , 'MASS' , 'LXP' , 'LSXMK' , 'LSXMB' , 'LSXMA' , 'LQDA' , 'LNTH' , 'LNG' , 'LITE' , 'LCUT' , 'LBRDK' , 'LBRDB' , 'LBRDA' , 'LAZY' , 'LAUR' , 'LAC' , 'LABP' , 'KVHI' , 'KTB' , 'KRTX' , 'KRP' , 'KOP' , 'KALA' , 'K' , 'JNCE' , 'ITRI' , 'ITIC' , 'ISPC' , 'IRWD' , 'IRM' , 'INS' , 'INOD' , 'IMUX' , 'IMRA' , 'IHC' , 'IFRX' , 'IDCC' , 'ICL' , 'IBP' , 'HZN' , 'HWM' , 'HSKA' , 'HMPT' , 'HMHC' , 'HL' , 'HIMX' , 'HII' , 'HBI' , 'GTN' , 'GPRE' , 'GPP' , 'GOLF' , 'GOLD' , 'GOGO' , 'GNL' , 'GNE' , 'GLTO' , 'GIL' , 'GEO' , 'GEL' , 'GDP' , 'FWONK' , 'FWONB' , 'FWONA' , 'FULC' , 'FOLD' , 'FOCS' , 'FIS' , 'ETTX' , 'EPAM' , 'ENG' , 'DYN' , 'DWSN' , 'DUK' , 'DSPG' , 'DRNA' , 'DOCN' , 'DNB' , 'DLX' , 'DISH' , 'DIN' , 'DEN' , 'DBRG' , 'CYBR' , 'CWEN' , 'CTXS' , 'CTRM' , 'CS' , 'CRON' , 'CRAI' , 'CQP' , 'CPE' , 'COMM' , 'CNQ' , 'CNP' , 'CNHI' , 'CMT' , 'CMRX' , 'CLDT' , 'CIR' , 'CI' , 'CHH' , 'CFX' , 'CDZI' , 'CCOI' , 'CBIO' , 'CARS' , 'BXRX' , 'BRG' , 'BPMP' , 'BOSSY' , 'BLUE' , 'BLPH' , 'BLL' , 'BLI' , 'BLDR' , 'BEPC' , 'BDX' , 'BCYC' , 'BCOR' , 'BCE' , 'BBIO' , 'BATRK' , 'BATRB' , 'BATRA' , 'BALY' , 'AYRO' , 'AVRO' , 'AUMN' , 'ATRS' , 'ATRA' , 'ATNX' , 'ASPS' , 'ARW' , 'ARVN' , 'ARDX' , 'APTV' , 'APT' , 'APD' , 'ALE' , 'ALBO' , 'AKBA' , 'AIH' , 'AHCO' , 'AGLE' , 'AFCG' , 'AES' , 'ADAP' , 'ACIW' , 'ABEO']

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]


    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    ##sys.exit()
    df=pd.DataFrame(df['Volume'])
    ##    print(df.tail(4))

##    df['revenuePerShare']=''
##    for x in df.index:
##        df['revenuePerShare'].loc[x]=yf.Ticker(ticker).info['revenuePerShare'].loc[x]
##
##
##    sys.exit()
##    df=pd.DataFrame(df['Close'])

    print('***********************************************************')
    print('Stocks performance in last 30 days for earnings')
    print('***********************************************************')

    print('========== running ===========')

    df.reset_index(inplace=False,drop=False)
    print(df,'   All tickers performance in last ',perda,' days')

    ########################################################################
    #############################################################
    #starting rows, ending rows
    n2=2
    n3=df.shape[0]-n4

    ##df2=df.iloc[[2,88],:]
    ##df2=df.iloc[[2,df.shape[0]-3],:]
    df2=df.iloc[[n2,n3],:]
    #########################################################################
    df2=df2.T
    df2=df2[1:]
    df2['diff']=df2.iloc[:,1]-df2.iloc[:,0]
    df2['%']=100*((df2.iloc[:,1]-df2.iloc[:,0])/df2.iloc[:,0])
    print('\n\n')

##    df2.columns=[df2.columns[0]+str['_Vol'],
##                 df2.columns[1]+str['_Vol'],
##                 df2.columns[2]+str['_Vol'],
####                 df2.columns[3]+str['_Vol']
####                 ]
##    print(df.columns)
##    df2.columns=['ff','tt3','g3','hh'
##                 ]



    ##print(df2.columns)

    print(df2.sort_values(by=['%'],ascending=False))
    print('\n\n')
    print(df2.shape)
    dfv=df2
    print(dfv.columns)
    dfv.to_csv('\home\az2\Downloads\dfv33.csv')

    print('\n\n')
    print('*********************************************************************************************')
    print('[Volume/part1] completed')
    print('*********************************************************************************************')
    print('\n\n')
    return(dfv)

def prices(mm,fa):
    print('kkkkkkkkkkk ', mm)
    print('*********************************************************************************************')
    print("inside prices/Part1, read all tickers from [t65.txt] file and get yahoo downloads. Output gpes to [dfp33.csv] file :")
    print('*********************************************************************************************')
##    int(breakz)=int(mm)
    #########################################
    #starting rows, ending rows
##    n2=2
##    n4=2
    ##########################################
        
    perda='90d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3

    f=open('/home/az2/t65.txt', 'r')
    
    ticker=[]
##    ticker=ticker.upper()
    i=0
    for x in f:
        i=i+1
        if re.findall('-',x):
            ticker.append(x.split('-')[0].strip(' '))
            if i > int(mm):
                break

    
    perd=perda
    intervl=intervla
    ##ticker=['ZTS' , 'ZBH' , 'YTRA' , 'XXII' , 'XTNT' , 'XRAY' , 'XOMA' , 'XFOR' , 'WMS' , 'WFCF' , 'WD' , 'WCC' , 'W' , 'VSTO' , 'VSAT' , 'VNT' , 'VMC' , 'VIACA' , 'VIAC' , 'VG' , 'USPH' , 'UONEK' , 'UONE' , 'UNIT' , 'UFS' , 'UFCS' , 'TWI' , 'TTSH' , 'TRGP' , 'TNK' , 'TM' , 'TK' , 'THR' , 'TGTX' , 'TGP' , 'TGNA' , 'TEF' , 'TCRR' , 'TARA' , 'STRA' , 'STOR' , 'STFC' , 'SSYS' , 'SRLP' , 'SO' , 'SMMNY' , 'SMLP' , 'SHYF' , 'SGMO' , 'SGA' , 'SELB' , 'SATS' , 'RGS' , 'RFP' , 'REYN' , 'REPL' , 'REGN' , 'RAVE' , 'QRTEB' , 'QRTEA' , 'PZZA' , 'PWR' , 'PWP' , 'PWFL' , 'PSNL' , 'PRVB' , 'PRMW' , 'PPL' , 'PLX' , 'PLNT' , 'PH' , 'PESI' , 'PENN' , 'PEI' , 'PBH' , 'PASG' , 'PALT' , 'PAE' , 'ORGS' , 'OPCH' , 'OGE' , 'OBSV' , 'NVMI' , 'NTLA' , 'NTCT' , 'NSIT' , 'NS' , 'NRG' , 'NREF' , 'NOVN' , 'NOMD' , 'NMM' , 'NKLA' , 'NEO' , 'MYE' , 'MUR' , 'MTSI' , 'MTBC' , 'MRNA' , 'MLAB' , 'MITO' , 'MGTX' , 'MGTA' , 'MDGL' , 'MBUU' , 'MASS' , 'LXP' , 'LSXMK' , 'LSXMB' , 'LSXMA' , 'LQDA' , 'LNTH' , 'LNG' , 'LITE' , 'LCUT' , 'LBRDK' , 'LBRDB' , 'LBRDA' , 'LAZY' , 'LAUR' , 'LAC' , 'LABP' , 'KVHI' , 'KTB' , 'KRTX' , 'KRP' , 'KOP' , 'KALA' , 'K' , 'JNCE' , 'ITRI' , 'ITIC' , 'ISPC' , 'IRWD' , 'IRM' , 'INS' , 'INOD' , 'IMUX' , 'IMRA' , 'IHC' , 'IFRX' , 'IDCC' , 'ICL' , 'IBP' , 'HZN' , 'HWM' , 'HSKA' , 'HMPT' , 'HMHC' , 'HL' , 'HIMX' , 'HII' , 'HBI' , 'GTN' , 'GPRE' , 'GPP' , 'GOLF' , 'GOLD' , 'GOGO' , 'GNL' , 'GNE' , 'GLTO' , 'GIL' , 'GEO' , 'GEL' , 'GDP' , 'FWONK' , 'FWONB' , 'FWONA' , 'FULC' , 'FOLD' , 'FOCS' , 'FIS' , 'ETTX' , 'EPAM' , 'ENG' , 'DYN' , 'DWSN' , 'DUK' , 'DSPG' , 'DRNA' , 'DOCN' , 'DNB' , 'DLX' , 'DISH' , 'DIN' , 'DEN' , 'DBRG' , 'CYBR' , 'CWEN' , 'CTXS' , 'CTRM' , 'CS' , 'CRON' , 'CRAI' , 'CQP' , 'CPE' , 'COMM' , 'CNQ' , 'CNP' , 'CNHI' , 'CMT' , 'CMRX' , 'CLDT' , 'CIR' , 'CI' , 'CHH' , 'CFX' , 'CDZI' , 'CCOI' , 'CBIO' , 'CARS' , 'BXRX' , 'BRG' , 'BPMP' , 'BOSSY' , 'BLUE' , 'BLPH' , 'BLL' , 'BLI' , 'BLDR' , 'BEPC' , 'BDX' , 'BCYC' , 'BCOR' , 'BCE' , 'BBIO' , 'BATRK' , 'BATRB' , 'BATRA' , 'BALY' , 'AYRO' , 'AVRO' , 'AUMN' , 'ATRS' , 'ATRA' , 'ATNX' , 'ASPS' , 'ARW' , 'ARVN' , 'ARDX' , 'APTV' , 'APT' , 'APD' , 'ALE' , 'ALBO' , 'AKBA' , 'AIH' , 'AHCO' , 'AGLE' , 'AFCG' , 'AES' , 'ADAP' , 'ACIW' , 'ABEO']

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    dft=pd.DataFrame(ticker)
    dft.to_csv('/home/az2/t__214.txt',index=False)



    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    ##sys.exit()
    
    ##    print(df.tail(4))


    df=pd.DataFrame(df['Close'])
    print('***********************************************************')
    print('Stocks performance in last 30 days for earnings')
    print('***********************************************************')

    print('========== running ===========')

    df.reset_index(inplace=False,drop=False)
    print(df,'   All tickers performance in last ',perda,' days')

    ########################################################################
    #############################################################
    #starting rows, ending rows
    n2=2
    n3=df.shape[0]-n4

    ##df2=df.iloc[[2,88],:]
    ##df2=df.iloc[[2,df.shape[0]-3],:]
    df2=df.iloc[[n2,n3],:]
    #########################################################################
    df2=df2.T
    df2=df2[1:]
    df2['diff']=df2.iloc[:,1]-df2.iloc[:,0]
    df2['%']=100*((df2.iloc[:,1]-df2.iloc[:,0])/df2.iloc[:,0])

##    df2['%']=(df2.iloc[:,1]-df2.iloc[:,0])/(df2.iloc[:,1]+df2.iloc[:,0])*100
    
    print('\n\n')

##    df2.columns=[df2.columns[0]+str['_Price'],
##                 df2.columns[1]+str['_Price'],
##                 df2.columns[2]+str['_Price'],
##                 df2.columns[3]+str['_Price']
##                 ]

    ##print(df2.columns)

    print(df2.sort_values(by=['%'],ascending=False))
    print('\n\n')
    print(df2.shape)
    dfp=df2
    dfp.to_csv('\home\az2\Downloads\dfp33.csv')

    print('\n\n')
    print('*********************************************************************************************')
    print('[Price/part1] completed')
    print('*********************************************************************************************')
    print('\n\n')           
    
    return(dfp)

############################### Part 1########################################

def Part1(i,fa):
    import os
    #########################################

    print("Inside Part1 i= ", i,' rows read inside the text file' )

##    test(i,fa)
    prices(i,fa)
    volume(i,fa)

def Part2():
    print('*********************************************************************************************')
    print("inside [part2] - final defc, read data from [part1/price and volume] df33.csv/volume, df33.csv/pricefiles-join/concat and throw output")
    print('*********************************************************************************************')
    import os
    import os.path
    if os.path.exists('\home\az2\Downloads\df33.csv') == True:
        os.remove('\home\az2\Downloads\df33.csv')
    ##############  Part 2 ###############################################
    dfp=pd.read_csv('\home\az2\Downloads\dfp33.csv')
    print(dfp.columns)
    dfp.columns=['ticker','Day1_P','Day90_P','Diff_price','Diff_%_P']
    print(dfp.head(4))

    dfv=pd.read_csv('\home\az2\Downloads\dfv33.csv')
    dfv.columns=['ticker','Day1_V','Day90_V','Diff_Vol','Diff_%_V']
    print(dfv.head(4))

    dfp.set_index('ticker',inplace=True)
    dfv.set_index('ticker',inplace=True)

    df33=pd.concat([dfp,dfv],axis=1)
    ##df33.fillna(str('0'), inplace=True)
    ##df33.reset_index(inplace=True,drop=False)
    df33['Diff_Vol']=df33['Diff_Vol'].fillna(0)
    df33['Day1_V']=df33['Day1_V'].fillna(0)
    df33['Day90_V']=df33['Day90_V'].fillna(0)
    ##df33['Diff_Vol'].replace(0,'nan',inplace=True)
    ##df33['Diff_Vol'].replace(44,nan,inplace=True)
    ##df33['Diff_Vol'].loc[:].fillna('0', inplace=True)
    for x in df33.index:
        df33['Diff_Vol'].loc[x]=numerize.numerize(np.float32(df33['Diff_Vol'].loc[x]).item())
        df33['Day1_V'].loc[x]=numerize.numerize(np.float32(df33['Day1_V'].loc[x]).item())
        df33['Day90_V'].loc[x]=numerize.numerize(np.float32(df33['Day90_V'].loc[x]).item())

    print(df33.sort_values(by=['Diff_%_P'],ascending=False),'  Price Delta % 3 month change - % Diff_%_P')

    print(df33.sort_values(by=['Day90_V'],ascending=False),'  Volume highest Raw volume yesterday - Day90_V')

    print(df33.sort_values(by=['Diff_Vol'],ascending=False),'  Volume Delta Raw 3 month change - Diff_Vol')
 ####################################   
##    for x in df33['Diff_Vol'].index:
##        if 'M' in df33['Diff_Vol'].loc[x]:
##            p4=len(df33['Diff_Vol'].loc[x])
##            df33.loc[x]=df33.loc[x].replace(to_replace=df33['Diff_Vol'].loc[x],value=int(str(df33['Diff_Vol'].loc[x])[0:p4-1]))
##            df33.loc[x]=df33['Diff_Vol'].loc[x]*1000000
####        if 'K' in df33['Diff_Vol'].loc[x]:
######            p4=len(df33['Diff_Vol'].loc[x])
####            df33['Diff_Vol'].loc[x]=df33.loc[x].replace(to_replace=df33['Diff_Vol'].loc[x],value=33)
####            df33['Diff_Vol'].loc[x]=df33['Diff_Vol'].loc[x]*1000    
##            
##            print(df33['Diff_Vol'].loc[x])
################################################
    print(df33.sort_values(by=['Diff_%_V'],ascending=False),'  Volume Delta % 3 month change - Diff_%_V')
    
##    print(df33.head(4))
    df33.to_csv('\home\az2\Downloads\df33.csv')

##    for x in df33.index:
##        df33['Diff_Vol'].loc[x]=numerize.numerize(np.float32(df33['Diff_Vol'].loc[x]).item())
    print('\n\n')
    print('*********************************************************************************************')
    print('[part2] completed')
    print('*********************************************************************************************')
    print('\n\n')
####################################################################################################################
def aligna():
    import os
    os.remove('/home/az2/t65.txt')

##    f3a=open('/home/az2/t7.txt','r')
##    for x in f3a:
##        print(x)
##    f3a.close()
    print('*********************************************************************************************')
    print("inside aligna")
    print('*********************************************************************************************')

    fa='/home/az2/t7_monday.txt'
##    fa='/home/az2/t7_tuesday.txt'
##    fa='/home/az2/t7_wednesday.txt'
##    fa='/home/az2/t7_thursday.txt'
##    fa='/home/az2/t7_Friday.txt'
##    fa='/home/az2/t7_test_list.txt'


    
##    fa=open('/home/az2/t7_monday.txt', 'r')
##    fa=open('/home/az2/t7_tuesday.txt', 'r')    
##    fa=open('/home/az2/t7_wednesday.txt', 'r')
##    fa=open('/home/az2/t7_thursday.txt', 'r')
##    fa=open('/home/az2/t7_Friday.txt', 'r')
    

    f=open(fa,'r')    
    f3=open('/home/az2/t65.txt','w+')
    ticker=[]
    i=0
    k=0
    for x in f:
        i=i+1
##        print(i,'  ',x)
        if re.findall('-',x):
    ##        print('- found ',x)
            k=k+1
            ticker.append(x.split('-')[0].strip(' '))
    print('ooooo [no dashes] k= ',k, ' in ',f)
    print('ooooo [no dashes] i= ',i, 'lines in ',f)
    print('\n')
##    return (k)
##    f3.close()
    print('****************8 babu2 completed')
    f.close()


################################################
    
    f=open(fa,'r')
##        f=open('/home/az2/t7_tuesday.txt', 'r')

    i=0
    k3a=0


    f=open(fa,'r')
    print("777   ",fa)
##        f=open('/home/az2/t7.txt', 'r')
    f3=open('/home/az2/t65.txt','w')
    if k <  1:
        
        for x in f:
##                print(x)
            i=i+1

            if '(' not in x:
##                    print('data [added] to the file: --> ',x)                    
                k3a=k3a+1
                f3.write(str(x).rstrip('\n')+str(' -').rstrip('\n'))
                f3.write('\n')

##        print('k2 / ', 'stupid removed ) tickers in t65.txt file = ',k2)
    print('k3a /', '55 No of companies to report earnings : ---> ', k3a)
    f.close()

    f=open(fa,'r')
##        f=open('/home/az2/t7_tuesday.txt', 'r')
    i=0
    k3b=0
    if k >  0:
        for x in f:
            print(x)
            if '[' not in x:
                
                k3b=k3b+1
                i=i+1
                print('data written [*withOUT*] dashes: -->',x)
                f3.write(str(x).rstrip('\n')+str(' -').rstrip('\n'))
                print('data written [*withOUT*] dashes: -->',x)
                f3.write(x)
    ##        f3.write(x.split('-')[0].strip(' '))
                f3.write('\n')
##        print('k3 / tickers in t65.txt file [no dashes added]= ',k3)
    print('k3b / 44  No of companies to report earnings : ---> ', k3b)
    print('tipu ', k3a)
    if k3b > k3a:
        k3=k3b
    if k3a > k3b:
        k3=k3a
    print('tipu33 ', k3)    
    
    
    f3.close()
    f.close()
    return (k3,fa)

  


    print('\n\n')
    print('*********************************************************************************************')
    print(' align completed')
    print('*********************************************************************************************')



    k=aligna.babu3(fa)
    print('babu2 no :',k,'   ','\n')
    babu3(fa,k)
##    sys.exit()

def main():
    import streamlit as st
    st.legacy_caching.clear_cache()

    k3,fa=aligna()
    print ('k3gggg',k3)

    Part1(k3,fa)
    Part2()
    print("No of companies reporting: ",k3-1)
    

main()


