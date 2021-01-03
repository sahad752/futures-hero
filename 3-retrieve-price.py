import os
import time
from binance.client import Client

# start = time.time()
# print(f"{time.time() - start} seconds\n")

symbol  =  "BTCUSDT"
bet     =  10

# Get environment variables
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')
client      = Client(api_key, api_secret)

while True:
    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, "1 minute ago UTC")
    print(klines)
    time.sleep(5)