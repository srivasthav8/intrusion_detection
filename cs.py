
################################################## QUESTION 6  ##########################################################
f=open('lab2-access-log.txt')
lists=f.readlines()
linel=0
for line in lists:
    linel=linel+1
    n=open("same.txt","a")
    logs=line.split(' ')
    hostname=logs[2]
    n.write(hostname)
    n.write("\n")
    n.close()
f.close()
#print linel

import collections

with open('same.txt') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, countip in counts.most_common():
    #print line,count
    counter=open("count.txt","a")
    counter.write("%s is repeated:%s"%(line,countip))
    #count.write(str(count))
    counter.write("\n")
    counter.close

#######################################################  QUESTION 7 ###################################################
most=open('count.txt','r')
mostlist=most.readlines()[0]
sep=mostlist.split(' ')
mostactive=sep[0]
count=0
f=open('lab2-access-log.txt')
list2=f.readlines()
g=open('mostactive_request.txt','a')
for line in list2:
   if mostactive in line:
       #print line
       requestsplit=line.split('"')
       requestandpath = requestsplit[1]
       REQUESTANDPATH= requestandpath.split(' ')
       REQUEST= REQUESTANDPATH[0]
       count = count+1
       if REQUEST=="GET":
          g.write("Log of the Get request is :%s"%(line)+"Its count is :%d"%(count)+"\n")
g.close()
f.close()

