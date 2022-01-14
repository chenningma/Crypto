#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:55:01 2022

@author: gracema
"""

import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '6e77b1fe-24f6-458b-975e-559576406596',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  


### Structure Data  
px_df = pd.json_normalize(data['data'])
px_tbl_fnl = px_df.loc[: , ['name', 'symbol', 'last_updated', 'quote.USD.price']]  



#### Specific URL for coin prices

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=6e77b1fe-24f6-458b-975e-559576406596&limit=10'

