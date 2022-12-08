import pandas as pd
from nltk.corpus import stopwords
j2=pd.read_csv("C:/Users/admin/Job Decription final.csv")
stop = stopwords.words('english')
j2['Description'] = j2['Description'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
j2['Description']=j2['Description'].apply(lambda x: " ".join(x.lower()for x in x.split()))
j=pd.read_csv("C:/Users/admin/Jobs.csv")
j=j.drop("Unnamed: 0",axis=1)

### SQLite3 Connection

import sqlite3
import csv



cursor.execute("""CREATE TABLE jobs(
        "S.no" TEXT,
        "index" TEXT,
        "job_name" TEXT,
        "skills_req" TEXT
) """)


connection.commit()
with open('C:/Users/admin/Jobs.csv','r') as file:
    for row in file:
        cursor.execute("INSERT INTO jobs VALUES(?,?,?,?)",row.split(','))
        connection.commit()
        n += 1

connection.close()

required_skills=["machine learning",'python','numpy','data science','database','sql','programming','communication','mathematics']
skills_dict={}
for i in required_skills:
    skills_dict[i]=0

job_gn=j['Job Title']
job_gn.to_list()

req=j['Description']
req.to_list()

