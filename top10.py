same=open('count.txt','r')
samelist=same.readlines()[0:9]
#print (samelist)
count=0

f=open('lab2-access-log.txt')
list2=f.readlines()
g=open('top10.txt','a')

for i in range(len(samelist)):
    count_d=0
    count_g=0
    count_p=0
    count_h=0
    count_d=0
    count_pu=0
    count_t=0
    count_c=0
    count_o=0
    count_to=0
    count_pf=0
    except10=samelist[i].split(' ')
    #print except10
    except10ip=except10[0]
    #print except10ip
    for line in list2:
      if except10ip in line:
         splitline=line.split('"')
         requestandpath= splitline[1]
         if len(requestandpath) >1:
            REQUESTANDPATH=requestandpath.split(' ')
            request= REQUESTANDPATH[0]
            if request=="GET":
              count_g=count_g+1
            elif request=="HEAD":
              count_h=count_h+1
            elif request=="POST":
              count_p=count_p+1
            elif request=="PUT":
              count_pu=count_pu+1
            elif request=="DELETE":
              count_d=count_d+1
            elif request=="TRACE":
              count_t=count_t+1
            elif request=="CONNECT":
              count_c=count_c+1
            elif request=="OPTIONS":
              count_o=count_o+1
            elif request=="PROPFIND":
              count_pf=count_pf+1
            else:
             pass
             
             
         if len(requestandpath) == 1:
           #print line
           count_to=count_to+1
           g.write("Timed Out request count is :%d %s"%(count_to,line))
    g.write("Ip is :%s"%(except10ip)+"\n"+"GET request count is :%d"%(count_g)+"\n"+"POST request count is :%d"%(count_p)+"\n"+"HEAD request count is :%d"%(count_h)+"\n"+"PUT request count is :%d"%(count_pu)+"\n"+"DELETE request count is :%d"%(count_d)+"\n"+"TRACE request count is :%d"%(count_t)+"\n"+"CONNECT request count is :%d"%(count_c)+"\n"+"OPTIONS request count is :%d"%(count_o)+"\n"+"PROPFIND request count is :%d"%(count_pf)+"\n")
    g.write("----------------------------------------------------------------------------------------------------------------"+"\n")
    
       
      
f.close()
g.close()
same.close()
