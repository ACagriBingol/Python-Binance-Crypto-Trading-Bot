import talib
import pandas_ta
import pandas as pd
##########################################################
############# OverlapStudiesFunctions ###############
##########################################################

################## BBANDS - Bollinger Bands  ##############################
def getBBANDS(closefloatarray):
    Pastupperbandarray, Pastmiddlebandarray, Pastlowerbandarray = talib.BBANDS(closefloatarray, timeperiod=21, nbdevup=2, nbdevdn=2, matype=0)
    lastupperbandValue=Pastupperbandarray[-1]
    lastmiddleValue=Pastmiddlebandarray[-1]
    lastlowerbandValue=Pastlowerbandarray[-1]
    return lastupperbandValue,lastmiddleValue,lastlowerbandValue

################## DEMA - Double Exponential Moving Average  ##############################
def getDEMA(closefloatarray):
    PastDEMAArray = talib.DEMA(closefloatarray, timeperiod=26)
    lastDEMAValue=PastDEMAArray[-1]
    return lastDEMAValue
################## EMA - Exponential Moving Average  ##############################
def getEMA(closefloatarray):
    PastEMAArray = talib.EMA(closefloatarray, timeperiod=30)
    lastEMAValue=PastEMAArray[-1]
    return lastEMAValue
################## EMA - Exponential Moving Average  ##############################
def getEMA2(closefloatarray):
    PastEMAArray = talib.EMA(closefloatarray, timeperiod=2)
    #lastEMAValue = PastEMAArray[-1]
    return PastEMAArray
################## EMA - Exponential Moving Average  ##############################
def getEMA9(closefloatarray):
    PastEMAArray = talib.EMA(closefloatarray, timeperiod=9)
    #lastEMAValue = PastEMAArray[-1]
    return PastEMAArray
################## HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline  ##############################
def getHT_TRENDLINE(closefloatarray):
    PastHT_TRENDLINEArray = talib.HT_TRENDLINE(closefloatarray)
    lastHT_TRENDLINEValue=PastHT_TRENDLINEArray[-1]
    return lastHT_TRENDLINEValue
    ################## KAMA - Kaufman Adaptive Moving Average  ##############################
def getKAMA(closefloatarray):
    PastKAMAArray = talib.KAMA(closefloatarray, timeperiod=30)
    lastKAMAValue=PastKAMAArray[-1]
    return lastKAMAValue
################## MA - Moving average  ##############################
def getMA(closefloatarray):
    PastMAArray = talib.MA(closefloatarray, timeperiod=30, matype=0)
    lastMAValue=PastMAArray[-1]
    return lastMAValue
################## MA - Moving average  ##############################
def getMA9(closefloatarray):
    PastMAArray = talib.MA(closefloatarray, timeperiod=9, matype=0)
    lastMAValue=PastMAArray[-1]
    return lastMAValue
"""
################## MAMA - MESA Adaptive Moving Average  ##############################
    mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
    lastKAMAValue=PastKAMAArray[-1]
    return lastKAMAValue

################## MAVP - Moving average with variable period  ##############################
def getMAVP(closefloatarray):
    PastMAVPArray = talib.MAVP(closefloatarray, periods, minperiod=2, maxperiod=30, matype=0)
    lastMAVPValue = PastMAVPArray[-1]
    return lastMAVPValue
"""
################## MIDPOINT - MidPoint over period  ##############################
def getMIDPOINT(closefloatarray):
    PastMIDPOINTArray = talib.MIDPOINT(closefloatarray, timeperiod=14)
    lastMIDPOINTValue = PastMIDPOINTArray[-1]
    return lastMIDPOINTValue

################## MIDPRICE - Midpoint Price over period  ##############################
def getMIDPRICE(highfloatarray,lowfloatarray):
    PastMIDPRICEArray = talib.MIDPRICE(highfloatarray, lowfloatarray, timeperiod=14)
    lastMIDPRICEValue = PastMIDPRICEArray[-1]
    return lastMIDPRICEValue

################## SAR - Parabolic SAR ##############################
def getSAR(highfloatarray, lowfloatarray):
    PastSARArray = talib.SAR(highfloatarray, lowfloatarray, acceleration=0.02, maximum=0.2)
    lastSARValue = PastSARArray[-1]
    prevlastSARValue = PastSARArray[-2]
    return lastSARValue,prevlastSARValue
################## SAR - Parabolic SAR ##############################
def getSARA(highfloatarray, lowfloatarray):
    PastSARArray = talib.SAR(highfloatarray, lowfloatarray, acceleration=0.02, maximum=0.2)
    return PastSARArray
################# SAREXT - Parabolic SAR - Extended  ##############################
def getSAREXT(highfloatarray, lowfloatarray):
    PastSAREXTArray = talib.SAREXT(highfloatarray, lowfloatarray, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0,accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    lastSAREXTvalue = PastSAREXTArray[-1]
    return lastSAREXTvalue

################## SMA - Simple Moving Average  ##############################
def getSMA50(closefloatarray):
    PastSMAArray = talib.SMA(closefloatarray, timeperiod=50)
    lastSMAvalue = PastSMAArray[-1]
    return lastSMAvalue

################## SMA - Simple Moving Average  ##############################
def getSMA200(closefloatarray):
    PastSMAArray = talib.SMA(closefloatarray, timeperiod=200)
    lastSMAvalue = PastSMAArray[-1]
    return lastSMAvalue

################## T3 - Triple Exponential Moving Average (T3)  ##############################
def getT3(close_array,high_array, low_array,t3Length,volume_factor):
    ema_first_input = (high_array + low_array + 2 * close_array) / 4

    e1 = talib.EMA(ema_first_input, t3Length)

    e2 = talib.EMA(e1, t3Length)

    e3 = talib.EMA(e2, t3Length)

    e4 = talib.EMA(e3, t3Length)

    e5 = talib.EMA(e4, t3Length)

    e6 = talib.EMA(e5, t3Length)

    c1 = -1 * volume_factor * volume_factor * volume_factor

    c2 = 3 * volume_factor * volume_factor + 3 * volume_factor * volume_factor * volume_factor

    c3 = -6 * volume_factor * volume_factor - 3 * volume_factor - 3 * volume_factor * volume_factor * volume_factor

    c4 = 1 + 3 * volume_factor + volume_factor * volume_factor * volume_factor + 3 * volume_factor * volume_factor

    T3 = c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3

    lastT3value = T3[-1]
    prevT3value = T3[-2]
    prevprevT3value = T3[-3]
    prevprevprevT3value = T3[-4]
    return lastT3value,prevT3value,prevprevT3value,prevprevprevT3value

################## TEMA30 - Triple Exponential Moving Average ##############################
def getTEMA8(closefloatarray):
    PastTEMA30Array = talib.TEMA(closefloatarray, timeperiod=8)
    lastTEMA30value = PastTEMA30Array[-1]
    return lastTEMA30value
################## TEMA60 - Triple Exponential Moving Average ##############################
def getTEMA21(closefloatarray):
    PastTEMA60Array = talib.TEMA(closefloatarray, timeperiod=21)
    lastTEMA60value = PastTEMA60Array[-1]
    return lastTEMA60value

################## TRIMA - Triangular Moving Average  ##############################
def getTRIMA(closefloatarray):
    PastTRIMAArray = talib.TRIMA(closefloatarray, timeperiod=30)
    lastTRIMAvalue = PastTRIMAArray[-1]
    return lastTRIMAvalue
################## WMA - Weighted Moving Average ##############################
def getWMA(closefloatarray):
    PastWMAArray = talib.WMA(closefloatarray, timeperiod=30)
    lastWMAvalue = PastWMAArray[-1]
    return lastWMAvalue
################## SUPERTREND 12-3 ##############################
def getSUPERTREND_12_3(highfloatarray, lowfloatarray,closefloatarray):
    data = {
        "high": highfloatarray,
        "low": lowfloatarray,
        "close":closefloatarray,
    }
    df = pd.DataFrame(data)
    supertrendarray = pandas_ta.supertrend(high=df['high'], low=df['low'], close=df['close'], period=12, multiplier=3)
    supertrend=supertrendarray.iloc[-1][0]
    prevsupertrend=supertrendarray.iloc[-2][0]
    return supertrend,prevsupertrend

################## SUPERTREND 11-2 ##############################
def getSUPERTREND_11_2(highfloatarray, lowfloatarray,closefloatarray):
    data = {
        "high": highfloatarray,
        "low": lowfloatarray,
        "close":closefloatarray,
    }
    df = pd.DataFrame(data)
    supertrendarray = pandas_ta.supertrend(high=df['high'], low=df['low'], close=df['close'], period=11, multiplier=2)
    supertrend=supertrendarray.iloc[-1][0]
    prevsupertrend=supertrendarray.iloc[-2][0]
    return supertrend,prevsupertrend

################## SUPERTREND 10-1 ##############################
def getSUPERTREND_10_1(highfloatarray, lowfloatarray,closefloatarray):
    data = {
        "high": highfloatarray,
        "low": lowfloatarray,
        "close":closefloatarray,
    }
    df = pd.DataFrame(data)
    supertrendarray = pandas_ta.supertrend(high=df['high'], low=df['low'], close=df['close'], period=10, multiplier=1)
    supertrend=supertrendarray.iloc[-1][0]
    prevsupertrend=supertrendarray.iloc[-2][0]
    return supertrend,prevsupertrend

