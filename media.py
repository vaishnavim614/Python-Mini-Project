import statistics
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import csv



#date
nifty_data = yf.download("^NSEI", start="2022-03-01", end="2023-05-07")
nifty_dates = pd.DataFrame(nifty_data.index.date, columns=["Date"])
date_list = nifty_dates["Date"].apply(lambda x: x.strftime('%Y-%m-%d')).tolist()
print(date_list)
length=len(date_list)
print (length)

sector_list=[]
for i in range (0,length+1):
    sector_list.append("MEDIA")
print(sector_list)


#nifty list
tickers_list1=['^NSEI']
nifty_list=[]
nifty_list=[yf.download(tickers_list1,'2022-03-01')['Adj Close']]
list1 =nifty_list[0].tolist()
print(list1)
print(len(list1))





tickers_list2=['PVR.NS']
pvr_list=[]
pvr_list=[yf.download(tickers_list2,'2022-03-01')['Adj Close']]
list2 =pvr_list[0].tolist()
print(list2)


tickers_list3=['TV18BRDCST.NS']
tv18_list=[]
tv18_list=[yf.download(tickers_list3,'2022-03-01')['Adj Close']]
list3 =tv18_list[0].tolist()
print(list3)


tickers_list4=['ZEEL.NS']
zee_list=[]
zee_list=[yf.download(tickers_list4,'2022-03-01')['Adj Close']]
list4 =zee_list[0].tolist()
print(list4) 

tickers_list5=['SAREGAMA.NS']
saregama_list=[]
saregama_list=[yf.download(tickers_list5,'2022-03-01')['Adj Close']]
list5 =saregama_list[0].tolist()
print(list5)

tickers_list6=['DISHTV.NS']
dishtv_list=[]
dishtv_list=[yf.download(tickers_list6,'2022-03-01')['Adj Close']]
list6 =dishtv_list[0].tolist()
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

PVRList = myfunction(list2)
TV18List = myfunction(list3)
ZEEList = myfunction(list4)
SAREGAMAList = myfunction(list5)
DISHTVList = myfunction(list6)

Date=date_list
Sector=sector_list
rsPVR = PVRList[0]
rmPVR = PVRList[1]
rsTV18 = TV18List[0]
rmTV18= TV18List[1]
rsZEE =ZEEList[0]
rmZEE= ZEEList[1]
rsSAREGAMA = SAREGAMAList[0]
rmSAREGAMA = SAREGAMAList[1]
rsDISHTV = DISHTVList[0]
rmDISHTV = DISHTVList[1]


import csv

# Sample list of values
values = [Date,Sector,rsPVR,rmPVR,rsTV18,rmTV18,rsZEE,rmZEE,rsSAREGAMA,rmSAREGAMA,rsDISHTV,rmDISHTV]

# Transpose the list using zip()
columns = list(zip(*values))

# Define column names
header = ['Date','Sector','rsPVR','rmPVR','rsTV18','rmTV18','rsZEE','rmZEE','rsSAREGAMA','rmSAREGAMA','rsDISHTV','rmDISHTV']

# Write the columns to a CSV file with header row
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for column in columns:
        writer.writerow(column)

