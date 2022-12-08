import pandas as pd
jd=pd.read_csv("C:/Users/admin/Job Decription final.csv")
inplace=True

job_title=[]
jt=jd['Job Title']
for i in jt:
    i=i.replace('-'," ")
    i=i.replace('description'," ")
    i=i.title()
    job_title.append(i)
jd.insert(1,column='JOB TITLE',value=job_title)

jd['Description']=jd['Description'].apply(lambda x: " ".join(x.lower()for x in x.split()))
jd['Description'] = jd['Description'].str.replace('[^\w\s]',' ')

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import Word

stop = stopwords.words('english')
jd['Description'] = jd['Description'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


