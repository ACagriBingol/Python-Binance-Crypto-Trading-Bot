import talib
    ##########################################################
    ############# Cycle Indicator Functions ###############
    ##########################################################

################## HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period  ##############################
def getHT_DCPERIOD(closefloatarray):
    PastHT_DCPERIODArray = talib.HT_DCPERIOD(closefloatarray)
    lastHT_DCPERIODValue = PastHT_DCPERIODArray[-1]
    return lastHT_DCPERIODValue
################## HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase  ##############################
def getHT_DCPHASE(closefloatarray):
    PastHT_DCPHASEArray = talib.HT_DCPHASE(closefloatarray)
    lastHT_DCPHASEValue = PastHT_DCPHASEArray[-1]
    return lastHT_DCPHASEValue
"""
    ################## HT_PHASOR - Hilbert Transform - Phasor Components  ##############################
    inphase, quadrature = HT_PHASOR(close)

    ################## HT_SINE - Hilbert Transform - SineWave  ##############################
    sine, leadsine = HT_SINE(close)
"""
################## HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode  ##############################
def getHT_TRENDMODE(closefloatarray):
    PastHT_TRENDMODEArray = talib.HT_TRENDMODE(closefloatarray)
    lastHT_TRENDMODEValue = PastHT_TRENDMODEArray[-1]
    return lastHT_TRENDMODEValue