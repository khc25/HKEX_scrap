import datetime
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from seleniumrequests import Firefox
import re
import pandas as pd
from sqlQuery import cur

url = "https://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh"

start_date = datetime.date(2020, 3, 30)

end_date = datetime.date(2021, 3, 29)

delta = datetime.timedelta(days=1)

while start_date <= end_date:
    #driver = webdriver.Firefox()
    # driver = Firefox()
    res=requests.get(url)
    data = res.text

    
    bs = BeautifulSoup(data, "lxml")
    __EVENTVALIDATION = bs.find("input", {"id": "__EVENTVALIDATION"}).attrs['value']
    __VIEWSTATEGENERATOR = bs.find("input", {"id": "__VIEWSTATEGENERATOR"}).attrs['value']
    __VIEWSTATE = bs.find("input", {"id": "__VIEWSTATE"}).attrs['value']
    today = bs.find("input", {"id": "today"}).attrs['value']
    day = start_date.day
    month = start_date.month
    year = start_date.year
    date = start_date.strftime("%Y/%m/%d")
    print(date)
    data = {
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "today":today,
        "sortBy" : "",
        "alertMsg" : "",
        # "ddlShareholdingDay":day,
        # "ddlShareholdingMonth":month,
        # "ddlShareholdingYear":year,
        "txtShareholdingDate":date,
        "btnSearch": "搜尋" 
        }
    req = requests.post(url, data)
    soup = BeautifulSoup(req.content, 'html.parser')


    
    all_tables=[[divs.getText() for divs in tr.find_all('div', {"class","mobile-list-body"})] for tr in soup.find_all('tr')]
    # stock_info=[[sub_item.replace('\r\n', '') for sub_item in item] for item in all_tables]
    for table in all_tables:
        if not table: 
            pass
        else:
            print(table)
            code = table[0]
            name = table[1]
            share = table[2]
            percent = table[3]
            cur.execute('INSERT INTO shc (date, stock_code, stock_name, shareholding_CCASS, shares_percentage) VALUES (%s, %s, %s, %s, %s)', (date,code,name,share, percent))

        
    # print(all_tables)
    start_date += delta
    

