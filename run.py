try:
    import os
    import time
    import requests
    import socket
    import urllib3
    import config
    import dead_or_alive
    import binance_futures
    from datetime import datetime
    from termcolor import colored
    from binance.exceptions import BinanceAPIException

    if binance_futures.position_information()[0].get('marginType') != "isolated": binance_futures.change_margin_to_ISOLATED()
    if int(binance_futures.position_information()[0].get("leverage")) != config.leverage:
        binance_futures.change_leverage(config.leverage)
        print(colored("CHANGED LEVERAGE :   " + binance_futures.position_information()[0].get("leverage") + "x\n", "red"))

    use_SL = input("Use Stoploss? [Y/n] ") or 'n'
        
    if use_SL == 'Y': 
        print(colored("Stoploss Enabled", "green"))
        use_stoploss = True
        percentage = input("Percentage % that you are willing to lose? (Default 70): ") or '70'
        print(colored("Stoploss         :   " + percentage + "%\n"))
    else: 
        print(colored("Stoploss Disabled\n", "red"))
        use_stoploss = False
        percentage = 0

    while True:
        try:
            dead_or_alive.dead_or_alive(use_stoploss, int(percentage))
            time.sleep(8)

        except (BinanceAPIException,
                ConnectionResetError,
                socket.timeout,
                urllib3.exceptions.ProtocolError,
                urllib3.exceptions.ReadTimeoutError,
                requests.exceptions.ConnectionError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout) as e:

            if not os.path.exists("Error_Message"): os.makedirs("Error_Message")
            with open((os.path.join("Error_Message", config.pair + ".txt")), "a") as error_message:
                error_message.write("[!] " + config.pair + " - " + "Created at : " + datetime.today().strftime("%d-%m-%Y @ %H:%M:%S") + "\n")
                error_message.write(str(e) + "\n\n")

except KeyboardInterrupt: print("\n\nAborted.\n")
