from SQLmodules import *

sqlite_file = 'buildingLinks.sqlite'    
x = dbo(sqlite_file)
print type(x)
x.dbo.c