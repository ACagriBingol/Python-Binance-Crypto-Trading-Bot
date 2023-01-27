from _datetime import datetime
import numpy as np
import pandas as pd
from binance.client import Client
import Getchartdata
import MomentumIndicatorFunctions
import OverlapStudiesFunctions
import requests
#import datetime
import time
import math 


token1 = "---" #telegram all logs token
token2 = "---" #telegram trades token
chat_id = 0 #telegram id
dp=[5,4,1,0,0,2,2,2]
alınandp=[]
trdPair1 = ['BTC','ETH','ADA','XRP','DOGE','DOT','UNI','LINK']
trdPair=['BTCUSDT','ETHUSDT','ADAUSDT','XRPUSDT','DOGEUSDT','DOTUSDT','UNIUSDT','LINKUSDT']
#trdPair = ['BTCUSDT','ETHUSDT','ADAUSDT','XRPUSDT','SOLUSDT','DOGEUSDT','DOTUSDT','UNIUSDT','LINKUSDT','BCHUSDT','LTCUSDT','LUNAUSDT','ICPUSDT','MATICUSDT','FILUSDT','AVAXUSDT','XLMUSDT','VETUSDT','ETCUSDT','THETAUSDT','FTTUSDT','TRXUSDT','XMRUSDT','ATOMUSDT','EOSUSDT','CAKEUSDT','AAVEUSDT','XECUSDT','ALGOUSDT','IOTAUSDT']
#trdPair1 = ['BTCUSDT','ETHUSDT','ADAUSDT','XRPUSDT','SOLUSDT','DOGEUSDT','DOTUSDT','UNIUSDT','LINKUSDT','BCHUSDT','LTCUSDT','LUNAUSDT','ICPUSDT','MATICUSDT','FILUSDT','AVAXUSDT','XLMUSDT','VETUSDT','ETCUSDT','THETAUSDT','FTTUSDT','TRXUSDT','XMRUSDT','ATOMUSDT','EOSUSDT','CAKEUSDT','AAVEUSDT','XECUSDT','ALGOUSDT','MIOTAUSDT','AXSRUSDT','GRTUSDT','QNTUSDT','FTMUSDT','XTZUSDT','BTCBUSDT','NEOUSDT','KLAYUSDT','NEARUSDT','MKRUSDT','LEOUSDT','BSVUSDT','EGLDUSDT','KSMUSDT','WAVESUSDT','HBARUSDT','BTTUSDT','SHIBUSDT','KICKUSDT','HTUSDT','COMPUSDT','AMPUSDT','DASHUSDT','REVUSDT','CHZUSDT','RUNEDUSDT','DCRUSDT','HNTUSDT','TFUELUSDT','HOTUSDT','ZECUSDT','XEMUSDT','STXUSDT','ARUSDT','MANAUSDT','ENJUSDT','CELUSDT','SUSHIUSDT','ONEUSDT','YFIUSDT','CELOUSDT','FLOWUSDT','QTUMUSDT','SNXUSDT','BTGUSDT','ZILUSDT','BATUSDT','PERPUSDT','OKBUSDT','RVNUSDT','TELUSDT','OMGUSDT','KCSUSDT','IOSTUSDT','NEXOUSDT','BNTUSDT','SCUSDT','ZENUSDT','PAXUSDT','ICXUSDT','DGBUSDT','NXMUSDT','CRVUSDT','ONTUSDT','ZRXUSDT','AUDIOUSDT','RAYUSDT','NANOUSDT','FETUSDT','CHSBUSDT','ANKRUSDT','MINAUSDT','UMAUSDT','VGXUSDT','RENUSDT', 'SANDUSDT', 'OMIUSDT', 'C98USDT', 'IOTXUSDT', 'LRCUSDT', '1INCHUSDT', 'GLMUSDT', 'RSRUSDT', 'SXPUSDT', 'DENTUSDT', 'WAXPUSDT', 'LSKUSDT', 'OCEANUSDT', 'ERGUSDT', 'STORJUSDT', 'ALPHAUSDT', 'UBTUSDT', 'BCDUSDT', 'NMRUSDT', 'INJUSDT', 'SANDUSDT', 'MEDUSDT', 'PUNDIXUSDT', 'ELFUSDT', 'SKLUSDT', 'LPTUSDT', 'VTHOUSDT', 'CKBUSDT', 'BAKEUSDT', 'WINUSDT', 'AGIXUSDT', 'WRXUSDT', 'TWTUSDT', 'YGGUSDT', 'ROSEUSDT', 'MNGOUSDT', 'GTUSDT', 'XVSUSDT', 'OGNUSDT', 'TITANUSDT', 'XPRTUSDT', 'XCHUSDT', 'SNTUSDT', 'EWTUSDT', 'STMXUSDT', 'VLXUSDT', 'CVCUSDT', 'ARDRUSDT', 'BESTUSDT', 'DAGUSDT', 'RLCUSDT', 'IDEXUSDT', 'STRAXUSDT', 'PAXGUSDT', 'KNCUSDT']
SatısCoinleri=[]
Coinlerim = []
CoinleriAldıgımFiyat=[]
AldığımCoinlerinSayısı=[]
YüzdeKar=[]
kumulatifYk=0
KacinciTrade=0
aldıgımzaman=['A','B','C','D','E']

while True:

    i = 0
    j = 0
    print("Al SAT DÖNGÜSÜ BAŞLADI " + str(datetime.now()))
    try:
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1), data={'chat_id': chat_id,'text': "Al SAT DÖNGÜSÜ BAŞLADI " + str(datetime.now())}).json()
    except:
        print("telegram baglantı hatası")

    #time.sleep(10)

#### AL DÖNGÜSÜ####
    while i < len(trdPair):

        try:
            client = Client('--','--')
            candles = client.get_klines(symbol=trdPair[i], interval=Client.KLINE_INTERVAL_4HOUR)
        except:
            print("Binance Bağlantı Hatası")

            try:
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': "Binance Bağlantı Hatası"}).json()
            except:
                print("telegram baglantı hatası")

        try:
            arr=np.array(candles)

            (close,prevclose)=Getchartdata.getclose(arr)
            close=float(close)
            prevclose=float(prevclose)

            #RSI14=MomentumIndicatorFunctions.getRSI14(GrafikDatalarınıCekmek.getopenarray(arr))
            (PSAR,PREVPSAR)=OverlapStudiesFunctions.getSAR(Getchartdata.gethigharray(arr), Getchartdata.getlowarray(arr))
            #(MACDHIST, PREVMACDHIST) = MomentumIndicatorFunctions.getMACD(GrafikDatalarınıCekmek.getclosearray(arr))
            #(sonhıst, onecekihıst, oncekindenoncekihıst) = MomentumIndicatorFunctions.getMACDEMA(GrafikDatalarınıCekmek.getclosearray(arr))
            #(STOCHRSIFAST, PREVSTOCHRSIFAST, STOCHRSISLOW,PREVSTOCHRSISLOW) = MomentumIndicatorFunctions.getSTOCHRSI( MomentumIndicatorFunctions.getRSIARRAY(GrafikDatalarınıCekmek.getclosearray(arr)))
            #(SUPERTREND_12_3,LASTSUPERTREND_12_3)=OverlapStudiesFunctions.getSUPERTREND_12_3(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #(SUPERTREND_11_2,LASTSUPERTREND_11_2)=OverlapStudiesFunctions.getSUPERTREND_11_2(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #(SUPERTREND_10_1,LASTSUPERTREND_10_1)=OverlapStudiesFunctions.getSUPERTREND_10_1(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))

            #ALLSUPERTRENDLİNEGREEN = SUPERTREND_12_3<close and SUPERTREND_11_2<close and SUPERTREND_10_1<close
            #SUPERTRENDLİNEGREEN = SUPERTREND_10_1<close
            #SUPERTRENDCROSSDOWN=SUPERTREND_12_3<close and LASTSUPERTREND_12_3>prevclose
            #STOCHRSICROSSUP=STOCHRSIFAST>STOCHRSISLOW and PREVSTOCHRSIFAST < PREVSTOCHRSISLOW
            #MACDCROSSUP = MACDHIST > 0 and PREVMACDHIST < 0
            PSARCROSSDOWN = PSAR < close and PREVPSAR > prevclose

            #ADX = MomentumIndicatorFunctions.getADX(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #pDI = MomentumIndicatorFunctions.getPLUS_DI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #nDI = MomentumIndicatorFunctions.getMINUS_DI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #(LASTT3, PREVT3, PREVPREVT3, PREVPREVPREVT3) = OverlapStudiesFunctions.getT3(GrafikDatalarınıCekmek.getclosearray(arr), GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr), 3, 0.618)
            #IFTCCI = MomentumIndicatorFunctions.getIFTCCI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
            #TEMA8 = OverlapStudiesFunctions.getTEMA8(GrafikDatalarınıCekmek.getclosearray(arr))
            #TEMA21 = OverlapStudiesFunctions.getTEMA21(GrafikDatalarınıCekmek.getclosearray(arr))


            #T3TOGREEN = (LASTT3>PREVPREVT3 and PREVPREVT3>PREVT3 and PREVT3>PREVPREVPREVT3) or (LASTT3>PREVT3 and PREVT3>PREVPREVPREVT3 and PREVPREVPREVT3 and PREVPREVT3) or (LASTT3>PREVPREVT3 and PREVPREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVT3) or (PREVPREVT3>LASTT3 and LASTT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVT3) or (LASTT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVT3 and PREVT3>PREVPREVT3) or (LASTT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVPREVT3 and PREVPREVT3>PREVT3) or (PREVPREVPREVT3>LASTT3 and LASTT3>PREVT3 and PREVT3>PREVPREVT3) or (PREVPREVPREVT3>LASTT3 and LASTT3>PREVPREVT3 and PREVPREVT3>PREVT3)
            #MACDDEMAAL = (sonhıst>0 and onecekihıst<0) or (sonhıst>0 and onecekihıst>0 and oncekindenoncekihıst>0)

        except:
            print("Ta-lib Hesaplama Hatası")
            try:
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': "Ta-lib Hesaplama Hatası"}).json()
            except:
                print("telegram baglantı hatası")

        if  (PSARCROSSDOWN):
            print(" AL !!!! " + trdPair[i] + " TARİH--- " +str(datetime.now()) + " -----CLOSE--- " + str(close))
            try:
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': " AL AL AL AL AL AL !!!!!!!!!!!!!!!! " + trdPair[i] + " TARİH--- " +str(datetime.now()) + " -----CLOSE--- " + str(close)}).json()
            except:
                print("telegram baglantı hatası")

            try:
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': " AL AL AL AL AL AL !!!!!!!!!!!!!!!! " + trdPair[i] + " TARİH--- " +str(datetime.now()) + " -----CLOSE--- " + str(close)}).json()
            except:
                print("telegram baglantı hatası")

            #balanceusdt = client.get_asset_balance(asset='USDT')
            #balanceusdt = float(balanceusdt['free'])

            try:
                try:
                    client = Client('---','---')
                    order1 = client.order_market_buy(symbol=trdPair[i],quantity=float(round((15.0/close),dp[i])))
                except:
                    client = Client('---','---')
                    order1 = client.order_market_buy(symbol=trdPair[i],quantity=float(round((15.0/close),dp[i])))
                alınandp.append(dp[i])
                Coinlerim.append(trdPair[i])
                SatısCoinleri.append(trdPair1[i])
                aldıgımzaman.append(str(datetime.now()))
                AldığımCoinlerinSayısı.append(float((order1['executedQty'])))
                orderrr1 = pd.DataFrame(order1)
                a=orderrr1.iloc[0][13]
                b = pd.DataFrame(a, index=[0])
                c1 = float(b['price'])
                CoinleriAldıgımFiyat.append(c1)
                print(trdPair[i] + " ALINDI--- " +  " TARİH--- " + str(datetime.now()) + " ALDIGIM FİYAT--- " + str(c1) + "ALDIGIM MİKTAR--- " + str((order1['executedQty'])))
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': trdPair[i] + " ALINDI--- " +  " TARİH--- " + str(datetime.now()) + " ALDIGIM FİYAT--- " + str(c1) + "ALDIGIM MİKTAR--- " + str((order1['executedQty']))}).json()
                except:
                    print("telegram baglantı hatası")

                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': trdPair[i] + " ALINDI--- " +  " TARİH--- " + str(datetime.now()) + " ALDIGIM FİYAT--- " + str(c1) + "ALDIGIM MİKTAR--- " + str((order1['executedQty']))}).json()
                except:
                    print("telegram baglantı hatası")

                trdPair.pop(i)
                dp.pop(i)
                trdPair1.pop(i)

                #now=datetime.datetime.now()
                #x=(now.minute)%60
                #y=60-x
                #time.sleep(y)

                #print(Coinlerim)
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': Coinlerim}).json()
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id,'text': Coinlerim}).json()
                #print(CoinleriAldıgımFiyat)
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': CoinleriAldıgımFiyat}).json()
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id,'text': CoinleriAldıgımFiyat}).json()
                #print(AldığımCoinlerinSayısı)
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': AldığımCoinlerinSayısı}).json()
                #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id,'text': AldığımCoinlerinSayısı}).json()

            except Exception as exp:
                print(exp.status_code)
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': exp.status_code}).json()
                except:
                    print("telegram baglantı hatası")

                print(exp.message)
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': exp.message}).json()
                except:
                    print("telegram baglantı hatası")



            i=i+1
        else:
            print(trdPair[i]+" Alım Şartları sağlamıyor")
            try:
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': trdPair[i]+" Alım Şartları sağlamıyor"}).json()
            except:
                print("telegram baglantı hatası")

            i=i+1
#### SAT DÖNGÜSÜ#####
    if len(Coinlerim)>0:
        while j < len(Coinlerim):
            try:
                client = Client('--','--')
                candles = client.get_klines(symbol=Coinlerim[j], interval=Client.KLINE_INTERVAL_4HOUR)
                print(Coinlerim[j]+"Kontrol ediliyor")
            except:
                print("Binance Bağlantı Hatası")
                j=j-1
                print(Coinlerim[j]+"Kontrol ediliyor")

                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': "Binance Bağlantı Hatası"}).json()
                except:
                    print("telegram baglantı hatası")



            try:
                arr=np.array(candles)

                (close, prevclose) = Getchartdata.getclose(arr)
                close = float(close)
                prevclose = float(prevclose)

                #RSI14 = MomentumIndicatorFunctions.getRSI14(GrafikDatalarınıCekmek.getopenarray(arr))
                (PSAR,PREVPSAR)=OverlapStudiesFunctions.getSAR(Getchartdata.gethigharray(arr), Getchartdata.getlowarray(arr))
                #(MACDHIST,PREVMACDHIST)=MomentumIndicatorFunctions.getMACD(GrafikDatalarınıCekmek.getclosearray(arr))
                #(sonhıst, onecekihıst, oncekindenoncekihıst) = MomentumIndicatorFunctions.getMACDEMA(GrafikDatalarınıCekmek.getclosearray(arr))
                #(STOCHRSIFAST, PREVSTOCHRSIFAST, STOCHRSISLOW,PREVSTOCHRSISLOW) = MomentumIndicatorFunctions.getSTOCHRSI( MomentumIndicatorFunctions.getRSIARRAY(GrafikDatalarınıCekmek.getclosearray(arr)))
                #(SUPERTREND_12_3, LASTSUPERTREND_12_3) = OverlapStudiesFunctions.getSUPERTREND_12_3(GrafikDatalarınıCekmek.gethigharray(arr), GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #(SUPERTREND_11_2, LASTSUPERTREND_11_2) = OverlapStudiesFunctions.getSUPERTREND_11_2(GrafikDatalarınıCekmek.gethigharray(arr), GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #(SUPERTREND_10_1, LASTSUPERTREND_10_1) = OverlapStudiesFunctions.getSUPERTREND_10_1(GrafikDatalarınıCekmek.gethigharray(arr), GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))

                #ALLSUPERTRENDLİNERED= SUPERTREND_12_3>close and  SUPERTREND_11_2>close and SUPERTREND_10_1>close
                #SUPERTRENDLİNERED= SUPERTREND_12_3>close


                #SUPERTRENDCROSSUP = SUPERTREND_12_3>close and LASTSUPERTREND_12_3<close
                #MACDCROSSDOWN=MACDHIST < 0 and PREVMACDHIST > 0
                PSARCROSSUP=(PSAR > close and PREVPSAR < prevclose) or (PSAR < close and PREVPSAR < prevclose)
                #STOCHRSICROSSDOWN = STOCHRSIFAST < STOCHRSISLOW and PREVSTOCHRSIFAST > PREVSTOCHRSISLOW

                #ADX = MomentumIndicatorFunctions.getADX(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #pDI = MomentumIndicatorFunctions.getPLUS_DI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #nDI = MomentumIndicatorFunctions.getMINUS_DI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #(LASTT3, PREVT3, PREVPREVT3, PREVPREVPREVT3) = OverlapStudiesFunctions.getT3(GrafikDatalarınıCekmek.getclosearray(arr), GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr), 3, 0.618)
                #IFTCCI = MomentumIndicatorFunctions.getIFTCCI(GrafikDatalarınıCekmek.gethigharray(arr),GrafikDatalarınıCekmek.getlowarray(arr),GrafikDatalarınıCekmek.getclosearray(arr))
                #TEMA8 = OverlapStudiesFunctions.getTEMA8(GrafikDatalarınıCekmek.getclosearray(arr))
                #TEMA21 = OverlapStudiesFunctions.getTEMA21(GrafikDatalarınıCekmek.getclosearray(arr))

                #T3TORED=(PREVT3>PREVPREVT3 and PREVPREVT3>LASTT3 and LASTT3>PREVPREVPREVT3) or (PREVPREVT3>PREVT3 and PREVT3>LASTT3 and LASTT3>PREVPREVPREVT3) or (PREVT3>PREVPREVT3 and PREVPREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>LASTT3) or (PREVPREVT3>PREVT3 and PREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>LASTT3 ) or (PREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>LASTT3 and LASTT3>PREVPREVT3) or (PREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVPREVT3 and PREVPREVT3>LASTT3) or (PREVPREVT3>PREVPREVPREVT3 and PREVPREVPREVT3>PREVT3 and PREVT3>LASTT3) or (PREVPREVPREVT3>PREVT3 and PREVT3>PREVPREVT3 and PREVPREVT3>LASTT3)
                #MACDDEMASAT= (sonhıst<0 and onecekihıst>0) or (oncekindenoncekihıst<0 and onecekihıst<0 and sonhıst<0) or ()
            except:
                print("Ta-lib Hesaplama Hatası")
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': "Ta-lib Hesaplama Hatası"}).json()
                except:
                    print("telegram baglantı hatası")


            if  (PSARCROSSUP):
                print(" SAT !!!!!!! " + Coinlerim[j] + " -----CLOSE--- " + str(close)  + " SAAT " + str(datetime.now()))
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': "SAT SAT SAT SAT SAT SAT SAT !!!!!!!!!! " + Coinlerim[j] + "-----CLOSE---" + str(close)  + " SAAT " + str(datetime.now())}).json()
                except:
                    print("telegram baglantı hatası")

                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id,'text': "SAT SAT SAT SAT SAT SAT SAT !!!!!!!!!! " + Coinlerim[j] + "-----CLOSE---" + str(close)  + " SAAT " + str(datetime.now())}).json()
                except:
                    print("telegram baglantı hatası")

                try:
                    try:
                        client = Client('--','---')
                        #getassettrdpair = client.get_asset_balance(asset=SatısCoinleri[j])
                        #balancetrdpair = float(getassettrdpair['free'])
                        order2 = client.order_market_sell(symbol=Coinlerim[j],quantity=float(math.floor(float(AldığımCoinlerinSayısı[j]) * (10**alınandp[j])) / (10**alınandp[j])))
                    except:
                        client = Client('---','---')
                        #getassettrdpair = client.get_asset_balance(asset=SatısCoinleri[j])
                        #balancetrdpair = float(getassettrdpair['free'])
                        order2 = client.order_market_sell(symbol=Coinlerim[j],quantity=float(math.floor(float(AldığımCoinlerinSayısı[j]) * (10**alınandp[j])) / (10**alınandp[j])))
                    KacinciTrade=KacinciTrade+1
                    orderrr2 = pd.DataFrame(order2)
                    a2 = orderrr2.iloc[0][13]
                    b2 = pd.DataFrame(a2, index=[0])
                    c2 = float(b2['price'])



                    Yk=float(((c2-CoinleriAldıgımFiyat[j])/CoinleriAldıgımFiyat[j])*100)-0.15
                    kumulatifYk=kumulatifYk+Yk
                    OrtalamaKar=float(kumulatifYk)/float(KacinciTrade)

                    print(str(KacinciTrade) + ".Trade---     " + Coinlerim[j] + "   SATILDI---   " + "   ALDIĞIM ZAMAN---    " + aldıgımzaman[j] +"    SATTIĞIM ZAMAN----    "+ str(datetime.now()) + "    SATTIĞIM  FİYAT---   " + str(c2) + "   ALDIGIM FİYAT---   " + str(CoinleriAldıgımFiyat[j]) + "  SATTIĞIM MİKTAR MİKTAR---    "  + str(AldığımCoinlerinSayısı[j]) + "   Yüzde Kar---      " + str(Yk) + "   Kumulutafif Yuzde kar---     " + str(kumulatifYk) + "Ortalama Yuzde kar---   " + str(OrtalamaKar))
                    try:
                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id,'text': str(KacinciTrade) + ".Trade---     " + Coinlerim[j] + "   SATILDI---   " + "   ALDIĞIM ZAMAN---    " + aldıgımzaman[j] +"    SATTIĞIM ZAMAN----    "+ str(datetime.now()) + "    SATTIĞIM  FİYAT---   " + str(c2) + "   ALDIGIM FİYAT---   " + str(CoinleriAldıgımFiyat[j]) + "  SATTIĞIM MİKTAR MİKTAR---    "  + str(AldığımCoinlerinSayısı[j]) + "   Yüzde Kar---      " + str(Yk) + "   Kumulutafif Yuzde kar---     " + str(kumulatifYk) + "Ortalama Yuzde kar---   " + str(OrtalamaKar)}).json()
                    except:
                        print("telegram baglantı hatası")

                    try:
                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id,'text': str(KacinciTrade) + ".Trade---     " + Coinlerim[j] + "   SATILDI---   " + "   ALDIĞIM ZAMAN---    " + aldıgımzaman[j] +"    SATTIĞIM ZAMAN----    "+ str(datetime.now()) + "    SATTIĞIM  FİYAT---   " + str(c2) + "   ALDIGIM FİYAT---   " + str(CoinleriAldıgımFiyat[j]) + "  SATTIĞIM MİKTAR MİKTAR---    "  + str(AldığımCoinlerinSayısı[j]) + "   Yüzde Kar---      " + str(Yk) + "   Kumulutafif Yuzde kar---     " + str(kumulatifYk) + "Ortalama Yuzde kar---   " + str(OrtalamaKar)}).json()
                    except:
                        print("telegram baglantı hatası")

                    aldıgımzaman.pop(j)
                    dp.append(alınandp[j])
                    trdPair.append(Coinlerim[j])
                    trdPair1.append(SatısCoinleri[j])
                    alınandp.pop(j)
                    Coinlerim.pop(j)
                    SatısCoinleri.pop(j)
                    CoinleriAldıgımFiyat.pop(j)
                    AldığımCoinlerinSayısı.pop(j)
                    YüzdeKar.append(Yk)

                    #now = datetime.datetime.now()
                    #x = (now.second) % 60
                    #y = 60 - x
                    #time.sleep(y)

                    #print(order2)
                    #print(Coinlerim)
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': Coinlerim}).json()
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': Coinlerim}).json()

                    #print(CoinleriAldıgımFiyat)
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': CoinleriAldıgımFiyat}).json()
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': CoinleriAldıgımFiyat}).json()

                    #print(AldığımCoinlerinSayısı)
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': AldığımCoinlerinSayısı}).json()
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': AldığımCoinlerinSayısı}).json()

                    #print(YüzdeKar)
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': YüzdeKar}).json()
                    #requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token2),data={'chat_id': chat_id, 'text': YüzdeKar}).json()

                except Exception as exp:
                    print(exp.status_code)
                    try:
                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': exp.status_code}).json()
                    except:
                        print("telegram baglantı hatası")

                    print(exp.message)
                    try:
                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': exp.message}).json()
                    except:
                        print("telegram baglantı hatası")


                j=j+1
            else:
                print(Coinlerim[j] + " Satış Şartları sağlamıyor --- " + " ALDIGIM FİYAT--- "+ str(CoinleriAldıgımFiyat[j]) + " CLOSE--- " + str(close))
                try:
                    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': Coinlerim[j] + " Satış Şartları sağlamıyor --- " + " ALDIGIM FİYAT--- "+ str(CoinleriAldıgımFiyat[j]) + " CLOSE--- " + str(close)}).json()
                except:
                    print("telegram baglantı hatası")

                j = j + 1
    print("Al SAT DÖNGÜSÜ TAMAMLANDI " +  str(datetime.now()))
    try:
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token1),data={'chat_id': chat_id, 'text': "Al SAT DÖNGÜSÜ TAMAMLANDI " +  str(datetime.now())}).json()
    except:
        print("telegram baglantı hatası")
