import os
import glob
import sys
import cx_Oracle


row_id = raw_input("Enter ROW_ID: ")
row_id = str(row_id)

SQL = ''' 

SELECT 
      FILE_REV_NUM
   FROM 
       SIEBEL.S_ACCNT_ATT
   WHERE
      (row_id = '%s')
''' % (row_id)

#connection with Oracle DB
print "Connecting with the Database..."
connstr = 'USERNAME/PASSWORD@HOST:PORT/SERVICENAME'
connection = cx_Oracle.connect(connstr)

if connection:
    print "Database connection SUCESS..."
else:
    print "Database connection ERROR"

cursor = connection.cursor()

for row in cursor.execute(SQL):
    print "FILE_REV_NUMBER: %s" % row

cursor.close()
connection.close()


print "Searching for .SAF file"

for filename in glob.glob('\\\\NETWORK-PATH\\*\\S_ACCNT_ATT_%s_%s.SAF' % (row_id, row[0])):
    print "FILE FOUND: \t", filename.split('\\')[-1]
    arquivo = filename.split('\\')[-1]
    arquivo = str(arquivo)
    #split the filepath
    Dir = filename.split('\\')[-2]
    print "FOLDER FOUND: %s" % Dir
    print "copying files..."


source = "\\\\NETWORK-PATH-ORIGIN\\%s\\%s" % (Dir, arquivo)
target = "\\\\NETWORK-PATH-DESTINATION\\%s" % (Dir)

output = os.system ("""xcopy "%s" "%s" """ % (source, target))

print "ATTACHMENTS RESTORED!!!"
