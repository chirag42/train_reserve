import sqlite3
conn3=sqlite3.connect('login.db')
with conn3:
    c3=conn3.cursor()
#create table headings
c3.execute('CREATE TABLE IF NOT EXISTS TRAIN_12951(HALT_NO INTEGER \
,STATION_NAME TEXT,ARRIVAL_TIME TEXT, DEPARTURE_TIME TEXT,HALT_TIME TEXT,\
DAY INTEGER,DISTANCE[IN KM] INTEGER)')
#insert stations
c3.execute('INSERT INTO TRAIN_12951 VALUES(1,"MUMBAI CENTRAL","SOURCE","17:00",\
"---",1,0)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(2,"BORIVALI","17:30","17:32",\
"2",1,30)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(3,"SURAT","19:53","19:58",\
"5",1,263)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(4,"VADODARA JN","21:18","21:28",\
"10",1,392)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(5,"RATLAM JN","00:37","00:40",\
"3",2,653)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(6,"NAGDA JN","01:18","01:20",\
"2",2,695)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(7,"KOTA JN","03:20","03:25",\
"2",2,920)')
conn3.commit()
c3.execute('INSERT INTO TRAIN_12951 VALUES(8,"NEW DELHI","08:35","END",\
"---",2,1351)')
conn3.commit()
conn3.close()
