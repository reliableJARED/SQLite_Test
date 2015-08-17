#import the SQL modules file
from SQLmodules import *

sqlite_file = 'buildingLinks.sqlite'    
c, conn = connect(sqlite_file)

# create table (complete with PRIMARY KEY as 'id')
# make some columns for the table besides the unique id
create_pk_table(c, 'building_links', 'id', 'TEXT')
add_column(c, 'building_links', 'nickname', 'TEXT')
add_column(c, 'building_links', 'display_address', 'TEXT')
add_column(c, 'building_links', 'url', 'TEXT')

# reads excel file and makes a table matrix in memory
matrix = makeMatrix('test.xls')

#define starting unique id
unique_id = 1

# iterates over the rows of the execel table and inserts the
# data into the databse
for row in matrix:

    #assign values to vars
    nickname =  matrix[row][0].lower()
    dispAddress = matrix[row][1].lower()
    url = matrix[row][6].lower()

    #package data and insert values into database
    info = [(unique_id, nickname, dispAddress, url),]
    insert_values(c, 'building_links', info)

    #save database
    commit(conn)

    #updates unique id
    unique_id += 1

#saves and closes the database
commit_close(conn)

# Connecting to the database file once again to see if changes are saved
c, conn = connect(sqlite_file)

#searches the 'nickname' column for 'the bristol' and returns all results
search_results = search_multiple_rows(c, 'building_links', 'nickname', 'the bristol')


#and finally, two queries to see if the info was stored in the database
print "Searching the nickname column for 'the bristol'..."
for result in search_results:
    unique_id = result[0]
    nickname = result[1]
    display_address = result[2]
    url = result[3]

    print '-->', display_address
    print ''

#searches the 'nickname' column for '320 east' and returns all results
search_results = search_multiple_rows(c, 'building_links', 'url', 'http://streeteasy.com/building/the-envoy')

print "Searching the url column for 'http://streeteasy.com/building/the-envoy'..."
for result in search_results:
    unique_id = result[0]
    nickname = result[1]
    display_address = result[2]
    url = result[3]

    print '-->', display_address

#close database
close(conn)
