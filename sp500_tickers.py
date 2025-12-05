"""
S&P 500 Ticker List
Updated: January 2025
Source: Manual curation of S&P 500 constituents
"""

SP500_TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'BRK-B', 'UNH',
    'XOM', 'JNJ', 'V', 'WMT', 'JPM', 'LLY', 'MA', 'PG', 'AVGO', 'HD',
    'CVX', 'MRK', 'ABBV', 'COST', 'KO', 'PEP', 'ADBE', 'TMO', 'MCD', 'CSCO',
    'ACN', 'ABT', 'WFC', 'DIS', 'CRM', 'VZ', 'DHR', 'CMCSA', 'NKE', 'NEE',
    'TXN', 'ORCL', 'INTC', 'PM', 'UPS', 'HON', 'RTX', 'UNP', 'COP', 'QCOM',
    'BA', 'INTU', 'LOW', 'AMD', 'AMGN', 'ELV', 'CAT', 'SPGI', 'GE', 'LMT',
    'SBUX', 'PLD', 'AXP', 'BLK', 'DE', 'ADI', 'MDLZ', 'GILD', 'BKNG', 'TJX',
    'CI', 'ADP', 'SYK', 'REGN', 'MMC', 'VRTX', 'C', 'ZTS', 'MO', 'CB',
    'ISRG', 'PGR', 'BMY', 'SCHW', 'SO', 'NOC', 'DUK', 'ETN', 'GS', 'BDX',
    'SLB', 'TGT', 'ITW', 'LRCX', 'USB', 'PNC', 'MS', 'MMM', 'FI', 'BSX',
    'APD', 'EOG', 'MDT', 'CME', 'ICE', 'MU', 'PH', 'WM', 'NSC', 'CL',
    'EMR', 'PYPL', 'AON', 'MCK', 'SHW', 'KLAC', 'MAR', 'COF', 'SNPS', 'PSX',
    'AJG', 'GM', 'ECL', 'TT', 'HCA', 'EQIX', 'ORLY', 'AFL', 'CMG', 'MSI',
    'OXY', 'NXPI', 'AIG', 'GEV', 'FCX', 'ADM', 'TFC', 'MCO', 'AMP', 'AZO',
    'TDG', 'PSA', 'WELL', 'JCI', 'SRE', 'APH', 'MPC', 'D', 'HUM', 'SPG',
    'ALL', 'TEL', 'AEP', 'PAYX', 'CARR', 'MSCI', 'ANET', 'FTNT', 'ROP', 'ROST',
    'OTIS', 'RSG', 'HLT', 'TRV', 'PRU', 'CDNS', 'DLR', 'EW', 'KMB', 'O',
    'PEG', 'FIS', 'BK', 'GIS', 'FAST', 'BKR', 'CTVA', 'PCAR', 'KR', 'CTAS',
    'CCI', 'NEM', 'KMI', 'COR', 'KHC', 'AMT', 'HPQ', 'VRSK', 'STZ', 'F',
    'VST', 'SYY', 'CTSH', 'GWW', 'IT', 'CMI', 'PPG', 'GLW', 'YUM', 'HWM',
    'AME', 'ACGL', 'A', 'EA', 'DHI', 'KVUE', 'HSY', 'EXC', 'WMB', 'IQV',
    'PWR', 'LHX', 'DAL', 'DG', 'WBD', 'VLO', 'RMD', 'ED', 'IDXX', 'DOW',
    'VMC', 'MLM', 'PCG', 'CBRE', 'DD', 'XEL', 'ANSS', 'ROK', 'HAL', 'VICI',
    'IR', 'LEN', 'MTD', 'EXR', 'CPRT', 'AWK', 'AEE', 'LVS', 'CHTR', 'WEC',
    'GEHC', 'FDX', 'EIX', 'DOV', 'TSCO', 'ETR', 'KEYS', 'CDW', 'TTWO', 'TROW',
    'DFS', 'DVN', 'MPWR', 'WAB', 'BRO', 'PPL', 'KDP', 'STT', 'AXON', 'CHD',
    'LYB', 'VLTO', 'EBAY', 'CAH', 'WY', 'RCL', 'WAT', 'SBAC', 'EFX', 'HPE',
    'URI', 'WTW', 'TYL', 'BR', 'CNP', 'BAX', 'GPN', 'MTB', 'IFF', 'ZBH',
    'DTE', 'XYL', 'HUBB', 'FTV', 'HOLX', 'FSLR', 'LUV', 'LDOS', 'TRGP', 'EQR',
    'HBAN', 'FE', 'CCL', 'ES', 'BALL', 'CINF', 'EXPE', 'K', 'PFG', 'IRM',
    'INVH', 'WDC', 'STLD', 'DRI', 'NTRS', 'OMC', 'APTV', 'AVB', 'IP', 'STE',
    'SYF', 'ATO', 'CFG', 'ARE', 'RF', 'MAA', 'FITB', 'AES', 'PKG', 'EXPD',
    'DGX', 'TXT', 'CAG', 'CBOE', 'WST', 'NDAQ', 'BLDR', 'LH', 'ULTA', 'PNR',
    'CNM', 'CLX', 'MOH', 'WRB', 'AMCR', 'MKC', 'BBWI', 'ESS', 'CMS', 'NUE',
    'FDS', 'LYV', 'VTR', 'TSN', 'CE', 'GRMN', 'JBHT', 'NI', 'CTRA', 'SNA',
    'AKAM', 'EMN', 'REG', 'CF', 'J', 'CPT', 'LNT', 'MAS', 'L', 'FICO',
    'ALGN', 'KEY', 'EVRG', 'PODD', 'AIZ', 'EPAM', 'PTC', 'BBY', 'NTAP', 'SWKS',
    'HIG', 'CHRW', 'SWK', 'BXP', 'TER', 'MRNA', 'VTRS', 'JKHY', 'POOL', 'GEN',
    'KIM', 'UDR', 'GL', 'ZBRA', 'PAYC', 'HST', 'TPR', 'TECH', 'BG', 'UHS',
    'AOS', 'BEN', 'HRL', 'ALB', 'ALLE', 'MKTX', 'CTLT', 'FFIV', 'IPG', 'CPB',
    'BWA', 'TAP', 'NDSN', 'HSIC', 'INCY', 'CRL', 'MOS', 'HII', 'LW', 'PARA',
    'IVZ', 'MTCH', 'NRG', 'PNW', 'AAL', 'BIO', 'FRT', 'WYNN', 'WBA', 'NWSA',
    'NWS', 'FOX', 'FOXA', 'QRVO', 'AIV'
]

def get_sp500_tickers():
    """
    Returns a list of S&P 500 ticker symbols.
    
    Returns:
        list: S&P 500 ticker symbols
    """
    return SP500_TICKERS.copy()