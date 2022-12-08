import requests
import bs4
import csv

#open a file

#request to get the website
res=requests.get("https://www.betterteam.com/job-description")
bs=bs4.BeautifulSoup(res.text,"html.parser")

#create a list with class name 
base=bs.select('.col-md-6.item')
i=0
requirements=[]
fd=[]
job=[]

joblist=["Machine Learning","Data Scientist","Data Analyst","Python Developer"]

while i!=len(base):
    #initialize each element of list to ul
    ul=base[i]
    #print("----------------------------------------------------------------")

    #get only the link from each href
    link_text=ul.select('a')[0].getText()
    link=""

    for item in joblist:
        if item in link_text:
            link=ul.select('a')[0]['href']
            job.append(link[27:])

        
            #next linked page
            req=requests.get(link)
            bea=bs4.BeautifulSoup(req.text,"html.parser")
            #the 3rd ul in the page has the job requierments
            li=bea.select('ul')[3]
            li=bea.select('ul')[3]
            li=str(li)
            requirements.append(li[8:])
    i=i+1
    #get each requierments and store it in a file
one=requirements[1]

fd=[]
for i in range(len(requirements)):
    s=requirements[i]
    s=s.replace('</li>',' ')
    s=s.replace('<li>',' ')
    s=s.replace('<ul>',' ')
    s=s.replace('</ul'," ")
    s=s.replace('<'," ")
    fd.append(s)


file_name='Job Decription final.csv'
with open(file_name,'w',encoding='utf-8') as f:
    f.write=csv.writer(f)
    f.write.writerow(['Index','Job Title','Description'])
    
    for i in range(len(job)):
        f.write.writerow([i+1,job[i],fd[i]])

   



