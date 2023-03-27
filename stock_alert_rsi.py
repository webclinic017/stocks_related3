import os, pandas
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import datetime as dt
import talib as ta

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)

def s3():
    
    uu4v=['vg','astr','ispc','mpln','nbev','avya','cei','nvts','now','snow','amc','aapl','f','asml','zm',
        'tsla','nio','plug','lcid','rivn','fsr','blnk','mrna','bntx','nvax','bntx','isrg','biib','pfe','abt',
        'qcom','nvda','avgo','qrvo','gfs','tsm',
        'adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc,dltr','penn','coin','mstr','uber','lyft','z',
        '^ndx','RSX','AUPH','BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
        'BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
        'bby','zm','dks','anf','xpev','arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji','pfe','f','spy']
    uu4v=['AA', 'AAL', 'AAPL', 'ABBV', 'ABEV', 'ABUS', 'AFRM', 'AMAT', 'AMC', 'AMD', 'ANY', 'APA', 'AR', 'ARDX',
         'ATER', 'ATUS', 'ATVI', 'AUY', 'BA', 'BABA', 'BAC', 'BB', 'BBBY', 'BBD', 'BBIG', 'BEKE', 'BIMI', 'BITF',
         'BKKT', 'BKLN', 'BKR', 'BMY', 'BNGO', 'BP', 'BSX', 'BTBT', 'BTG', 'BTU', 'C', 'CAN', 'CCJ', 'CCL',
         'CDEV', 'CEI', 'CHPT', 'CIDM', 'CIG', 'CLF', 'CLOV', 'CMCSA', 'COP', 'COTY', 'CPNG', 'CSCO', 'CSX',
         'CTRA', 'CVE', 'CVX', 'CX', 'DAL', 'DELL', 'DIDI', 'DIS', 'DKNG', 'DM', 'DNA', 'DNN', 'DRIP', 'DVN',
         'EBAY', 'EDU', 'EEM', 'EFA', 'ENDP', 'EPD', 'EQT', 'ET', 'EVGO', 'EWJ', 'EWZ', 'F', 'FAMI', 'FB', 'FCEL',
         'FCX', 'FSR', 'FUBO', 'FUTU', 'FXI', 'GDX', 'GDXJ', 'GE', 'GEVO', 'GGB', 'GGPI', 'GILD', 'GLD', 'GM',
         'GNUS', 'GOLD', 'GOTU', 'GPS', 'GRNQ', 'GSAT', 'HAL', 'HBAN', 'HEXO', 'HIVE', 'HL', 'HOOD', 'HPE',
         'HPQ', 'HST', 'HUT', 'HYG', 'IAG', 'IAU', 'IBN', 'IDEX', 'IEF', 'IEFA', 'IEMG', 'INFY', 'INTC', 'IQ',
         'ITUB', 'IWM', 'IYR', 'JBLU', 'JD', 'JETS', 'JNJ', 'JNK', 'JPM', 'KEY', 'KGC', 'KMI', 'KO',
         'KOLD', 'KOS', 'KPLT', 'KR', 'KRE', 'KWEB', 'LCID', 'LGVN', 'LI', 'LQD', 'LU', 'LUMN', 'LUV', 'LVS',
         'LYG', 'M', 'MARA', 'MARK', 'MDLZ', 'METX', 'MGM', 'MKD', 'MMAT', 'MO', 'MRK', 'MRNA', 'MRO', 'MRVL',
         'MS', 'MSFT', 'MU', 'NAK', 'NAKD', 'NAOV', 'NCLH', 'NEE', 'NGD', 'NIO', 'NKLA', 'NLY', 'NNDM', 'NOK',
         'NVDA', 'OCGN', 'OGI', 'OPEN', 'ORCL', 'OXY', 'PBR',  'PBTS', 'PCG', 'PDD', 'PFE', 'PG',
         'PHUN', 'PINS', 'PLTR', 'PLUG', 'PPSI', 'PROG', 'PSFE', 'PTON', 'PTPI', 'PYPL', 'QCOM', 'QID', 'QQQ',
         'QS', 'RBLX', 'RF', 'RIDE', 'RIG', 'RIOT', 'RLX', 'ROOT', 'RWLK', 'SABR', 'SAVA', 'SDC', 'SDS', 'SENS',
         'SESN', 'SH', 'SHIP', 'SIRI', 'SKLZ', 'SLB', 'SLV', 'SNAP', 'SNDL', 'SOFI', 'SONN', 'SOS', 'SOXL',
         'SOXS', 'SPCE', 'SPXL', 'SPXS', 'SPXU', 'SPY', 'SQ', 'SQQQ', 'SU', 'SWN', 'T', 'TAL', 'TELL', 'TEVA',
         'TIGR', 'TJX', 'TLRY', 'TLT', 'TME', 'TNA', 'TNXP', 'TQQQ', 'TSLA', 'TSM', 'TWTR', 'TZA', 'UAL', 'UBER',
         'UEC', 'UMC', 'UNG', 'UVXY', 'V', 'VALE', 'VEA', 'VEON', 'VIAC', 'VICI', 'VIPS', 'VTRS', 'VWO', 'VXX', 'VZ',
         'WFC', 'WISH', 'WKHS', 'WMB', 'WMT', 'WTRH', 'X', 'XELA', 'XLB', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP',
         'XLRE', 'XLU', 'XLV', 'XOM', 'XOP', 'XPEV', 'Z', 'ZNGA', 'ZOM', 'MRNA','BNTX'
    ]

    s_p_500=['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP',
             'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL',
             'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON',
             'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO',
             'BA', 'BAC', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BIIB', 'BIO', 'BK', 'BKNG', 'BKR', 'BLK', 'BLL',
             'BMY', 'BR', 'BSX', 'BWA', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI',
             'CDNS', 'CDW', 'CE', 'CERN', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA',
             'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COST', 'CPB', 'CPRT', 'CRL', 'CRM', 'CSCO',
             'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CTXS', 'CVS', 'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS',
             'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRE',
             'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'ENPH', 'EOG', 'EQIX', 'EQR', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FTNT', 'FTV','GD', 'GE', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI',
             'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INFO','INTC', 'INTU', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KSU', 'L', 'LDOS', 'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NEE',
             'NEM', 'NFLX','NI', 'NKE', 'NLOK', 'NLSN', 'NOC', 'NOV', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA',
             'NXPI', 'ONL', 'ODFL', 'OGN', 'OKE','OMC', 'ORCL', 'ORLY', 'OTIS', 'OXY', 'PAYC', 'PAYX', 'PBCT', 'PCAR', 'PEAK', 'PEG', 'PENN',
             'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'POOL', 'PPG', 'PPL', 'PRGO', 'PRU',
             'PSA', 'PSX', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK',
             'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI',
             'SRE', 'STE', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TEL', 'TER', 'TFC', 'TFX', 'TGT',
             'TJX', 'TMO', 'TMUS', 'TPR', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TTWO', 'TWTR', 'TXN', 'TXT', 'TYL', 'UA', 'UAA', 'UAL',
             'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC', 'VIAC', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR',
             'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WU', 'WY', 'WYNN',
             'XEL', 'XLNX', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS' ]

    dji=['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
    nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CPRT', 'CSCO', 'CSX', 'CTAS', 'CTSH', 'DLTR', 'DOCU', 'DXCM', 'EA', 'EBAY', 'EXC', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JD', 'KDP', 'KHC', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SGEN', 'SIRI', 'SPLK', 'SWKS', 'TCOM', 'TEAM', 'TMUS', 'TSLA', 
    'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM' ]
    djTransport=['AAL', 'ALK', 'CAR', 'CHRW', 'CSX', 'DAL', 'EXPD', 'FDX', 'JBHT', 'JBLU', 'KEX', 'KSU', 'LSTR', 'LUV', 'MATX', 'NSC', 'R', 'UAL', 'UNP', 'UPS' ]
    etf=['AAXJ', 'ACWI', 'ACWX', 'AGG', 'AGQ', 'AMLP', 'ANGL', 'ARKF', 'ARKG', 'ARKK', 'ARKW', 'ASHR', 'BDRY', 'BIL', 'BITO', 'BKLN', 'BLOK', 'BND', 'BNDX', 'BNO', 'BOIL', 'BOTZ', 'BSJM', 'BSV', 'CIBR', 'CTRU', 'CWB', 'CWEB', 'CWI', 'DBA', 'DBC', 'DBO', 'DFAC', 'DFEN', 'DGRO', 'DIA', 'DOG', 'DRIP', 'DRIV', 'DUST', 'DVY', 'DXD', 'DXJ', 'ECH', 'EEM', 'EFA', 'EFG', 'EFV', 'EMB', 'EMLC', 'ERX', 'ERY', 'ESGE', 'ESGU', 'EUFN', 'EWA', 'EWC', 'EWG', 'EWH', 'EWJ', 'EWL', 'EWS', 'EWT', 'EWU', 'EWW', 'EWY', 'EWZ', 'EZU', 'FALN', 'FAS', 'FAZ', 'FCG', 'FEZ', 'FLOT', 'FPE', 'FTXN', 'FVD', 'FXI', 'FXN', 'GDX', 'GDXJ', 'GLD', 'GLDM','GSG', 'GUSH', 'HDV', 'HNDL', 'HYEM', 'HYG', 'HYLB', 'IAU', 'IBB', 'ICLN', 'IDV', 'IEF', 'IEFA', 'IEI', 'IEMG', 'IGIB', 'IGLB', 'IGSB', 'IGV', 'IHI', 'IJH', 'IJR', 'ILF', 'INDA', 'ISTB', 'ITB', 'ITOT', 'IUSB', 'IUSG', 'IUSV', 'IVOL', 'IVV', 'IVW', 'IWB', 'IWD', 'IWF', 'IWM', 'IWN', 'IWO', 'IWP', 'IWR', 'IWS', 'IXC', 'IXUS', 'IYE', 'IYR', 'JDST', 'JETS', 'JMST', 'JNK', 'JNUG', 'JPST', 'KBE', 'KBWB', 'KOLD', 'KRBN', 'KRE', 'KWEB', 'LABD', 'LABU', 'LIT', 'LMBS', 'LQD', 'MBB', 'MCHI', 'MDY', 'META', 'MINT', 'MJ', 'MSOS', 'MTUM', 'MUB', 'NEAR', 'NUGT', 'OIH', 'PAVE', 'PCY', 'PDBC', 'PFF', 'PFFD', 'PGX', 'PSQ', 'QID', 'QLD', 'QQQ', 'QUAL', 'QYLD', 'RDVY', 'REET', 'RSP', 'RSX', 'RWM','RYLD', 'SARK', 'SCHD', 'SCHE', 'SCHF', 'SCHO', 'SCHP', 'SCHX', 'SCHZ', 'SCO', 'SCZ', 'SDOW', 'SDS', 'SGOL', 'SH', 'SHV', 'SHY', 'SHYG', 'SILJ', 'SJNK', 'SLV','SMH', 'SOXL', 'SOXS', 'SPAB', 'SPDW', 'SPEM', 'SPHB', 'SPIB', 'SPIP', 'SPLB', 'SPLG', 'SPLV', 'SPMB', 'SPMD', 'SPSB', 'SPSM', 'SPTI', 'SPTL', 'SPTM', 'SPXL', 'SPXS', 'SPXU', 'SPY', 'SPYD', 'SPYG', 'SPYV', 'SQQQ', 'SRLN', 'SRTY', 'SSO', 'STIP', 'SVXY', 'TAN', 'TBF', 'TBT', 'TECL', 'TIP', 'TIPX', 'TLT', 'TMF', 'TMV','TNA', 'TOTL', 'TQQQ', 'TWM', 'TZA', 'UDOW', 'UNG', 'UPRO', 'URA', 'USHY', 'USMV', 'USO', 'UUP', 'UVXY', 'UWM', 'VB', 'VCIT', 'VCLT', 'VCSH', 'VDE', 'VEA','VEU', 'VGIT', 'VGK', 'VGLT', 'VGSH', 'VIG', 'VIXY', 'VLUE', 'VMBS', 'VNQ', 'VOO', 'VPL', 'VT', 'VTEB', 'VTI', 'VTIP', 'VTV', 'VTWO', 'VUG', 'VV', 'VWO', 'VXUS', 'VYM', 'XBI', 'XHB', 'XLB', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLU', 'XLV', 'XLY', 'XME', 'XOP', 'XRT', 'YANG', 'YINN']
    ##
    ##############################################################
    dollar3_ATR_most_liquid=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN',
                             'MARA', 'MRNA', 'MRVL','MSFT', 'MU', 'NVDA', 'ORCL', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT',
                             'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX']

    dollar3_ATR_s_p_500=['A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORCL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS']

    dollar3_dji=['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V']

    dollar3_nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM']
    dollar3_djtransport=['CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS']


    dollar3_etf=['ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']
    #################### with vol > 1Mill + 3ATR

    dollar3_ATR_most_liquid=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX']
    dollar3_ATR_s_p_500=['A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS']
    dollar3_dji=['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V']
    dollar3_nasdaq100=['AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM']
    dollar3_djtransport=['CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS']
    dollar3_etf=['ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']

    all=all=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']

    ########################
    print('#of stocks',len(all))

    pp=[]
    pp_buy=[]
    pp_sell=[]

    i=1


    for x in all:
        i=i+1
    ##    df=yf.download(x, period='1h', interval='1m')

        df=yf.Ticker(x).history(period ='1d', interval = '1m',prepost = True)
##        df=yf.Ticker(x).history(period ='20d', interval = '1d',prepost = True)
    ##    df=pd.DataFrame(df)    
        df['RSI']= ta.RSI(df['Close'], timeperiod=14)
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['fastk'], df['fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
        df['MA'] = ta.EMA(df['fastd'], timeperiod=14)
        df['MA2'] = ta.EMA(df['fastk'], timeperiod=14)
        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=0, maximum=0)
##        print(i,'   ',x)
##        print(i,'  ',x,'    ATR= ',round(df['ATR'][-1],2),' close= ',round(df['Close'][-1],2),'/',round(df['Close'][-1]-df['Close'].shift(1)[-1],2))
    ##    if df['ATR'][-2] > 3 :
    ##        pp.append(x)
    ##        
    ##    
##        if df['RSI'][-1] > 80:
        if df['fastd'][-1] > 80:
            pass
##            print(df)
##            print(x,' -vv----------------------------------------------  ','rsi=',df['fastd'][-1],'   sell','atr=',df['ATR'][-1],df['Close'][-1])
##            pp_buy.append(x)
        elif df['fastd'][-1] < 20:
##            pass
            if df['SAR'][-1] > df['Close'][-1]:
                print(x,' -UP/UP ------------------------------------------------  ','rsi=',df['fastd'][-1], ' / sar=',df['SAR'][-1],'    buy atr',
                  df['ATR'][-1],'close=',df['Close'][-1],'  ',df['MA'][-1],'/',df['MA2'][-1])
                pp_sell.append(x)

            elif df['SAR'][-1] < df['Close'][-1]:
                print(x,' -Down/UP ------------------------------------------------  ','rsi=',df['fastd'][-1], ' / sar=',df['SAR'][-1],'    buy atr',
                  df['ATR'][-1],'close=',df['Close'][-1],'  ',df['MA'][-1],'/',df['MA2'][-1])
                pp_sell.append(x)
##    print('comp')
##    print(pp)


def s4():
    import os, pandas
    import plotly.graph_objects as go
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import talib as ta

    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)

    print('jjj')
    alln=['aapl','t']
    pp_buy=[]
    pp_sell=[]
    
    for x in alln:
        df=yf.Ticker(x).history(period ='1d', interval = '1m',prepost = False)
        df=pd.DataFrame(df)

        
        
        df['RSI']= ta.RSI(df['Close'], timeperiod=14)
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['MOM']=ta.MOM(df['Close'], timeperiod=5)
        df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['EMA_21']=ta.EMA(df['Close'], timeperiod=21)
        df['EMA_slope']=df['EMA_3']-df['EMA_3'].shift(1)
##        print(df[['Close','ATR']])

        if df['RSI'][-1] > 80:
            print(x,' ---------------------------------  ','rsi=',df['RSI'][-1],'   sell ATR',df['ATR'][-1],'  ',df['Close'][-1])
            pp_buy.append(x)
        elif df['RSI'][-1] < 20:
            print(x,' ----------------------------------  ','rsi=',df['RSI'][-1],'    buy ATR',df['ATR'][-1],'   ',df['Close'][-1])
            pp_sell.append(x)



def s5():
    import os, pandas
    import plotly.graph_objects as go
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import talib as ta

    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=None
    pd.set_option("display.max_columns", 400)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 100)
    pd.set_option('display.max_columns', 0)
    pandas.set_option('display.max_columns', None)

    x='arkk'
    df=yf.Ticker(x).history(period ='1d', interval = '5m',prepost = True)
    df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=3)
    df['Simple MA_3'] = ta.SMA(df['Close'].astype(int),3).round(2)
    df['Simple MA_5'] = ta.SMA(df['Close'].astype(int),5).round(2)
    df['Simple MA_10'] = ta.SMA(df['Close'].astype(int),10).round(2)
    df['Simple MA_21'] = ta.SMA(df['Close'].astype(int),21).round(2)
    df['Simple MA_50'] = ta.SMA(df['Close'].astype(int),50).round(2)

    df['H_Bear_Rev_CDLABANDONEDBABY']=ta.CDLABANDONEDBABY(df['Open'],df['High'], df['Low'], df['Close'])

    df['H_Bear_Rev_CDL3OUTSIDE']=ta.CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bear_Rev_CDLKICKING']=ta.CDLKICKING(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bear_Rev_CDLDARKCLOUDCOVER']=ta.CDLDARKCLOUDCOVER(df['Open'],df['High'], df['Low'], df['Close'])

    df['H_Bear_Rev_CDLKICKING']=ta.CDLKICKING(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bear_Rev_CDL3BLACKCROWS']=ta.CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])

    df['M_Bear_Rev_CDL2CROWS']=ta.CDL2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
    df['M_Bear_Rev_CDLSTALLEDPATTERN']=ta.CDLSTALLEDPATTERN(df['Open'],df['High'], df['Low'], df['Close'])


    df['H_Bull_rev_CDLCONCEALBABYSWALL']=ta.CDLCONCEALBABYSWALL(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bull_rev_CDLMORNINGSTAR']=ta.CDLMORNINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bull_rev_CDL3WHITESOLDIERS']=ta.CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bull_rev_CDL3INSIDE']=ta.CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bull_rev_CDLMORNINGDOJISTAR']=ta.CDLMORNINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
    df['L_Bull_Rev_CDLHARAMICROSS']=ta.CDLHARAMICROSS(df['Open'],df['High'], df['Low'], df['Close'])
    df['L_Bull_Rev_CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
    df['L_Bull_Rev_CDLHARAMI']=ta.CDLHARAMI(df['Open'],df['High'], df['Low'], df['Close'])
    df['L_Bull_Rev_CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER (df['Open'],df['High'], df['Low'], df['Close'])
    df['H_Bull_continu_CDLRISEFALL3METHODS']=ta.CDLRISEFALL3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
    df['Mod_Bull_continu_CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
    df['L_Bull_continuation_CDLSEPARATINGLINES']=ta.CDLSEPARATINGLINES(df['Open'],df['High'], df['Low'], df['Close'])
    df['Mod_Bull_rev_CDLUNIQUE3RIVER']=ta.CDLUNIQUE3RIVER(df['Open'],df['High'], df['Low'], df['Close'])

    df['Med_Bull_Rev_CDLSTICKSANDWICH']=ta.CDLSTICKSANDWICH(df['Open'],df['High'], df['Low'], df['Close'])
    df['Med_Bull_Rev_CDLBREAKAWAY']=ta.CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
    df['Low_Rever_Contin_CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
    df['b']='*'
    print(df.columns,df.shape)
    df2=df.iloc[:,:]
    df2=df2[['Close','H_Bear_Rev_CDLABANDONEDBABY', 'H_Bear_Rev_CDL3OUTSIDE', 'H_Bear_Rev_CDLKICKING', 'H_Bear_Rev_CDLDARKCLOUDCOVER', 'H_Bear_Rev_CDL3BLACKCROWS', 'M_Bear_Rev_CDL2CROWS', 'M_Bear_Rev_CDLSTALLEDPATTERN', 'H_Bull_rev_CDLCONCEALBABYSWALL', 'H_Bull_rev_CDLMORNINGSTAR', 'H_Bull_rev_CDL3WHITESOLDIERS', 'H_Bull_rev_CDL3INSIDE', 'H_Bull_rev_CDLMORNINGDOJISTAR', 'L_Bull_Rev_CDLHARAMICROSS', 'L_Bull_Rev_CDLHAMMER', 'L_Bull_Rev_CDLHARAMI', 'L_Bull_Rev_CDLINVERTEDHAMMER', 'H_Bull_continu_CDLRISEFALL3METHODS', 'Mod_Bull_continu_CDLXSIDEGAP3METHODS', 'L_Bull_continuation_CDLSEPARATINGLINES', 'Mod_Bull_rev_CDLUNIQUE3RIVER', 'Med_Bull_Rev_CDLSTICKSANDWICH', 'Med_Bull_Rev_CDLBREAKAWAY', 'Low_Rever_Contin_CDLSPINNINGTOP']]
    
    
##    df2=df2[['Close','H_Bear_Rev_CDLABANDONEDBABY', 'H_Bear_Rev_CDL3OUTSIDE', 'H_Bear_Rev_CDLKICKING', 'H_Bear_Rev_CDLDARKCLOUDCOVER',
##             'H_Bear_Rev_CDL3BLACKCROWS', 'M_Bear_Rev_CDL2CROWS', 'M_Bear_Rev_CDLSTALLEDPATTERN']]
    print(df2)
##    
    

    
 #  CDLRISEFALL3METHODS
# https://www.quantshare.com/index.php?option=manual&dir=/QuantShare%20Language/Candlestick%20Pattern//CdlRisefall3methods%200.html

'''
##
##    #high bearish reveral
##    CDLABANDONEDBABY
##    CDL3OUTSIDE
##    CDLKICKING
##    CDLDARKCLOUDCOVER
##
##    #high nearish reversal
##    CDL3BLACKCROWS
##    CDLKICKING
##
##    # med bearish reversal
##    Cdl2crows
##    CDLSTALLEDPATTERN
##    CDLSTALLEDPATTERN
##
##    #moder bearush continuation
##    CDLTASUKIGAP
##    CDLINNECK
##    CDLONNECK



##    # low bullish continuation
##    CDLSEPARATINGLINES

##    # moder continuation bullish
##    CDLXSIDEGAP3METHODS

##    # moderate bullish reversal
##    CDLUNIQUE3RIVER

##    # high continuation bullish
##    CdlRisefall3methods

33
##    #high bullish revrsal
##    CDLCONCEALBABYSWALL
##    CDLMORNINGSTAR
##    
##    CDL3WHITESOLDIERS
##    CDL3INSIDE
##    CDLMORNINGDOJISTAR

##    #low bullish reversal
##    CDLHARAMICROSS
##    CDLHAMMER
##    CDLHARAMI
##    CdlInvertedhammer()
##    CDLINVERTEDHAMMER

    #low indecision
    CDLLONGLINE

    # low indecision reversal
    CDLSHORTLINE
    CDLSPINNINGTOP

    #low bearish reversal/conti
    CDLLONGLINE


    
    #moder bearish reversal
    CDLADVANCEBLOCK
    CDLGRAVESTONEDOJI

    #med reversal indecision
    CDLRICKSHAWMAN

    # low bearish/reversal continuatuib
    CDLMARUBOZU
    CDLDRAGONFLYDOJI

##    #low revresal contiunition:
##    CDLSPINNINGTOP    

##    # med bullish rev
##    CDLSTICKSANDWICH
##    CDLBREAKAWAY

    

CDLRISEFALL3METHODS


'''



##    df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLENGULFING']=ta.CDLENGULFING (df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLBREAKAWAY']=ta.CDLBREAKAWAY (df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI (df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER (df['Open'],df['High'], df['Low'], df['Close'])

##
##    
##    df['CDL3BLACKCROWS']=ta.CDL3BLACKCROWS(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDL3INSIDE']=ta.CDL3INSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDL3LINESTRIKE']=ta.CDL3LINESTRIKE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDL3OUTSIDE']=ta.CDL3OUTSIDE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDL3STARSINSOUTH']=ta.CDL3STARSINSOUTH(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDL3WHITESOLDIERS']=ta.CDL3WHITESOLDIERS(df['Open'],df['High'], df['Low'], df['Close'])
##    
##    df['CDLADVANCEBLOCK']=ta.CDLADVANCEBLOCK(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLBREAKAWAY']=ta.CDLBREAKAWAY(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLCLOSINGMARUBOZU']=ta.CDLCLOSINGMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
##    
##    df['CDLCOUNTERATTACK']=ta.CDLCOUNTERATTACK(df['Open'],df['High'], df['Low'], df['Close'])
##    
##    df['CDLDOJI']=ta.CDLDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLDOJISTAR']=ta.CDLDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLDRAGONFLYDOJI']=ta.CDLDRAGONFLYDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLENGULFING']=ta.CDLENGULFING(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLEVENINGDOJISTAR']=ta.CDLEVENINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLEVENINGSTAR']=ta.CDLEVENINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLGAPSIDESIDEWHITE']=ta.CDLGAPSIDESIDEWHITE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLGRAVESTONEDOJI']=ta.CDLGRAVESTONEDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHAMMER']=ta.CDLHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHANGINGMAN']=ta.CDLHANGINGMAN(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHARAMI']=ta.CDLHARAMI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHARAMICROSS']=ta.CDLHARAMICROSS(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHIGHWAVE']=ta.CDLHIGHWAVE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHIKKAKE']=ta.CDLHIKKAKE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHIKKAKEMOD']=ta.CDLHIKKAKEMOD(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLHOMINGPIGEON']=ta.CDLHOMINGPIGEON(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLIDENTICAL3CROWS']=ta.CDLIDENTICAL3CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLINNECK']=ta.CDLINNECK(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLINVERTEDHAMMER']=ta.CDLINVERTEDHAMMER(df['Open'],df['High'], df['Low'], df['Close'])
##    
##    df['CDLKICKINGBYLENGTH']=ta.CDLKICKINGBYLENGTH(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLLADDERBOTTOM']=ta.CDLLADDERBOTTOM(df['Open'],df['High'], df['Low'], df['Close'])
##
##    df['CDLLONGLEGGEDDOJI']=ta.CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLLONGLINE']=ta.CDLLONGLINE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLMARUBOZU']=ta.CDLMARUBOZU(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLMATCHINGLOW']=ta.CDLMATCHINGLOW(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLMATHOLD']=ta.CDLMATHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLMORNINGDOJISTAR']=ta.CDLMORNINGDOJISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLMORNINGSTAR']=ta.CDLMORNINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLONNECK']=ta.CDLONNECK(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLPIERCING']=ta.CDLPIERCING(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLRICKSHAWMAN']=ta.CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
##
##    df['CDLSEPARATINGLINES']=ta.CDLSEPARATINGLINES(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLSHOOTINGSTAR']=ta.CDLSHOOTINGSTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLSHORTLINE']=ta.CDLSHORTLINE(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLSPINNINGTOP']=ta.CDLSPINNINGTOP(df['Open'],df['High'], df['Low'], df['Close'])
##    
##    df['CDLSTICKSANDWICH']=ta.CDLSTICKSANDWICH(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLTAKURI']=ta.CDLTAKURI(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLTASUKIGAP']=ta.CDLTASUKIGAP(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLTHRUSTING']=ta.CDLTHRUSTING(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLTRISTAR']=ta.CDLTRISTAR(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLUNIQUE3RIVER']=ta.CDLUNIQUE3RIVER(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLUPSIDEGAP2CROWS']=ta.CDLUPSIDEGAP2CROWS(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLXSIDEGAP3METHODS']=ta.CDLXSIDEGAP3METHODS(df['Open'],df['High'], df['Low'], df['Close'])
##
##    df['CDLBELTHOLD']=ta.CDLBELTHOLD(df['Open'],df['High'], df['Low'], df['Close'])
##    df['CDLRICKSHAWMAN']=ta.CDLRICKSHAWMAN(df['Open'],df['High'], df['Low'], df['Close'])
##    df['Reversal']=ta.CDLLONGLEGGEDDOJI(df['Open'],df['High'], df['Low'], df['Close'])

##    df3=df[['Simple MA_5', 'Simple MA_10', 'Simple MA_21', 'Simple MA_50', 'CDLDOJI', 'CDLHAMMER', 'CDLDOJISTAR', 'CDLENGULFING', 'CDLBREAKAWAY', 'CDLGRAVESTONEDOJI', 'CDLINVERTEDHAMMER', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK']]
##    df4=df[[ 'CDLBELTHOLD', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDRAGONFLYDOJI',
##             'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS',
##             'CDLHIGHWAVE', 'CDLHIKKAKE']]
##    df5=df[['CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLKICKING', 'CDLKICKINGBYLENGTH',
##          'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR']]
##    df6=df[['CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN',
##       'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH']]
##    df7=df[['CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN',
##       'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH']]
##    df8=df[['CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'Reversal']]     
##    print(df3.tail(20),df4.tail(20),df5.tail(20),df6.tail(20),df7.tail(20),df8.tail(20))
    
    
s5()
