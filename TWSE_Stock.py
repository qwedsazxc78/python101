import requests
import time
import os

mydate = time.strftime("%Y/%m/%d")
year = str(int(mydate[0:4]) - 1911)
mydate2 = mydate.replace(mydate[0:4], year)

StartYear = '2018'
StartMonth = '02'
StartDay = '02'
StartDate = StartYear + StartMonth + StartDay
mydate2 = StartDate
setting = os.getcwd() + "\\" + "path.ini"

if os.path.exists(setting):
    with open(setting, 'r') as r:
        path = r.read()
    if not os.path.exists(path):
        os.makedirs(path)
else:
    path = ""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}

url1 = "http://www.twse.com.tw/ch/trading/fund/T86/T86.php"
payload1 = {"download": "csv",
            "qdate": mydate2,
            "select2": "ALLBUT0999",
            "sorting": "by_issue"}

res1 = requests.post(url1, headers=headers, data=payload1, stream=True)

fName1 = path + mydate.replace("/", "") + ".csv"

with open(fName1, 'wb') as f1:
    for chunk in res1.iter_content(1024):
        f1.write(chunk)

url3 = "http://www.tpex.org.tw/web/stock/3insti/daily_trade/\
3itrade_hedge_download.php?l=zh-tw&se=EW&t=D&d=" + mydate2 + "&s=0,asc,0"

res3 = requests.get(url3, headers=headers, stream=True)

fName3 = path + "BIGD_" + mydate2.replace("/", "") + ".csv"

with open(fName3, 'wb') as f3:
    for chunk in res3.iter_content(1024):
        f3.write(chunk)

url2 = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
payload2 = {"download": "csv",
            "qdate": mydate2,
            "selectType": "ALLBUT0999"}

res2 = requests.post(url2, headers=headers, data=payload2, stream=True)

fName2 = path + "A11" + mydate.replace("/", "") + ".csv"

with open(fName2, 'wb') as f2:
    for chunk in res2.iter_content(1024):
        f2.write(chunk)

url4 = "http://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/\
stk_wn1430_download.php?l=zh-tw&d=" + mydate2 + "&se=EW&s=0,asc,0"

res4 = requests.post(url4, headers=headers, data=payload2, stream=True)

fName4 = path + "SQUOTE_EW_" + mydate2.replace("/", "") + ".csv"

with open(fName4, 'wb') as f4:
    for chunk in res4.iter_content(1024):
        f4.write(chunk)