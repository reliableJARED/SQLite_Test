# -*- coding: utf-8 -*-
#
#   SQLite3 Testing
#
#A comment by Jared: Took a quick glance at the work.  looks good.  
#Maybe we should make a class database and add functions so that: database.close or database.insert_values() 
#will work

#one issue is that there is no error handle.  I ran main_workflow.py but didnt have text.xls
#so I got an error, put test.xls in the folder and ran again but got error
#running create_pk_table because table already existed
import sqlite3
#create dbo (database object) class
class dbo:
    def __init__(self,sqlite_file):
         self.conn = sqlite3.connect(sqlite_file)
         print "connected to DB"

         
    def c(self):
        return self.cursor()
        print "created cursor instance"
        
