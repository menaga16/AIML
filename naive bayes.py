#DESIGN A PROGRAM USING NAIVE BAYESIAN CLASSIFIER FOR A SAMPLE TRAINING DATASET STORED AS A CSV FILE


#naive bayes
import numpy as np
import pandas as pd
data=pd.read_csv('Dataset.csv')
data.head()
data
data['BuysComputer'].value_counts()
p_yes=4/10
p_no=6/10
print(p_yes)
print(p_no)
pd.crosstab(data['Income'],data['BuysComputer'])

p_10_no=3/6
p_25_no=0
p_30_no=1/6
p_35_no=2/6

p_10_yes=0
p_25_yes=2/4
p_30_yes=2/4
p_35_yes=0

pd.crosstab(data['Age'],data['BuysComputer'])

p_20a_no=2/6
p_25a_no=3/6
p_35a_no=1/6

p_20a_yes=2/4
p_25a_yes=2/4
p_35a_yes=0

pyes=p_yes*p_30_yes*p_20a_yes
print(pyes)
pno=p_no*p_30_no*p_20a_no
print(pno)
if(pyes >= pno):
 print(pyes, "user will Buy computer")
else:
 print(pno, "user will not Buy computer")



#DATA SET:

#Age,Income,BuysComputer
#30,25000,Yes
#40,45000,No
#20,20000,No
#25,26000,Yes
#35,35000,Yes
#35,35000,Yes
#35,35000,Yes
#35,35000,Yes

