# -*- coding: utf-8 -*-
#
#   SQLite3 Testing
#
#A comment by Jared: Took a quick glance at the work.  looks good.  Maybe we should make a class database and add functions so that: database.close or database.insert_values() will work
def test_function(nothing):
    return 1

#connect to database
def connect(sqlite_file):
    import sqlite3
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return [c, conn]

#save and close database connection
def commit_close(conn):
    #save db
    conn.commit()
    
    #close db
    conn.close()
    print 'Database saved & closed.'
    print ''

#closes the connection without saving
def close(conn):
    conn.close()
    print 'Databse closed.'
    print ''

#save database but keep SQL connection open
def commit(conn):
    conn.commit()

#for cleaning variable inputs before passing them to the SQL server
def clean_input(input_var):
    return ''.join(char for char in input_var if char.isalnum())

def create_pk_table(c, table_name, col_name, field_type):
    # create table with primary key
    # field_type i.e. TEXT, INT, etc.
    
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
            .format(tn=table_name, nf=col_name, ft=field_type))
    print "Table %s created with a primary key column named: %s" % (table_name, col_name)

def add_column(c, table_name, col_name, col_type):
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
            .format(tn=table_name, cn=col_name, ct=col_type))
    print "Column %s added!" % (col_name)

def insert_values(c, table_name, values_list):
    c.executemany('''INSERT INTO {tn} VALUES (?,?,?,?)'''.format(tn=table_name), values_list)    

def search_multiple_rows(c, table_name, col_name, value):
    c.execute("SELECT * FROM {tn} WHERE {idf}=?".\
            format(tn=table_name, idf=col_name), (value,))
    all_rows = c.fetchall()
    return all_rows

# Returns a random alphanumeric string of length 'length'
def random_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.lowercase + string.uppercase + string.digits)
    return key

def makeMatrix(filename):
    import xlrd
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_index(0)
    matrix = dict((row,list(worksheet.row_values(row))) for row in range(worksheet.nrows))
    return matrix
