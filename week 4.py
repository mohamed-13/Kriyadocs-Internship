jd=pd.read_csv("C:/Users/admin/Job Decription final.csv")

requi=jd['Description']
final_dict={}
j=0
for i in requi:
        requi=list(i.split("."))
        final_dict[j]=requi
        j=j+1

        
final_list=[]
for key in final_dict:
    final_list.append(final_dict[key])

ser={job_gn[i]:final_list[i] for i in range(len(job_gn))}

new_skills=[]
for i in ser:
    job_list=[]
    job_list.append(i)
    
    job_list.append(ser[i])
    new_skills.append(job_list)

rank_skills=[]
for i in required_skills:
    count=0
    for j in ser:
        
            if i==ser[j]:
                count +=1
                rank_skills[i]=count


a=0
while(a<len(required_skills)):
    count=0
    lt=[]
    for i in range(len(new_skills)):
        for j in range(len(new_skills[i][1])):
            if required_skills[a] in new_skills[i][1][j]:
                count += 1
                s=required_skills[a]
                #print(s)
                lt.append(new_skills[i][0])
                skills_dict[s] = [count,lt]
                
    a +=1


rank_list=sorted(skills_dict)
print('The most on demand skills and their respective jobs: ")
for i in rank_list:
  print(i," ",skills_dict[i])
