# -*- coding: utf-8 -*-

import sqlite3



class DbManager(object):
    
    def __init__(self):
        print('db created')
    
    def store_data(self, data):

        conn = sqlite3.connect('C:/sandbox/Euromillions/reviews.sqlite')
        
        
        conn.execute("INSERT INTO results_db (date, col1, col2, col3, col4, col5) VALUES " \
                  " (DATE('now'), ?,?,?,?,?) ", data)
        
        conn.commit()
        conn.close()
        
    def reset(self):
        conn = sqlite3.connect('C:/sandbox/Euromillions/reviews.sqlite')
        
        
        conn.execute("DELETE FROM results_db where col1 = 5")       
        
        
        conn.commit()
        conn.close()
        
test = DbManager()
test.reset()



#* * * * WED,SAT python /home/fabio/TensorFlow/Euromillions/Project/database.py  &>>/tmp/cron_debug_log.log
