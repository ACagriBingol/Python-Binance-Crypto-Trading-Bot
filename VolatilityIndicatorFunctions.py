import talib
##########################################################
############# Volatility Indicator Functions ###############
##########################################################

################## ATR - Average True Range  ##############################
def getATR(highfloatarray,lowfloatarray,closefloatarray):
    PastATRArray = talib.ATR(highfloatarray,lowfloatarray,closefloatarray, timeperiod=14)
    lastATRValue = PastATRArray[-1]
    return lastATRValue

################## NATR - Normalized Average True Range  ##############################
def getNATR(highfloatarray,lowfloatarray,closefloatarray):
    PastNATRArray = talib.NATR(highfloatarray,lowfloatarray,closefloatarray, timeperiod=14)
    lastNATRValue = PastNATRArray[-1]
    return lastNATRValue


################## TRANGE - True Range  ##############################
def getNATR(highfloatarray,lowfloatarray,closefloatarray):
    PastTRANGEArray = talib.TRANGE(highfloatarray, lowfloatarray, closefloatarray)
    lastTRANGEValue = PastTRANGEArray[-1]
    return lastTRANGEValue