import yfinance as yf

stock = yf.Ticker("MSFT")
print(stock.info)

{'zip': '98052-6399', 'sector': 'Technology', 'fullTimeEmployees': 181000, 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for organizations and enterprise divisions. Its Intelligent Cloud segment licenses SQL, Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification on Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. It has collaborations with Dynatrace, Inc., Morgan Stanley, Micro Focus, WPP plc, ACI Worldwide, Inc., and iCIMS, Inc., as well as strategic relationships with Avaya Holdings Corp. and wejo Limited. Microsoft Corporation was founded in 1975 and is based in Redmond, Washington.', 'city': 'Redmond', 'phone': '425 882 8080', 'state': 'WA', 'country': 'United States', 'companyOfficers': [], 'website': 'https://www.microsoft.com', 'maxAge': 1, 'address1': 'One Microsoft Way', 'industry': 'Software—Infrastructure', 'ebitdaMargins': 0.48648998, 'profitMargins': 0.38515, 'grossMargins': 0.68864995, 'operatingCashflow': 81945001984, 'revenueGrowth': 0.22, 'operatingMargins': 0.42143002, 'ebitda': 85745000448, 'targetLowPrice': 299.93, 'recommendationKey': 'buy', 'grossProfits': 115856000000, 'freeCashflow': 49819750400, 'targetMedianPrice': 368, 'currentPrice': 316.38, 'earningsGrowth': 0.489, 'currentRatio': 2.165, 'returnOnAssets': 0.14589, 'numberOfAnalystOpinions': 42, 'targetMeanPrice': 369.86, 'debtToEquity': 51.938, 'returnOnEquity': 0.49303, 'targetHighPrice': 412.07, 'totalCash': 130584002560, 'totalDebt': 78934999040, 'totalRevenue': 176250994688, 'totalCashPerShare': 17.393, 'financialCurrency': 'USD', 'revenuePerShare': 23.395, 'quickRatio': 1.961, 'recommendationMean': 1.6, 'exchange': 'NMS', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 13.722, 'beta3Year': None, 'enterpriseToEbitda': 28.206, '52WeekChange': 0.50721514, 'morningStarRiskRating': None, 'forwardEps': 10.54, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7507979776, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'totalAssets': None, 'bookValue': 20.242, 'sharesShort': 42981645, 'sharesPercentSharesOut': 0.0057, 'fundFamily': None, 'lastFiscalYearEnd': 1625011200, 'heldPercentInstitutions': 0.71769994, 'netIncomeToCommon': 67882999808, 'trailingEps': 8.939, 'lastDividendValue': 0.62, 'SandP52WeekChange': 0.26020098, 'priceToBook': 15.629878, 'heldPercentInsiders': 0.00062, 'nextFiscalYearEnd': 1688083200, 'yield': None, 'mostRecentQuarter': 1632960000, 'shortRatio': 1.48, 'sharesShortPreviousMonthDate': 1636934400, 'floatShares': 7501148182, 'beta': 0.872727, 'enterpriseValue': 2418551554048, 'priceHint': 2, 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400, 'lastSplitFactor': '2:1', 'legalType': None, 'lastDividendDate': 1637107200, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.476, 'priceToSalesTrailing12Months': 13.477226, 'dateShortInterest': 1639526400, 'pegRatio': 2.16, 'ytdReturn': None, 'forwardPE': 30.017078, 'lastCapGain': None, 'shortPercentOfFloat': 0.0057, 'sharesShortPriorMonth': 41195079, 'impliedSharesOutstanding': None, 'category': None, 'fiveYearAverageReturn': None, 'previousClose': 329.01, 'regularMarketOpen': 325.86, 'twoHundredDayAverage': 288.4612, 'trailingAnnualDividendYield': 0.006990669, 'payoutRatio': 0.25059998, 'volume24Hr': None, 'regularMarketDayHigh': 326.07, 'navPrice': None, 'averageDailyVolume10Day': 21536090, 'regularMarketPreviousClose': 329.01, 'fiftyDayAverage': 332.724, 'trailingAnnualDividendRate': 2.3, 'open': 325.86, 'toCurrency': None, 'averageVolume10days': 21536090, 'expireDate': None, 'algorithm': None, 'dividendRate': 2.48, 'exDividendDate': 1644969600, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 315.98, 'currency': 'USD', 'trailingPE': 35.39322, 'regularMarketVolume': 39662628, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 2375374602240, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 25791530, 'dayLow': 315.98, 'ask': 317.6, 'askSize': 1000, 'volume': 39662628, 'fiftyTwoWeekHigh': 349.67, 'fromCurrency': None, 'fiveYearAvgDividendYield': 1.39, 'fiftyTwoWeekLow': 212.03, 'bid': 316.5, 'tradeable': False, 'dividendYield': 0.0075, 'bidSize': 1000, 'dayHigh': 326.07, 'regularMarketPrice': 316.38, 'logo_url': 'https://logo.clearbit.com/microsoft.com'}