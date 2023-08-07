import statistics
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import csv



#date
nifty_data = yf.download("^NSEI", start="2022-04-03", end="2023-05-07")
nifty_dates = pd.DataFrame(nifty_data.index.date, columns=["Date"])
date_list = nifty_dates["Date"].apply(lambda x: x.strftime('%Y-%m-%d')).tolist()
print(date_list)
length=len(date_list)
print (length)

sector_list=[]
for i in range (0,length):
    sector_list.append("BANKING")
print(sector_list)


#nifty list
tickers_list1=['^NSEI']
nifty_list=[]
nifty_list=[yf.download(tickers_list1,'2022-04-03')['Adj Close']]
list1 =nifty_list[0].tolist()
print(list1)
print(len(list1))




tickers_list2=['HDFCBANK.NS']
hdfc_list=[]
hdfc_list=[yf.download(tickers_list2,'2022-04-03')['Adj Close']]
list2 =hdfc_list[0].tolist()
print(list2)


tickers_list3=['ICICIBANK.NS']
icici_list=[]
icici_list=[yf.download(tickers_list3,'2022-04-03')['Adj Close']]
list3 =icici_list[0].tolist()
print(list3)


tickers_list4=['KOTAKBANK.NS']
kotak_list=[]
kotak_list=[yf.download(tickers_list4,'2022-04-03')['Adj Close']]
list4 =kotak_list[0].tolist()
print(list4)

tickers_list5=['AXISBANK.NS']
axis_list=[]
axis_list=[yf.download(tickers_list5,'2022-04-03')['Adj Close']]
list5 =axis_list[0].tolist()
print(list5)

tickers_list6=['SBIN.NS']
sbi_list=[]
sbi_list=[yf.download(tickers_list6,'2022-04-03')['Adj Close']]
list6 =sbi_list[0].tolist()
print(list6)

n1 = list1.__len__() - 1

def myfunction(list):

    MasterList = []
    # PR
    PR_list = []
    for i in range(0, n1):
        PR = (list[i] / list1[i]) * 100
        PR_list.append(PR)
    #print('PR list: ', PR_list)
    
    
    # mean
    sum = 0
    std_dev = 0
    for i in range(0, n1):
        sum = sum + PR_list[i]
        std_dev = statistics.stdev(PR_list)
    mean = sum / n1


    # Rs-ratio
    RS_list = []
    for i in range(0, n1):
        RS_ratio = 101 + ((PR_list[i] - mean) / std_dev)
        RS_list.append(RS_ratio)

    MasterList.append(RS_list)

    # ROC
    ROC_list = []
    for i in range(0, n1 - 1):
        ROC = ((RS_list[i] / RS_list[i + 1]) - 1) * 100
        ROC_list.append(ROC)
    
    sum1 = 0
    std_dev1 = 0
    for i in range(0, n1 - 1):
        sum1 = sum1 + ROC_list[i]
        std_dev1 = statistics.stdev(ROC_list)
    mean1 = sum1 / n1 - 1
    

    # RS Momentum
    Momentum_list = []
    for i in range(0, n1 - 1):
        RS_momentum = 101 + ((ROC_list[i] - mean1) / std_dev1)
        Momentum_list.append(RS_momentum)
    #print('RS momentum list is: ', Momentum_list)
    MasterList.append(Momentum_list)

    return MasterList

HDFCList = myfunction(list2)
ICICIList = myfunction(list3)
KOTAKList = myfunction(list4)
AXISList = myfunction(list5)
SBIList = myfunction(list6)

Date=date_list
Sector=sector_list
rsHDFC = HDFCList[0]
rmHDFC = HDFCList[1]
rsICICI = ICICIList[0]
rmICICI = ICICIList[1]
rsKOTAK = KOTAKList[0]
rmKOTAK = KOTAKList[1]
rsAXIS = AXISList[0]
rmAXIS = AXISList[1]
rsSBI = SBIList[0]
rmSBI = SBIList[1]


import csv


values = [Date,Sector,rsHDFC,rmHDFC,rsICICI,rmICICI,rsKOTAK,rmKOTAK,rsAXIS,rmAXIS,rsSBI,rmSBI]


columns = list(zip(*values))


header = ['Date','Sector','rsHDFC', 'rmHDFC', 'rsICICI','rmICICI','rsKOTAK','rmKOTAK','rsAXIS','rmAXIS','rsSBI','rmSBI']


with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for column in columns:
        writer.writerow(column)

