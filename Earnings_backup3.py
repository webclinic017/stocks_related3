##import talib as ta
##from ta.utils import dropna
import yfinance as yf
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

def volume():
    
    #########################################
    #starting rows, ending rows
    n2=2
    n4=2
    ##########################################
        
    perda='90d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3

    f=open('/home/az2/t5.txt', 'r')
    ticker=[]
    i=0
    for x in f:
        i=i+1
        if re.findall('-',x):
            ticker.append(x.split('-')[0].strip(' '))
    ##        if i > 10:
    ##            break


    perd=perda
    intervl=intervla
    ##ticker=['ZTS' , 'ZBH' , 'YTRA' , 'XXII' , 'XTNT' , 'XRAY' , 'XOMA' , 'XFOR' , 'WMS' , 'WFCF' , 'WD' , 'WCC' , 'W' , 'VSTO' , 'VSAT' , 'VNT' , 'VMC' , 'VIACA' , 'VIAC' , 'VG' , 'USPH' , 'UONEK' , 'UONE' , 'UNIT' , 'UFS' , 'UFCS' , 'TWI' , 'TTSH' , 'TRGP' , 'TNK' , 'TM' , 'TK' , 'THR' , 'TGTX' , 'TGP' , 'TGNA' , 'TEF' , 'TCRR' , 'TARA' , 'STRA' , 'STOR' , 'STFC' , 'SSYS' , 'SRLP' , 'SO' , 'SMMNY' , 'SMLP' , 'SHYF' , 'SGMO' , 'SGA' , 'SELB' , 'SATS' , 'RGS' , 'RFP' , 'REYN' , 'REPL' , 'REGN' , 'RAVE' , 'QRTEB' , 'QRTEA' , 'PZZA' , 'PWR' , 'PWP' , 'PWFL' , 'PSNL' , 'PRVB' , 'PRMW' , 'PPL' , 'PLX' , 'PLNT' , 'PH' , 'PESI' , 'PENN' , 'PEI' , 'PBH' , 'PASG' , 'PALT' , 'PAE' , 'ORGS' , 'OPCH' , 'OGE' , 'OBSV' , 'NVMI' , 'NTLA' , 'NTCT' , 'NSIT' , 'NS' , 'NRG' , 'NREF' , 'NOVN' , 'NOMD' , 'NMM' , 'NKLA' , 'NEO' , 'MYE' , 'MUR' , 'MTSI' , 'MTBC' , 'MRNA' , 'MLAB' , 'MITO' , 'MGTX' , 'MGTA' , 'MDGL' , 'MBUU' , 'MASS' , 'LXP' , 'LSXMK' , 'LSXMB' , 'LSXMA' , 'LQDA' , 'LNTH' , 'LNG' , 'LITE' , 'LCUT' , 'LBRDK' , 'LBRDB' , 'LBRDA' , 'LAZY' , 'LAUR' , 'LAC' , 'LABP' , 'KVHI' , 'KTB' , 'KRTX' , 'KRP' , 'KOP' , 'KALA' , 'K' , 'JNCE' , 'ITRI' , 'ITIC' , 'ISPC' , 'IRWD' , 'IRM' , 'INS' , 'INOD' , 'IMUX' , 'IMRA' , 'IHC' , 'IFRX' , 'IDCC' , 'ICL' , 'IBP' , 'HZN' , 'HWM' , 'HSKA' , 'HMPT' , 'HMHC' , 'HL' , 'HIMX' , 'HII' , 'HBI' , 'GTN' , 'GPRE' , 'GPP' , 'GOLF' , 'GOLD' , 'GOGO' , 'GNL' , 'GNE' , 'GLTO' , 'GIL' , 'GEO' , 'GEL' , 'GDP' , 'FWONK' , 'FWONB' , 'FWONA' , 'FULC' , 'FOLD' , 'FOCS' , 'FIS' , 'ETTX' , 'EPAM' , 'ENG' , 'DYN' , 'DWSN' , 'DUK' , 'DSPG' , 'DRNA' , 'DOCN' , 'DNB' , 'DLX' , 'DISH' , 'DIN' , 'DEN' , 'DBRG' , 'CYBR' , 'CWEN' , 'CTXS' , 'CTRM' , 'CS' , 'CRON' , 'CRAI' , 'CQP' , 'CPE' , 'COMM' , 'CNQ' , 'CNP' , 'CNHI' , 'CMT' , 'CMRX' , 'CLDT' , 'CIR' , 'CI' , 'CHH' , 'CFX' , 'CDZI' , 'CCOI' , 'CBIO' , 'CARS' , 'BXRX' , 'BRG' , 'BPMP' , 'BOSSY' , 'BLUE' , 'BLPH' , 'BLL' , 'BLI' , 'BLDR' , 'BEPC' , 'BDX' , 'BCYC' , 'BCOR' , 'BCE' , 'BBIO' , 'BATRK' , 'BATRB' , 'BATRA' , 'BALY' , 'AYRO' , 'AVRO' , 'AUMN' , 'ATRS' , 'ATRA' , 'ATNX' , 'ASPS' , 'ARW' , 'ARVN' , 'ARDX' , 'APTV' , 'APT' , 'APD' , 'ALE' , 'ALBO' , 'AKBA' , 'AIH' , 'AHCO' , 'AGLE' , 'AFCG' , 'AES' , 'ADAP' , 'ACIW' , 'ABEO']

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]


    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    ##sys.exit()
    df=pd.DataFrame(df['Volume'])
    ##    print(df.tail(4))

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
    df2['%']=(df2.iloc[:,1]-df2.iloc[:,0])/(df2.iloc[:,1]+df2.iloc[:,0])*100
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
    return(dfv)



def prices():
    
    #########################################
    #starting rows, ending rows
    n2=2
    n4=2
    ##########################################
        
    perda='90d'
    intervla='1d'
    yy=str(intervla).split('d')[0]
    shiftbydays=3

    f=open('/home/az2/t5.txt', 'r')
    ticker=[]
    i=0
    for x in f:
        i=i+1
        if re.findall('-',x):
            ticker.append(x.split('-')[0].strip(' '))
    ##        if i > 10:
    ##            break


    perd=perda
    intervl=intervla
    ##ticker=['ZTS' , 'ZBH' , 'YTRA' , 'XXII' , 'XTNT' , 'XRAY' , 'XOMA' , 'XFOR' , 'WMS' , 'WFCF' , 'WD' , 'WCC' , 'W' , 'VSTO' , 'VSAT' , 'VNT' , 'VMC' , 'VIACA' , 'VIAC' , 'VG' , 'USPH' , 'UONEK' , 'UONE' , 'UNIT' , 'UFS' , 'UFCS' , 'TWI' , 'TTSH' , 'TRGP' , 'TNK' , 'TM' , 'TK' , 'THR' , 'TGTX' , 'TGP' , 'TGNA' , 'TEF' , 'TCRR' , 'TARA' , 'STRA' , 'STOR' , 'STFC' , 'SSYS' , 'SRLP' , 'SO' , 'SMMNY' , 'SMLP' , 'SHYF' , 'SGMO' , 'SGA' , 'SELB' , 'SATS' , 'RGS' , 'RFP' , 'REYN' , 'REPL' , 'REGN' , 'RAVE' , 'QRTEB' , 'QRTEA' , 'PZZA' , 'PWR' , 'PWP' , 'PWFL' , 'PSNL' , 'PRVB' , 'PRMW' , 'PPL' , 'PLX' , 'PLNT' , 'PH' , 'PESI' , 'PENN' , 'PEI' , 'PBH' , 'PASG' , 'PALT' , 'PAE' , 'ORGS' , 'OPCH' , 'OGE' , 'OBSV' , 'NVMI' , 'NTLA' , 'NTCT' , 'NSIT' , 'NS' , 'NRG' , 'NREF' , 'NOVN' , 'NOMD' , 'NMM' , 'NKLA' , 'NEO' , 'MYE' , 'MUR' , 'MTSI' , 'MTBC' , 'MRNA' , 'MLAB' , 'MITO' , 'MGTX' , 'MGTA' , 'MDGL' , 'MBUU' , 'MASS' , 'LXP' , 'LSXMK' , 'LSXMB' , 'LSXMA' , 'LQDA' , 'LNTH' , 'LNG' , 'LITE' , 'LCUT' , 'LBRDK' , 'LBRDB' , 'LBRDA' , 'LAZY' , 'LAUR' , 'LAC' , 'LABP' , 'KVHI' , 'KTB' , 'KRTX' , 'KRP' , 'KOP' , 'KALA' , 'K' , 'JNCE' , 'ITRI' , 'ITIC' , 'ISPC' , 'IRWD' , 'IRM' , 'INS' , 'INOD' , 'IMUX' , 'IMRA' , 'IHC' , 'IFRX' , 'IDCC' , 'ICL' , 'IBP' , 'HZN' , 'HWM' , 'HSKA' , 'HMPT' , 'HMHC' , 'HL' , 'HIMX' , 'HII' , 'HBI' , 'GTN' , 'GPRE' , 'GPP' , 'GOLF' , 'GOLD' , 'GOGO' , 'GNL' , 'GNE' , 'GLTO' , 'GIL' , 'GEO' , 'GEL' , 'GDP' , 'FWONK' , 'FWONB' , 'FWONA' , 'FULC' , 'FOLD' , 'FOCS' , 'FIS' , 'ETTX' , 'EPAM' , 'ENG' , 'DYN' , 'DWSN' , 'DUK' , 'DSPG' , 'DRNA' , 'DOCN' , 'DNB' , 'DLX' , 'DISH' , 'DIN' , 'DEN' , 'DBRG' , 'CYBR' , 'CWEN' , 'CTXS' , 'CTRM' , 'CS' , 'CRON' , 'CRAI' , 'CQP' , 'CPE' , 'COMM' , 'CNQ' , 'CNP' , 'CNHI' , 'CMT' , 'CMRX' , 'CLDT' , 'CIR' , 'CI' , 'CHH' , 'CFX' , 'CDZI' , 'CCOI' , 'CBIO' , 'CARS' , 'BXRX' , 'BRG' , 'BPMP' , 'BOSSY' , 'BLUE' , 'BLPH' , 'BLL' , 'BLI' , 'BLDR' , 'BEPC' , 'BDX' , 'BCYC' , 'BCOR' , 'BCE' , 'BBIO' , 'BATRK' , 'BATRB' , 'BATRA' , 'BALY' , 'AYRO' , 'AVRO' , 'AUMN' , 'ATRS' , 'ATRA' , 'ATNX' , 'ASPS' , 'ARW' , 'ARVN' , 'ARDX' , 'APTV' , 'APT' , 'APD' , 'ALE' , 'ALBO' , 'AKBA' , 'AIH' , 'AHCO' , 'AGLE' , 'AFCG' , 'AES' , 'ADAP' , 'ACIW' , 'ABEO']

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]


    df = yf.download(ticker, period=perd, interval=intervl,prepost = True)
    ##sys.exit()
    df=pd.DataFrame(df['Close'])
    ##    print(df.tail(4))

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
    df2['%']=(df2.iloc[:,1]-df2.iloc[:,0])/(df2.iloc[:,1]+df2.iloc[:,0])*100
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

            

    return(dfp)
    
#######################################################################
##
##dfv=volume()
##dfp=prices()
##
##print('\n\n\n')
##print("*****************************************************************")
##print(dfv,'  Volume')
####print(dfp,'  Prices')
##print("*****************************************************************")


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

print(df33.sort_values(by=['Diff_%_P'],ascending=False))
print(df33.head(4))

