import talib
import math
import numpy as np
import OverlapStudiesFunctions
import Getchartdata
##########################################################
############# Momentum Indicator Functions ###############
##########################################################

################## WMA - Weighted Moving Average ##############################
def getWMAarray9(closefloatarray):
    PastWMAArray = talib.WMA(closefloatarray, timeperiod=9)
    return PastWMAArray
################## IFTCCI   ##############################
def getIFTCCI(highfloatarray,lowfloatarray,closefloatarray):
    PastCCIArray = talib.CCI(highfloatarray,lowfloatarray,closefloatarray,timeperiod=5)
    value1=0.1*(PastCCIArray)
    value2=getWMAarray9(value1)
    IFTCCI1=np.exp(2*value2)-1
    IFTCCI2=np.exp(2*value2)+1
    IFTCCI=IFTCCI1/IFTCCI2
    lastIFTCCI=IFTCCI[-1]
    prevIFTCCI = IFTCCI[-2]
    prevprevIFTCCI = IFTCCI[-3]
    #return lastIFTCCI,prevIFTCCI,prevprevIFTCCI
    return lastIFTCCI
################## IFTRSI   ##############################
def getIFTRSI(closefloatarray):
    PastRSIArray = talib.RSI(closefloatarray,timeperiod=5)
    value1=0.1*(PastRSIArray-50)
    value2=getWMAarray9(value1)
    IFTRSI1=np.exp(2*value2)-1
    IFTRSI2=np.exp(2*value2)+1
    IFTRSI=IFTRSI1/IFTRSI2
    lastIFTCCI=IFTRSI[-1]
    prevIFTCCI = IFTRSI[-2]
    prevprevIFTCCI = IFTRSI[-3]
    #return lastIFTCCI,prevIFTCCI,prevprevIFTCCI
    return IFTRSI
################## RSI - Relative Strength Index   ##############################
def getRSI14(openfloatarray):
    PastRsıArray = talib.RSI(openfloatarray,timeperiod=14)
    lastRSIValue=PastRsıArray[-1]
    return lastRSIValue
################## RSIARRAY - Relative Strength Index   ##############################
def getRSIARRAY(closefloatarray):
    PastRsıArray1 = talib.RSI(closefloatarray,timeperiod=14)
    return PastRsıArray1

############## AROONOSC - Aroon Oscillator ###############################################
def getAROONOSC(highfloatarray,lowfloatarray):
    PastAROONOSCarray = talib.AROONOSC(highfloatarray, lowfloatarray, timeperiod=14)
    lastAROONOSCvalue=PastAROONOSCarray[-1]
    return lastAROONOSCvalue
############## WILLR - Williams' %R###############################################
def getWILLR(highfloatarray,lowfloatarray,closefloatarray):
    PastWILLRarray = talib.WILLR(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastWILLRvalue=PastWILLRarray[-1]
    return lastWILLRvalue
############## ULTOSC - Ultimate Oscillator ###############################################
def getULTOSC(highfloatarray,lowfloatarray,closefloatarray):
    PastULTOSCarray = talib.ULTOSC(highfloatarray, lowfloatarray, closefloatarray, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    lastULTOSCvalue=PastULTOSCarray[-1]
    return lastULTOSCvalue
############## TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA  ####################
def getTRIX(closefloatarray):
    PastTRIXarray = talib.TRIX(closefloatarray, timeperiod=30)
    lastTRIXvalue=PastTRIXarray[-1]
    return lastTRIXvalue


############## STOCHRSI - Stochastic Relative Strength Index  ###############################################
def getSTOCHRSI(PastRsıArray11):
    PastRsıArray11=PastRsıArray11[~np.isnan(PastRsıArray11)]
    stochrsif, stochrsis = talib.STOCH(PastRsıArray11, PastRsıArray11, PastRsıArray11, fastk_period=14, slowk_period=3, slowd_period=3)
    laststochrsifvalue=stochrsif[-1]
    lastlaststochrsifvalue=stochrsif[-2]
    laststochrsisvalue=stochrsis[-1]
    lastlaststochrsisvalue=stochrsis[-2]
    return laststochrsifvalue,lastlaststochrsifvalue,laststochrsisvalue,lastlaststochrsisvalue

################## STOCHF - Stochastic Fast  ##############################
def getSTOCHF(highfloatarray,lowfloatarray,closefloatarray):
    bfastk, bfastd = talib.STOCHF(highfloatarray, lowfloatarray, closefloatarray, fastk_period=3, fastd_period=3, fastd_matype=0)
    lastbfastkvalue=bfastk[-1]
    lastbfastdvalue=bfastd[-1]
    return lastbfastkvalue,lastbfastdvalue

################## STOCH - Stochastic   ##############################
def getSTOCH(highfloatarray,lowfloatarray,closefloatarray):
    slowk, slowd = talib.STOCH(highfloatarray, lowfloatarray, closefloatarray, fastk_period=3, slowk_period=3, slowk_matype=0, slowd_period=3,slowd_matype=0)
    lastslowkvalue=slowk[-1]
    lastslowdvalue=slowd[-1]
    return lastslowkvalue,lastslowdvalue


################## ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100  ##############################
def getROCR100(closefloatarray):
    PastROCR100array = talib.ROCR100(closefloatarray, timeperiod=10)
    lastROCR100value=PastROCR100array[-1]
    return lastROCR100value
################# ROCR - Rate of change ratio: (price/prevPrice)  ##############################
def getROCR(closefloatarray):
    PastROCRarray =talib.ROCR(closefloatarray, timeperiod=10)
    lastROCRvalue=PastROCRarray[-1]
    return lastROCRvalue
################## ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice  ##############################
def getROCP(closefloatarray):
    PastROCParray = talib.ROCP(closefloatarray, timeperiod=10)
    lastROCPvalue=PastROCParray[-1]
    return lastROCPvalue
################## ROC - Rate of change : ((price/prevPrice)-1)*100   ##############################
def getROC(closefloatarray):
    PastROCarray = talib.ROC(closefloatarray, timeperiod=10)
    lastROCvalue=PastROCarray[-1]
    return lastROCvalue

################## PPO - Percentage Price Oscillator  ##############################
def getPPO(closefloatarray):
    PastPPOarray = talib.PPO(closefloatarray, fastperiod=12, slowperiod=26, matype=0)
    lastPPOvalue = PastPPOarray[-1]
    return lastPPOvalue

################## PLUS_DM - Plus Directional Movement  ##############################
def getPLUS_DM(highfloatarray,lowfloatarray):
    PastPLUS_DMarray = talib.PLUS_DM(highfloatarray, lowfloatarray , timeperiod=14)
    lastPLUS_DMvalue = PastPLUS_DMarray[-1]
    return lastPLUS_DMvalue

################## PLUS_DI - Plus Directional Indicator  ##############################
def getPLUS_DI(highfloatarray, lowfloatarray, closefloatarray):
    PastPLUS_DIarray = talib.PLUS_DI(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastPLUS_DIvalue = PastPLUS_DIarray[-1]
    return lastPLUS_DIvalue

################## MOM - Momentum  ##############################
def getMOM(closefloatarray):
    PastMOMarray = talib.MOM(closefloatarray, timeperiod=10)
    lastMOMvalue = PastMOMarray[-1]
    return lastMOMvalue

################## MINUS_DM - Minus Directional Movement ##############################
def getMINUS_DM(highfloatarray, lowfloatarray):
    PastMINUS_DMarray = talib.MINUS_DM(highfloatarray, lowfloatarray, timeperiod=14)
    lastMINUS_DMvalue = PastMINUS_DMarray[-1]
    return lastMINUS_DMvalue

################## MINUS_DI - Minus Directional Indicator  ##############################
def getMINUS_DI(highfloatarray, lowfloatarray, closefloatarray):
    PastMINUS_DIarray = talib.MINUS_DI(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastMINUS_DIvalue = PastMINUS_DIarray[-1]
    return lastMINUS_DIvalue
"""
################## MFI - Money Flow Index  ##############################
def getMFI(highfloatarray, lowfloatarray, closefloatarray):
    PastMFIarray = MFI(highfloatarray, lowfloatarray, closefloatarray, volume, timeperiod=14)
    lastMFIvalue = PastMFIarray[-1]
    return lastMFIvalue

################## MACDFIX - Moving Average Convergence/Divergence Fix 12/26  ##############################
    macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)

################## MACDEXT - MACD with controllable MA type   ##############################
    macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0,signalperiod=9, signalmatype=0)
"""

################## MACD - Moving Average Convergence/Divergence  ##############################
def getMACD(closefloatarray):
    Pastmacdarray, Pastmacdsignalarray, Pastmacdhistarray = talib.MACD(closefloatarray, fastperiod=12, slowperiod=26, signalperiod=9)
    sonmacdhistvalue = Pastmacdhistarray[-1]
    oncekilastmacdhistvalue=Pastmacdhistarray[-2]
    oncekindenoncekilastmacdhistvalue = Pastmacdhistarray[-3]
    return sonmacdhistvalue,oncekilastmacdhistvalue,oncekindenoncekilastmacdhistvalue
################## MACDDEMA - Moving Average Convergence/Divergence  ##############################
def getMACDEMA(closefloatarray):
    MacddemaARRAY=getDEMAARRAY12(closefloatarray)-getDEMAARRAY26(closefloatarray)
    TriggerARRAY1=OverlapStudiesFunctions.getEMA9(MacddemaARRAY)
    TriggerARRAY2=OverlapStudiesFunctions.getEMA9(TriggerARRAY1)                  #2*mov(MACDEMA,9,e)-mov(mov(MACDEMA,9,e),9,e);
    Trigger=2*TriggerARRAY1-TriggerARRAY2
    HIST=MacddemaARRAY-Trigger
    sonhıst=HIST[-1]
    onecekihıst = HIST[-2]
    oncekindenoncekihıst = HIST[-3]
    return sonhıst,onecekihıst,oncekindenoncekihıst
################## DEMAARRAY12 - Double Exponential Moving Average  ##############################
def getDEMAARRAY12(closefloatarray):
    PastDEMAArray12 = talib.DEMA(closefloatarray, timeperiod=12)
    return PastDEMAArray12
################## DEMAARRAY26 - Double Exponential Moving Average  ##############################
def getDEMAARRAY26(closefloatarray):
    PastDEMAArray26 = talib.DEMA(closefloatarray, timeperiod=26)
    return PastDEMAArray26
################## DX - Directional Movement Index  ##############################
def getDX(highfloatarray, lowfloatarray, closefloatarray):
    PastDXarray = talib.DX(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastDXvalue = PastDXarray[-1]
    return lastDXvalue

################## CMO - Chande Momentum Oscillator  ##############################
def getCMO(closefloatarray):
    PastCMOarray = talib.CMO(closefloatarray, timeperiod=14)
    lastCMOvalue = PastCMOarray[-1]
    return lastCMOvalue
    ################## CCI - Commodity Channel Index  ##############################
def getCCI(highfloatarray, lowfloatarray, closefloatarray):
    PastCCIarray = talib.CCI(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastCCIvalue = PastCCIarray[-1]
    return lastCCIvalue
################## BOP - Balance Of Power  ##############################
def getBOP(openfloatarray,highfloatarray, lowfloatarray, closefloatarray):
    PastBOParray = talib.BOP(openfloatarray,highfloatarray, lowfloatarray, closefloatarray)
    lastBOPvalue = PastBOParray[-1]
    return lastBOPvalue
"""
    ################## AROON - Aroon  ##############################
    aroondown, aroonup = AROON(high, low, timeperiod=14)
"""
################## APO - Absolute Price Oscillator  ##############################
def getAPO(closefloatarray):
    PastAPOarray = talib.APO(closefloatarray, fastperiod=12, slowperiod=26, matype=0)
    lastAPOvalue = PastAPOarray[-1]
    return lastAPOvalue

################## ADXR - Average Directional Movement Index Rating  ##############################
def getADXR(highfloatarray, lowfloatarray, closefloatarray):
    PastADXRarray = talib.ADXR(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastADXRvalue = PastADXRarray[-1]
    return lastADXRvalue

################## ADX - Average Directional Movement Index  ##############################
def getADX(highfloatarray, lowfloatarray, closefloatarray):
    PastADXarray = talib.ADX(highfloatarray, lowfloatarray, closefloatarray, timeperiod=14)
    lastADXvalue = PastADXarray[-1]
    return lastADXvalue