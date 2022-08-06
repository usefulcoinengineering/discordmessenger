#!/usr/bin/env python3

import json
import requests

from libraries.discordmessenger import appalert as appalert

response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDC')
jsondata = response.json()

messages = json.dumps( jsondata, sort_keys=True, indent=4, separators=(',', ': ') )
appalert ( messages )
