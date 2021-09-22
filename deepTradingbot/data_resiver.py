import MetaTrader5 as mt5




def getdata():

    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    else:
        print("initialize() succes, error code =", mt5.last_error())
    # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
    # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
    rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 9999)
    return rates