import sqlite3
import random
conn5=sqlite3.connect('login.db')
with conn5:
    cursor=conn5.cursor()
cursor.execute('DROP TABLE booking1')
cursor.execute('CREATE TABLE IF NOT EXISTS booking1 (USERNAME TEXT,PNR TEXT,TRAIN_NO TEXT,NAME TEXT,FROM_STAT TEXT,TO_STAT TEXT,DOJ TEXT,GENDER INT ,AGE INT)')
conn5.commit()
conn5.close()
