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
######pd.set_option('display.max_colwidth', 200)
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

    alls=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    all=['spy','tna','mstr','coin']
    ########################
    print('#of stocks',len(all))

    pp=[]
    pp_buy=[]
    pp_sell=[]

    i=1


    for x in all:
        print(x)
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
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)

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
    import sys
    import warnings
    warnings.filterwarnings("ignore")

    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns=255
    pd.options.display.max_rows=6500000

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)
    pd.set_option('display.max_columns', None)


##    print('jjj')
##    alln=['aapl','t']
    allb=['AAPL', 'AFRM', 'AMAT', 'AMC', 'AMD', 'BA', 'BABA', 'DIS', 'FB', 'FUTU', 'IWM', 'JD', 'JPM', 'LCID', 'LGVN', 'MARA', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NVDA', 'PDD', 'PLUG', 'PTON', 'PYPL', 'QCOM', 'QQQ', 'RBLX', 'RIOT', 'SAVA', 'SOXL', 'SPXL', 'SPY', 'SQ', 'TNA', 'TQQQ', 'TSLA', 'TSM', 'V', 'XLK', 'XOP', 'XPEV', 'Z', 'MRNA', 'BNTX'
    ,'A', 'AAP', 'AAPL', 'ABMD', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AIZ', 'AJG', 'ALB', 'ALGN', 'ALLE', 'AMAT', 'AMD', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'APD', 'APTV', 'ARE', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BBY', 'BDX', 'BIIB', 'BIO', 'BKNG', 'BLK', 'BR', 'BXP', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CDNS', 'CDW', 'CE', 'CHTR', 'CI', 'CLX', 'CME', 'CMG', 'CMI', 'COF', 'COO', 'COST', 'CPRT', 'CRL', 'CRM', 'CTAS', 'CTLT', 'CZR', 'DE', 'DFS', 'DG', 'DGX', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DVA', 'DXCM', 'EA', 'ECL', 'EFX', 'EL', 'EMN', 'ENPH', 'EOG', 'EQIX', 'ESS', 'ETN', 'ETSY', 'EW', 'EXPD', 'EXPE', 'EXR', 'FANG', 'FB', 'FDX', 'FFIV', 'FIS', 'FLT', 'FRC', 'FRT', 'FTNT', 'GD', 'GNRC', 'GOOG', 'GOOGL', 'GPN', 'GRMN', 'GS', 'GWW', 'HCA', 'HD', 'HES', 'HII', 'HLT', 'HON', 'HUM', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INFO', 'INTU', 'IPGP', 'IQV', 'ISRG', 'IT', 'ITW', 'J', 'JBHT', 'JKHY', 'JPM', 'KEYS', 'KLAC', 'KMX', 'KSU', 'LEN', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LYV', 'MA', 'MAA', 'MAR', 'MCD', 'MCK', 'MCO', 'MHK', 'MKTX', 'MLM', 'MMC', 'MMM', 'MPWR', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NDAQ', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ODFL', 'ORLY', 'PAYC', 'PH', 'PKI', 'PLD', 'PNC', 'POOL', 'PPG', 'PSA', 'PTC', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REGN', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'SBAC', 'SHW', 'SIVB', 'SNA', 'SNPS', 'SPG', 'SPGI', 'STE', 'STX', 'STZ', 'SWK', 'SWKS', 'SYK', 'TDG', 'TDY', 'TEL', 'TER', 'TFX', 'TGT', 'TMO', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TTWO', 'TXN', 'TYL', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'V', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'WAT', 'WHR', 'WLTW', 'WST', 'WYNN', 'XLNX', 'ZBH', 'ZBRA', 'ZTS'
    ,'AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'DIS', 'GS', 'HD', 'HON', 'JPM', 'MCD', 'MMM', 'MSFT', 'NKE', 'TRV', 'UNH', 'V'
    ,'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ASML', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'CDNS', 'CDW', 'CHTR', 'COST', 'CPRT', 'CTAS', 'DLTR', 'DOCU', 'DXCM', 'EA', 'FB', 'GOOG', 'GOOGL', 'IDXX', 'ILMN', 'INTU', 'ISRG', 'JD', 'KLAC', 'LRCX', 'LULU', 'MAR', 'MELI', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'OKTA', 'ORLY', 'PDD', 'PTON', 'PYPL', 'QCOM', 'REGN', 'ROST', 'SGEN', 'SPLK', 'SWKS', 'TEAM', 'TSLA', 'TXN', 'VRSK', 'VRSN', 'VRTX', 'WDAY', 'XLNX', 'ZM'
    ,'CAR', 'EXPD', 'FDX', 'JBHT', 'KSU', 'LSTR', 'NSC', 'UNP', 'UPS'
    ,'ARKG', 'ARKK', 'ARKW', 'BOIL', 'DIA', 'FAS', 'GUSH', 'IBB', 'IGV', 'IJH', 'IVV', 'IWB', 'IWF', 'IWM', 'IWN', 'IWO', 'JNUG', 'LABU', 'MDY', 'MTUM', 'OIH', 'QLD', 'QQQ', 'SMH', 'SOXL', 'SPXL', 'SPY', 'SSO', 'TAN', 'TECL', 'TNA', 'TQQQ', 'UPRO', 'VB', 'VOO', 'VTI', 'VUG', 'XBI', 'XLK', 'XLY', 'XOP']


    allv=['spy','tna','mstr','coin','tsla']
    all=['ba','adbe','tsla']
    pp_buy=[]
    pp_sell=[]
    

    print('# of stocks being checked: ',len(all))
    i=0
    i2=0
    for x in all:
        print(x)
        df=yf.Ticker(x).history(period ='5d', interval = '1m',prepost = False)
        df=pd.DataFrame(df)
        print(df)

        
        i=i+1

        df=df[df.index.astype(str).str.contains('2021-12-07')]
##        print(df)

##        sys.exit()

        df['Boling_upper2']=''
        df['Boling__middle2']=''
        df['Boling_lower2']=''
        df['x']=''
        df['SARx']=''
        df['ADX_over25_strong_less25_weak_trend']=''

        df['aroondown'],df['aroonup']=ta.AROON(df['High'],df['Low'], timeperiod=14)

        df['CCI']=ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['RSI']= ta.RSI(df['Close'], timeperiod=14)
        df['ATR']=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['MOM']=ta.MOM(df['Close'], timeperiod=3)
        df['MOM_slope']=df['MOM']-df['MOM'].shift(1)
        df['EMA_3']=ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5']=ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10']=ta.EMA(df['Close'], timeperiod=10)
        df['EMA_50']=ta.EMA(df['Close'], timeperiod=50)
        df['EMA_21']=ta.EMA(df['Close'], timeperiod=21)
        df['EMA_slope']=df['EMA_3']-df['EMA_3'].shift(1)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['adx']= ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)

        df['EMA-35']=df['EMA_3']-df['EMA_5']



        df['fastk'], df['fastd'] = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
        df['MA'] = ta.EMA(df['fastd'], timeperiod=14)
        df['MA2'] = ta.EMA(df['fastk'], timeperiod=14)
        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=90, maximum=5)
        df['Boling_upper'], df['Boling__middle'], df['Boling_lower'] = ta.BBANDS(df['High'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)
        df['SARx']=df['Close']-df['SAR']
        df['ADX_over25_strong_less25_weak_trend']=ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=3).round(2)
        df['ticker']=x


            
        df=df[['ticker','High','Close','Low','x','SARx','Boling_upper','Boling_lower2','SAR','CCI','ATR','MOM','MOM_slope',\
               'ADX_over25_strong_less25_weak_trend',\
               'macd', 'macdsignal', 'macdhist','adx','EMA-35','EMA_3','EMA_5','EMA_21','EMA_10','EMA_50',
                'aroondown','aroonup'
               ]]
        df3=df
        g6=pd.DataFrame()
        g7=pd.DataFrame()
##        print(df3)

        
        
        c=vv(df,g6,g7)
##        pp=pp.append(c,ignore_index=False)
        return(c)


    
          

def vv(df,g6,g7):
    import time
    
    i2='51'
    ##        SAR reversal
    df.reset_index(inplace=True)

    m2=[];m3=[];m4=[]

    for x in df.index:
        

##        print(df['ticker'].loc[x],df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
##                  round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
##                  round(df['CCI'].loc[x],2),\
##                  '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
##                  '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),
##                  round(df['aroondown'].loc[x],2),round(df['aroonup'].loc[x],2)

##              )
        
##        if  df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['SAR'].shift(1).loc[x] - df['Close'].shift(1).loc[x] > 0 and\
##        df['CCI'].loc[x] > 100 :

######################################################################################################################################
        if i2=='51':   # Sell condition
##            pb=df['MOM'].loc[x]-df['MOM'].shift(1).loc[x] > 0
            sell=df['Close'].loc[x]>df['Close'].shift(1).loc[x] and df['MOM'].loc[x]>df['MOM'].shift(1).loc[x] and\
                df['EMA_5'].loc[x]>df['EMA_5'].shift(1).loc[x] and df['MOM'].loc[x]>df['MOM'].shift(2).loc[x]
            
##            uu=df['Low'].loc[x]-df['Low'].shift(1).loc[x] > 0 and df['Low'].shift(1).loc[x]-df['Low'].shift(2).loc[x]>0

            if sell:
                
##            if df['aroonup'].loc[x] < 70:
##            if df['MOM'].loc[x]-df['MOM'].shift(1).loc[x]>.1 and\
##               df['CCI'].loc[x]<-70:
#######################################################################################################################################               
##               df['SAR'].loc[x]>df['SAR'].shift(1).loc[x]and\
               
            
            
####               df['Low'].loc[x]-df['EMA_3'].loc[x] > 0\
####               and\
##            if df['Close'].loc[x]-df['EMA_3'].loc[x] > 0\
##               and\
##               df['Close'].shift(1).loc[x]-df['EMA_5'].shift(1).loc[x] < 0 and\
##               df['MOM'].loc[x]>df['MOM'].shift(1).loc[x]\
##               and\
##               df['SAR'].loc[x]-df['Close'].loc[x] <0 :
            ##            df['EMA_10'].loc[x]-df['EMA_21'].loc[x] > 0 and df['EMA_10'].shift(1).loc[x]-df['EMA_21'].shift(1).loc[x]>0
##            and
##            df['EMA_21'].loc[x]-df['EMA_50'].loc[x] > 0 and df['EMA_21'].shift(1).loc[x]-df['EMA_50'].shift(1).loc[x]>0
##            and
        

            

##            if df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['MOM'].loc[x] - df['MOM'].shift(1).loc[x] > 0 and df['Close'].loc[x] > df['EMA_3'].loc[x]\
##               and df['Close'].loc[x] > df['EMA_5'].loc[x] and df['Close'].loc[x] > df['EMA_10'].loc[x] and df['Close'].loc[x] > df['EMA_21'].loc[x]\
##               and df['Close'].loc[x] > df['EMA_3'].shift(1).loc[x]\
##               and df['EMA_3'].loc[x]>df['EMA_5'].loc[x] and df['EMA_5'].loc[x]>df['EMA_10'].loc[x]and df['EMA_10'].loc[x]>df['EMA_21'].loc[x]:
##            
            
                
##            if df['macdsignal'].loc[x] > 0 and (df['macdsignal'].shift(1).loc[x] < 0 and df['macdsignal'].shift(2).loc[x] < 0  and df['CCI'].loc[x] < -100):
       


                i2='53'

##                print('\n')
##                print('------BUY------------------------------------------------------------------------------------------------------')
##                print(i2,'****macd up -- cci100-sar-reversal-down*********',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
##                      round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
##                      round(df['CCI'].loc[x],2),\
##                      '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
##                      '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    UP')
##
##                print('------------------------------------------------------------------------------------------------------------')
##                
                v4=df['Close'].loc[x]   # v4 is sell

#########################################################################################################################################################
        if i2=='53':    # Buy condition
            uu=df['Low'].loc[x] < df['EMA_50'].loc[x] and df['Low'].loc[x] < df['EMA_21'].loc[x] and df['Low'].loc[x] < df['Low'].shift(1).loc[x]
            uu2=df['Low'].loc[x]<df['Low'].shift(1).loc[x] and df['Low'].shift(1).loc[x]  < df['Low'].shift(2).loc[x] and df['High'].loc[x] <\
                df['EMA_50'].loc[x]

# downtred
            uu3b=df['Close'].loc[x] < df['Close'].shift(1).loc[x]  and df['EMA_50'].loc[x] < df['EMA_50'].shift(1).loc[x] and\
                 df['MOM'].loc[x] < df['MOM'].shift(1).loc[x]
            
            uu3=df['Close'].loc[x] < df['Close'].shift(1).loc[x] and df['Close'].loc[x] < df['EMA_21'].loc[x] \
                 and df['Close'].loc[x] < df['EMA_10'].loc[x] and df['Close'].loc[x] > df['EMA_50'].loc[x]\
                 and df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and df['CCI'].loc[x]<-130

            if uu3:

##            if df['aroonup'].loc[x] == 100:
###############################################################################################################################################                
                
##               df['MOM'].loc[x] < df['MOM'].shift(1).loc[x] and\
##               df['SAR'].loc[x]<df['SAR'].shift(1).loc[x]:
            
##            if df['macdsignal'].loc[x] < 0 :
##                print('\n')
##                print(i2,' Sell %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                v5=df['Close'].loc[x] #v5 is buy
                v6=df['CCI'].loc[x]
                profit=(v5-v4)

##                print(df['ticker'].loc[x],v4.round(2),v5.round(2),' profit-----> ',profit.round(2))
##                pp=pp.append(df['ticker'].loc[x],v4.round(2),v5.round(2),profit.round(2))
                xm=pd.Series(str(df['ticker'].loc[x]))
                x2=pd.Series(v5.round(2))
                x3=pd.Series(v4.round(2))
                x4=pd.Series(profit.round(2))
                x5=pd.Series(v6.round(2))


##                time.sleep(2)

                
                    
                
##                if profit < 0:
####                    time.sleep(4)
                i2='51'

                g6=pd.concat([xm,x2,x3,x4,x5],axis=1)
                g7a=g6
                
##                print(g7a.T)

##                pp=pp.append((xm,x2,x3,x4),ignore_index=False)
##                print(g6,'\n',g6.shape,'\n','g6.....dataframe g6................')

                
         

                g7=g7.append(g7a,ignore_index=True)
##                print(g7)
                
    return(g7)           
##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
##            print(x,' cci100-sar-reversal-down   ',df['ticker'].loc[x],' No  ',df['Close'].loc[x],i2,' / ',round(df['SAR'].loc[x],2))
##

##        if  df['SAR'].loc[x] - df['Close'].loc[x] > 0 and df['SAR'].shift(1).loc[x] - df['Close'].shift(1).loc[x] < 0 and\
##                df['CCI'].loc[x] < -100 :

##                    elif df['macdsignal'].loc[x] < 0 and (df['macdsignal'].shift(1).loc[x] > 0 and df['macdsignal'].shift(2).loc[x] > 0):
##                        print('c3b  ',len(c3b))
##                        if len(c3) >0:
##                            print('************************************************************8 c4=',df['Close'][c4[0]],'  ',df['Close'][c4[-1]])
##                        c3=[] 
##                        profit3=df['Close'].loc[x]
##
##                        
##                        print('----profit/loss--------------------------------------------------------------------------------------------------------')
##            ##            print(profit3-profit2)
##                        print('----D--------------------------------------------------------------------------------------------------------')
##                        
##                    
##            ##        and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
##            ##           and df['ATR'].loc[x] > 2
##            ##        :
##                        i2=i2+1
##                        sell.append(x)
##                        print('----D--------------------------------------------------------------------------------------------------------')
##                        print('********macd down*****SAR reversal up**********''',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
##                              round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
##                              round(df['CCI'].loc[x],2),\
##                              '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
##                              '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    Down')
##                        print('------------------------------------------------------------------------------------------------------------')
##                        k2=1
##                    elif df['macdsignal'].loc[x] < 0 and (df['macdsignal'].shift(1).loc[x] < 0 and df['macdsignal'].shift(2).loc[x] < 0 ):
##                        k2=k2+1
##                        c3.append(x)
##                        print('U',df['Datetime'].loc[x],round(df['Close'].loc[x],2),i2,' SAR ',\
##                              round(df['SARx'].loc[x],2),' MOM ',round(df['MOM'].loc[x],2),' CCI',\
##                              round(df['CCI'].loc[x],2),\
##                              '  macd ',round(df['macd'].loc[x],2), round(df['macdsignal'].loc[x],2),round(df['macdhist'].loc[x],2),\
##                              '  adx',round(df['adx'].loc[x],2),' ema35',round(df['EMA-35'].loc[x],2),'    Down')

            
##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
##            
##            print(x,'    ',df['ticker'].loc[x],' No ',df['Close'].loc[x],i2,'  ',round(df['SAR'].loc[x],2))
##


        
##        if df['High'].loc[x] >= df['Boling_upper'].loc[x] and df['SAR'].loc[x] - df['Close'].loc[x] < 0:
####        and df['Close'].loc[x]<df['Close'].shift(1).loc[x] and\
####        df['CCI'].loc[x] > 200 and df['ATR'].loc[x]>2
####        :
##            i2=i2+1
##            cc=df['Close']
##            buy.append(x)
##            print('************** Bolinger_High ',df['Close'].loc[x],i2,'  ',x,'  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2),'  ',round(df['High'].loc[x],2),'/',round(df['Boling_upper'][-1],2))
##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
##            print(x,'    ',df['ticker'].loc[x],' No  ',round(df['Close'].loc[x],2),'  ',round(df['SAR'].loc[x] - df['Close'].loc[x],2),
##                  '  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2))
##
##
##        if df['Low'].loc[x] <= df['Boling_lower2'].loc[x] and df['SAR'].loc[x]> df['Close'].loc[x]:
####        and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
####           and df['ATR'].loc[x] > 2
####        :
##            i2=i2+1
##            sell.append(x)
##            print('################### Bolinger_Low ',i2,'  ',x,'  ',round(df['Low'].loc[x]-df['Boling_lower2'].loc[x],2),'  ',
##                  round(df['Low'].loc[x],2),'/',round(df['Boling_lower2'].loc[x],2))
##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
##            
##            print(x,'    ',df['ticker'].loc[x],' No ',round(df['Close'].loc[x],2),'  ',round(df['SAR'].loc[x] - df['Close'].loc[x],2))


##    sleep(10)    



##
##    for x in df.index:
##        
##        if df['High'].loc[x] >= df['Boling_upper'].loc[x] and df['SAR'].loc[x] - df['Close'].loc[x] < 0 and df['Close'].loc[x]<df['Close'].shift(1).loc[x] and\
##        df['CCI'].loc[x] > 200 and df['ATR'].loc[x]>2 :
##            i2=i2+1
##            buy.append(x)
##            print('Bolinger_High ',i2,'  ',x,'  ',round(df['High'].loc[x]-df['Boling_upper'].loc[x],2),'  ',round(df['High'].loc[x],2),'/',round(df['Boling_upper'][-1],2))
##        elif df['High'].loc[x] < df['Boling_upper'].loc[x]:
##            print(x,'    ',df['ticker'].loc[x],' No')
##
##
##        if df['Low'].loc[x] <= df['Boling_lower2'].loc[x] and df['SAR'].loc[x]> df['Close'].loc[x] and df['Close'].loc[x]> df['Close'].shift(1).loc[x] and df['CCI'].loc[x]< -200 \
##           and df['ATR'].loc[x] > 2 :
##            i2=i2+1
##            sell.append(x)
##            print('Bolinger_Low ',i2,'  ',x,'  ',round(df['Low'].loc[x]-df['Boling_lower2'].loc[x],2),'  ',
##                  round(df['Low'].loc[x],2),'/',round(df['Boling_lower2'].loc[x],2))
##        elif df['High'].loc[x] > df['Boling_lower2'].loc[x]:
##            print(x,'    ',df['ticker'].loc[x],' No')



##    return(buy,sell)  

b=s4()


print('\n\n\n')
print('***************************************************************************')
print('this is coming from bottom/main','\n')
##b=columns['purchase_price','Sell_price','Profot']
b.sort_values(by=[3])
print(b)




