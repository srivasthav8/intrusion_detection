Execution of python file in Ubuntu:
$ python pythonfile
To get the results of the top 10 clients and also what requests does the most active client make?
cs.py
O/P for Q6: count.txt,top10.txt
O/P for mostactive_request.txt
To analyse the requests of the top 10 clients (Q NO:7 and 9)
top10.py
O/P for Q7: top10.txt
To analyse the requests of the remaining clients (Q No:9)
q9.py
O/P for Q9: q9.txt
Malicious attacks
q1-q5.py
O/P for Q2: bm.txt
O/P for Q3: threats.txt
Cs.py:


REQUESTS WILL BE IN THE FOLLOWING WAY:

2002-12-01 00.00.09 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/05_djycablecar.jpg HTTP/1.1" 200 978184
2002-12-01 00.00.25 nat4-083.rz.uni-karlsruhe.de "GET /~rjmh/tutorials.html HTTP/1.0" 200 6201
2002-12-01 00.00.36 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/06_djybaopingkou.jpg HTTP/1.1" 200 29121
2002-12-01 00.00.46 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/07_djybaopingkou2.jpg HTTP/1.1" 200 847397
2002-12-01 00.00.53 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/08a_dujiangyan01.jpg HTTP/1.1" 200 692342
2002-12-01 00.00.55 crawl15-public.alexa.com "GET /robots.txt HTTP/1.0" 301 243
2002-12-01 00.00.56 crawl15-public.alexa.com "GET /~reiner/Lehre/strein/sld024.htm HTTP/1.0" 200 2119
2002-12-01 00.01.01 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/08b_dujiangyan02.jpg HTTP/1.1" 200 739212
2002-12-01 00.01.14 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/09a_fishmouse.jpg HTTP/1.1" 200 38119
2002-12-01 00.01.26 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/09b_dujiangyandivide.jpg HTTP/1.1" 200 839193
2002-12-01 00.01.30 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/10a_djyoverview.jpg HTTP/1.1" 200 60047
2002-12-01 00.01.41 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/15a_Panda_Wolong.jpg HTTP/1.1" 200 47341
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/lic-thesis/pure-functional-parsing.ps HTTP/1.0" 304 -
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/parsers/AmbExTrie.hs HTTP/1.0" 304 -
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/parsers/AmbTrie.hs HTTP/1.0" 304 -
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/parsers/ContTrans.hs HTTP/1.0" 304 -
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/parsers/ExTrie.hs HTTP/1.0" 304 -
2002-12-01 00.01.45 vvv.adm.chalmers.se "GET /~peb/parsing/parsers/ExampleParsers.hs HTTP/1.0" 304 -
2002-12-01 00.01.46 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/OrdMap.hs HTTP/1.0" 404 556
2002-12-01 00.01.46 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/OrdSet.hs HTTP/1.0" 404 556
2002-12-01 00.01.47 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/algorithms/ HTTP/1.0" 404 558
2002-12-01 00.01.47 gminlap1.eimc.brad.ac.uk "GET /~yzhang/presentation/19a_Valley.jpg HTTP/1.1" 200 73745
2002-12-01 00.01.47 benny.olofshojd.studenthem.gu.se "GET /Cs/Grundutb/Kurser/e3ptfk/ HTTP/1.1" 200 17914
2002-12-01 00.01.48 benny.olofshojd.studenthem.gu.se "GET /Cs/Grundutb/Kurser/e3ptfk/dsj2.jpg HTTP/1.1" 200 35050
2002-12-01 00.01.49 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/collecting-parser/ HTTP/1.0" 404 565
2002-12-01 00.01.49 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/lic-thesis/ HTTP/1.0" 404 558
2002-12-01 00.01.50 vvv.adm.chalmers.se "GET /~peb/parsing/algorithms/parsers/ HTTP/1.0" 404 555
2002-12-01 00.01.51 vvv.adm.chalmers.se "GET /~peb/parsing/collecting-parser/OrdMap.hs HTTP/1.0" 404 563
2002-12-01 00.01.51 vvv.adm.chalmers.se "GET /~peb/parsing/collecting-parser/OrdSet.hs HTTP/1.0" 404 563


Due to size factor all requests are not uploaded.
