import csv
import math
import pandas as pd
import operator


path=input('Enter user-item matrix address')
neigh=int(input('Enter neighborhood size'))
u_id=input('Enter user ID')
m_id=input('Enter item ID')

path=r'C:\Users\pegah\Desktop\univ\social media mining\hw\hw5\ml-20m\ml-20m\ratings.csv'
#read file
with open(path) as f:
    ratings=[tuple(line) for line in csv.reader(f)]
ratings.remove(ratings[0])
rat=pd.DataFrame([x[1:3] for x in ratings], index = [x[0] for x in ratings])

#user based cf
#get all movies of user u_id
u_dic={}
for i in range(len(ratings)):
    if ratings[i][0]==u_id:
        u_dic[ratings[i][1]]=ratings[i][2]
#get similiarities
sim={}
nume=0
den1=0
den2=0
for i in range(1,100):
    if str(i)!=u_id:
        r=rat.loc[str(i)]
        for j in range(len(r)):
            if r.iloc[j,0] in u_dic.keys():
                if r.iloc[j,0]!=m_id:
                    nume=nume+float(r.iloc[j,1])*float(u_dic[r.iloc[j,0]])
                    den1=den1+float(r.iloc[j,1])*float(r.iloc[j,1])
                    den2=den2+float(u_dic[r.iloc[j,0]])*float(u_dic[r.iloc[j,0]])
        sim[i]=nume/(math.sqrt(den1)*math.sqrt(den2))
#average of u_id ratings
s=0
l=0
for i in u_dic.keys():
    if i!=m_id:
        s=s+float(u_dic[i])
        l=l+1
avg_u_id=s/l
#rating of neighbors for m_id , their average ranking and final ranking of u_id for m_id
s1=0
s2=0
s3=0
m_id_neigh={}
avg_neigh={}
#get most similar neighbors
sorted_sim=dict(sorted(sim.items(), key=operator.itemgetter(1), reverse=True)[:neigh])
#rating of neighbors for movie m_id
for k in sorted_sim.keys():
    r=rat.loc[str(i)]
    for j in range(len(r)):
        if r.iloc[j,0]==m_id:
            m_id_neigh[k]=float(r.iloc[j,1])
#mean of neighborhood rating
for k in sorted_sim.keys():
    r=rat.loc[str(i)]
    for j in range(len(r)):
        s2=s2+float(r.iloc[j,1])
    avg_neigh[k]=s2/len(r)
    s2=0
#final rank
for i in sorted_sim.keys():
    s1=s1+(sorted_sim[i]*(m_id_neigh[i]-avg_neigh[i]))
    s3=s3+sorted_sim[i]
final_rank=avg_u_id+(s1/s3)
final_rank