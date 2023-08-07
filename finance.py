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
    sector_list.append("FINANCE")
print(sector_list)


#nifty list
tickers_list1=['^NSEI']
nifty_list=[]
nifty_list=[yf.download(tickers_list1,'2022-03-01')['Adj Close']]
list1 =nifty_list[0].tolist()
print(list1)
print(len(list1))





tickers_list2=['RELIANCE.NS']
reliance_list=[]
reliance_list=[yf.download(tickers_list2,'2022-03-01')['Adj Close']]
list2 =reliance_list[0].tolist()
print(list2)


tickers_list3=['MUTHOOTFIN.NS']
muthoot_list=[]
muthoot_list=[yf.download(tickers_list3,'2022-03-01')['Adj Close']]
list3 =muthoot_list[0].tolist()
print(list3)


tickers_list4=['BAJFINANCE.NS']
bajaj_list=[]
bajaj_list=[yf.download(tickers_list4,'2022-03-01')['Adj Close']]
list4 =bajaj_list[0].tolist()
print(list4) 

tickers_list5=['IIFL.NS']
iifl_list=[]
iifl_list=[yf.download(tickers_list5,'2022-03-01')['Adj Close']]
list5 =iifl_list[0].tolist()
print(list5)

tickers_list6=['ABSLAMC.NS']
absl_list=[]
absl_list=[yf.download(tickers_list6,'2022-03-01')['Adj Close']]
list6 =absl_list[0].tolist()
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

RELIANCEList = myfunction(list2)
MUTHOOTList = myfunction(list3)
BAJAJList = myfunction(list4)
IIFLList = myfunction(list5)
ABSLList = myfunction(list6)

Date=date_list
Sector=sector_list
rsRELIANCE = RELIANCEList[0]
rmRELIANCE = RELIANCEList[1]
rsMUTHOOT = MUTHOOTList[0]
rmMUTHOOT = MUTHOOTList[1]
rsBAJAJ = BAJAJList[0]
rmBAJAJ= BAJAJList[1]
rsIIFL = IIFLList[0]
rmIIFL = IIFLList[1]
rsABSL = ABSLList[0]
rmABSL = ABSLList[1]


import csv

# Sample list of values
values = [Date,Sector,rsRELIANCE,rmRELIANCE,rsMUTHOOT,rmMUTHOOT,rsBAJAJ,rmBAJAJ,rsIIFL,rmIIFL,rsABSL,rmABSL]

# Transpose the list using zip()
columns = list(zip(*values))

# Define column names
header = ['Date','Sector','rsRELIANCE', 'rmRELIANCE', 'rsMUTHOOT','rmMUTHOOT','rsBAJAJ','rmBAJAJ','rsIIFL','rmIIFL','rsABSL','rmABSL']

# Write the columns to a CSV file with header row
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for column in columns:
        writer.writerow(column)

