import talib
##########################################################
############# Price Transform ###############
##########################################################


 ################## AVGPRICE - Average Price ##############################
def getAVGPRICE(openfloatarray,highfloatarray,lowfloatarray,closefloatarray):
    PastAVGPRICEArray = talib.AVGPRICE(openfloatarray, highfloatarray, lowfloatarray, closefloatarray)
    lastAVGPRICEValue = PastAVGPRICEArray[-1]
    return lastAVGPRICEValue

################## MEDPRICE - Median Price  ##############################
def getMEDPRICE(highfloatarray, lowfloatarray):
    PastMEDPRICEArray = talib.MEDPRICE(highfloatarray, lowfloatarray)
    lastMEDPRICEValue = PastMEDPRICEArray[-1]
    return lastMEDPRICEValue

################## TYPPRICE - Typical Price  ##############################
def getTYPPRICE(highfloatarray,lowfloatarray,closefloatarray):
    PastTYPPRICEArray = talib.TYPPRICE(highfloatarray,lowfloatarray,closefloatarray)
    lastTYPPRICEValue = PastTYPPRICEArray[-1]
    return lastTYPPRICEValue


################## WCLPRICE - Weighted Close Price  ##############################
def getWCLPRICE(highfloatarray, lowfloatarray, closefloatarray):
    PastWCLPRICEArray = talib.WCLPRICE(highfloatarray, lowfloatarray, closefloatarray)
    lastWCLPRICEValue = PastWCLPRICEArray[-1]
    return lastWCLPRICEValue