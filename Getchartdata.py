from datetime import datetime
################## close verilerini çekme ######################
def getclosearray(arr):
    close=arr[:,4]
    closefloatarray = close.astype(float)
    return closefloatarray

############### HIGH VERİLERİNİ ÇEKME #########################
def gethigharray(arr):
    high = arr[:, 2]
    highfloatarray = high.astype(float)
    return highfloatarray

################ LOW VERİLERİNİ ÇEKMEK ################################
def getlowarray(arr):
    low = arr[:, 3]
    lowfloatarray = low.astype(float)
    return lowfloatarray

################# OPEN VERİLEİNİ ÇEKMEK ##############################
def getopenarray(arr):
    open = arr[:, 1]
    openfloatarray = open.astype(float)
    return openfloatarray

################# VOLUME VERİLERİNİ ÇEKMEK #############################
def getvolumearray(arr):
    volume = arr[:, 5]
    volumefloatarray = volume.astype(float)
    return volumefloatarray

################## SON close verilerini çekme ######################
def getclose(arr):
    closearray=arr[:,4]
    close=closearray[-1]
    prevclose = closearray[-2]
    close = close.astype(float)
    prevclose = prevclose.astype(float)
    return close,prevclose

############### SON HIGH VERİLERİNİ ÇEKME #########################
def gethigh(arr):
    high=arr[:,2]
    high=high[-1]
    high = high.astype(float)
    return high


################ SON LOW VERİLERİNİ ÇEKMEK ################################
def getlow(arr):
    low=arr[:,3]
    low=low[-1]
    low = low.astype(float)
    return low

################# SON OPEN VERİLEİNİ ÇEKMEK ##############################
def getopen(arr):
    open=arr[:,1]
    open=open[-1]
    open = open.astype(float)
    return open

################# SON VOLUME VERİLERİNİ ÇEKMEK #############################
def getvolume(arr):
    volume=arr[:,5]
    volume=volume[-1]
    volume = volume.astype(float)
    return volume
################# TİİME VERİSİNİ ÇEKMEK #############################
def gettime(arr):
    timearr = arr[:, 0]
    timearr = timearr.astype(float)
    timearr=timearr[-1]
    time = datetime.fromtimestamp(timearr / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    return time
