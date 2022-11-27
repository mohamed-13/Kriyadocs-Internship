#importing necessary libraries

import pandas as pd
import nltk
from nltk.corpus import stopwords

#storing the data 
jd=pd.read_csv("C:/Users/admin/Job Decription.csv")

#removing the unwanted characters in job title
job_title=[]
jt=jd['Job Title']
for i in jt:
    i=i.replace('-'," ")
    i=i.replace('description'," ")
    i=i.title()
    print(i)
    job_title.append(i)
job_title
jd.drop('JOB TITLE',axis=1)


#inserting the a new column with new clean job titles
jd.insert(1,column='JOB TITLE',value=job_title)

#removing the old columns
jd.drop('Job Title',axis=1,inplace=True)
jd.head()

#removing punctuations and converting all the ctring in decription to lower case
jd['Description']=jd['Description'].apply(lambda x: " ".join(x.lower()for x in x.split()))

#removing stopwords 
stop = stopwords.words('english')
jd['Description'] = jd['Description'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
