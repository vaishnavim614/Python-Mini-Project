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
for i in range (0,length):
    sector_list.append("PHARMA")
print(sector_list)


#nifty list
tickers_list1=['^NSEI']
nifty_list=[]
nifty_list=[yf.download(tickers_list1,'2022-03-01')['Adj Close']]
list1 =nifty_list[0].tolist()
print(list1)





tickers_list2=['AARTIDRUGS.NS']
aarti_list=[]
aarti_list=[yf.download(tickers_list2,'2022-03-01')['Adj Close']]
list2 =aarti_list[0].tolist()
print(list2)


tickers_list3=['CIPLA.NS']
cipla_list=[]
cipla_list=[yf.download(tickers_list3,'2022-03-01')['Adj Close']]
list3 =cipla_list[0].tolist()
print(list3)


tickers_list4=['PFIZER.NS']
pfizer_list=[]
pfizer_list=[yf.download(tickers_list4,'2022-03-01')['Adj Close']]
list4 =pfizer_list[0].tolist()
print(list4) 

tickers_list5=['SUNPHARMA.NS']
sun_list=[]
sun_list=[yf.download(tickers_list5,'2022-03-01')['Adj Close']]
list5 =sun_list[0].tolist()
print(list5)

tickers_list6=['AJANTPHARM.NS']
ajanta_list=[]
ajanta_list=[yf.download(tickers_list6,'2022-03-01')['Adj Close']]
list6 =ajanta_list[0].tolist()
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

AARTIList = myfunction(list2)
CIPLAList = myfunction(list3)
PFIZERList = myfunction(list4)
SUNList = myfunction(list5)
AJANTAList = myfunction(list6)

Date=date_list
Sector=sector_list
rsAARTI = AARTIList[0]
rmAARTI = AARTIList[1]
rsCIPLA = CIPLAList[0]
rmCIPLA = CIPLAList[1]
rsPFIZER = PFIZERList[0]
rmPFIZER= PFIZERList[1]
rsSUN = SUNList[0]
rmSUN = SUNList[1]
rsAJANTA = AJANTAList[0]
rmAJANTA = AJANTAList[1]


import csv

# Sample list of values
values = [Date,Sector,rsAARTI,rmAARTI,rsCIPLA,rmCIPLA,rsPFIZER,rmPFIZER,rsSUN,rmSUN,rsAJANTA,rmAJANTA]

# Transpose the list using zip()
columns = list(zip(*values))

# Define column names
header = ['Date','Sector','rsAARTI', 'rmAARTI', 'rsCIPLA','rmCIPLA','rsPFIZER','rmPFIZER','rsSUN','rmSUN','rsAJANTA','rmAJANTA']

# Write the columns to a CSV file with header row
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for column in columns:
        writer.writerow(column)

