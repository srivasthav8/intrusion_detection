
########################################### QUESTION3 ###########################################

a=open('lab2-access-log.txt')
lines=a.readlines()
count=0

A=open('threats.txt','a')

A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Cross Site Request Forgery:"+"\n")
for line in lines:
   logs=line.split('"')
   crosssite=".php?"   
   requestsplit=line.split('"')
   getandpath= requestsplit[1]  
   REQUEST=getandpath.split(' ')
   if len(REQUEST)>1:
          path=REQUEST[1]
          request=REQUEST[0]
          if  crosssite in path:
             A.write("Malicious Request may be :%s"%(line)+"\n")

A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Information Leakage and Improper Error Handling:"+"\n") 
for line in lines:
    logs=line.split(' ')
    ia6="aves.viktorrydberg.studenthem.gu.se"
    if ia6 in line:
      if ( logs[6] > '400'):
         A.write("Malicious Request may be :%s"%(line)+"\n")
      
A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Broken Authentication and Session Management:"+"\n")
import re
for line in lines:
    logs=line.split(' ')
    ia7="61.95.23.158"
    if ia7 in line:
       request=logs[4]
       pattern = re.compile("\/\w+\/\w+\.\w+\?\w+\=\w\&\w+\=+\w\&\w+\=\w+\&\w+\=\w\&\w+\=+\w")
       if pattern.match(request):
          A.write("Malicious Request may be :%s"%(line)+"\n")

A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Insecure Direct Object Reference:"+"\n")
for line in lines:
    logs=line.split(' ')
    request=logs[4]
    pattern = re.compile("\/\w+\/..\%\w+\%\w+..\/\w+\/+\w+\/+cmd.exe\?\/+\w+\+\w+")
    if pattern.match(request):
       A.write("Malicious Request may be :%s"%(line)+"\n")

A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Malicious File Execution:"+"\n")
for line in lines:
    logs=line.split(' ')
    ia3="sakalthor.dd.chalmers.se"
    if ia3 in line:
      request=logs[4]
      malicious="?http:"
      if malicious in request:
          A.write("Malicious Request may be :%s"%(line)+"\n")

A.write("-------------------------------------------------------------------------------------------------------------------------------"+"\n")
A.write("Injection Flaws:"+"\n")
import re
for line in lines:
    logs=line.split(' ')
    ia2="210.114.220.220"
    if ia2 in line:
       request=logs[4]
       pattern = re.compile("[\/]\w+\.[a-z]+\?[A-Z]+\=[a-z]")
       if pattern.match(request):
          A.write("Malicious Request may be :%s"%(line)+"\n")
A.close()
a.close()


##################################################  QUESTION 2  ############################################################
b=open('lab2-access-log.txt')
lines=b.readlines()

count4=0
count400=0
count401=0
count402=0
count403=0
count404=0
count405=0
count406=0
count407=0
count408=0
count409=0
count416=0
count500=0
others=0
len5=0
len6=0
len7=0
bm=open('bm.txt','a')
bm.write("Benign and Malicious errors : Client Side"+"\n")
for line in lines:
    bmlogs=line.split(' ')    
    #print bmlogs
    if len(bmlogs) == 8:
      status=bmlogs[6]

      if (status >='400'):
        #print status
        

        count4=count4+1
        
        if status=='400':
          bm.write("Bad Request :"+"\n")
          count400=count400+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
       
        if status=='401':
          bm.write("Unauthorized Request :"+"\n")
          count401=count401+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='402':
          bm.write("Payment Required :"+"\n")
          count402=count402+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='403':
          bm.write("Forbidden Request :"+"\n")
          count403=count403+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='404':
          #bm.write("Not found :"+"\n")
          count404=count404+1
          #bm.write("Malicious Access may be :%s"%(line)+"\n")
          #bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='405':
          bm.write("Method not allowed :"+"\n")
          count405=count405+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='406':
          bm.write("Not acceptible:"+"\n")
          count406=count406+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='407':
          bm.write("Proxy Authentication Required  :"+"\n")
          count407=count407+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='408':
          bm.write("Request Timed Out :"+"\n")
          count408=count408+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='409':
          bm.write("Conflict :"+"\n")
          count409=count409+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
       
        if status=='416':
          bm.write("Range not Satisfiable :"+"\n")
          count416=count416+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")
        
        if status=='500':
          bm.write("Internal Server Error :"+"\n")
          count500=count500+1
          bm.write("Malicious Access may be :%s"%(line)+"\n")
          bm.write("-------------------------------------------------------------------------------------------------------------------"+"\n")

    if len(bmlogs)<8:
       others=others+1
       if len(bmlogs)==6:
          len6=len6+1
          othersstatus=bmlogs[4]
          if othersstatus == '408' :
            bm.write("Request Timed Out : *** Special Cases ***"+"\n")
            bm.write("Malicious Access may be :%s"%(line)+"\n")
            bm.write("------------------------------------------------------------------------------------------------------------------"+"\n")
          else:
             pass
             
       if len(bmlogs)==7:
          len7=len7+1
          othersstatus=bmlogs[5]
          if othersstatus=='404':
            #bm.write("Not found :"+"\n")
            #bm.write("Malicious Access may be :%s"%(line)+"\n")
            #bm.write("-----------------------------------------------------------------------------------------------------------------"+"\n")
            pass

bm.close()

#################################################### 	QUESTION5   ################################################################

c=open('lab2-access-log.txt')
lines=c.readlines()
count12=count11=count10=0
for line in lines:
    amlogs=line.split(' ')
    ip=amlogs[2]
    
    if ip=="crawler12.googlebot.com":
       count12=count12+1
    
    elif ip=="crawler11.googlebot.com":
       count11=count11+1
    
    elif ip=="crawler10.googlebot.com":
       count10=count10+1
 
    else:
       pass

#print count12
#print count11
#print count10


