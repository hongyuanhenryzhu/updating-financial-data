#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import investpy
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt   


# # S&P 500 data

# In[2]:


#Using investpy to import the data from investing.com


# In[4]:


df = pd.DataFrame()
today = dt.datetime.today().strftime("%m/%d/%Y")
index = ['S&P 500 REAL ESTATE','S&P 500 TELECOM SERVICES','S&P 500 HEALTH CARE','S&P 500 FINANCIALS',
         'S&P 500 ENERGY','S&P 500 UTILITIES','S&P 500 INDUSTRIALS','S&P 500 CONSUMER STAPLES','S&P 500 INFORMATION TECHNOLOGY']
for x in index:
    df[x] = investpy.get_index_historical_data(index= x,
                                        country='United States',
                                        from_date='02/12/2019',
                                        to_date=today)['Close']


# In[5]:


df


# In[6]:


df.index=df.index + pd.DateOffset(1) #adjusting date
df


# In[13]:


df.to_excel("s&p500.xlsx")  #export excel file


# # ETF quotes

# In[2]:


#Using yfinance to import the data from yahoofinance


# In[7]:


# The below will pull back stock prices from the start date until end date specified.
start_sp = dt.datetime(2019, 12, 2)
end_sp = dt.datetime.today()
yf.pdr_override()


# In[8]:


xlsx=pd.ExcelFile('financial data.xlsx')
etf=pd.read_excel(xlsx,'QUOTES')
etf=etf.iloc[0].to_list()
del etf[0] 
etf #get the name list of etf


# In[9]:


df1 = pd.DataFrame()
for x in etf:
    df1[x] = pdr.get_data_yahoo(x, 
                               start_sp,
                                 end_sp)['Close']


# In[10]:


df1


# In[12]:


df1.to_excel("quotes.xlsx")  #export excel file

