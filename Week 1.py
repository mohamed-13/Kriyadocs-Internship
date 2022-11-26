import requests
import bs4
import csv


res=requests.get("https://www.betterteam.com/job-description")
bs=bs4.BeautifulSoup(res.text,"html.parser")

#create a list with class name 
base=bs.select('.col-md-6.item')
i=0
job=[]
requirements=[]


while i!=5:
    #initialize each element of list to ul
    ul=base[i]
  

    #fetching link from anchor tag
    link=ul.select('a')[0]['href']
    
    job.append(link[27:])
    #next linked page 
    req=requests.get(link)
    bea=bs4.BeautifulSoup(req.text,"html.parser")

    #Getting requirement from the redirected page
    li=bea.select('ul')[3]
    li=str(li)
    requirements.append(li[8:])
    i=i+1
    #get each requierments and store it in a file

#replacing list tags present in the description
fd=[]
for i in range(len(requirements)):
    s=requirements[i]
    s=s.replace('</li>',' ')
    s=s.replace('<li>',' ')
    s=s.replace('<ul>',' ')
    s=s.replace('</ul'," ")
    s=s.replace('<'," ")
    fd.append(s)

#Storing the details in a csvfile
file_name='Job Decription.csv'
with open(file_name,'w',encoding='utf-8') as f:
    f.write=csv.writer(f)
    f.write.writerow(['Index','Job Title','Description'])
    
    for i in range(len(job)):
        f.write.writerow([i+1,job[i],fd[i]])
