__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

import os
import glob
import sys
import cx_Oracle
import csv


#open the data.txt file and at the same time storing each item in a position of the list
lista_de_anexos = [line.rstrip() for line in open('data.txt')]

#connection with Oracle DB
print "Realizando conexao com o Banco de Dados..."
connstr = 'USERNAME/PASSWORD@HOST:PORT/SERVICE_NAME'
connection = cx_Oracle.connect(connstr)

#testing if the connection is successful
if connection:
    print "Conexao realizada com sucesso..."
else:
    print "erro na conexao ao banco de dados"

#declaring the cursor which will move through the records
cursor = connection.cursor()

for item in lista_de_anexos:
	file_name = item

	#SQL statement
	SQL = '''
		(SELECT ROW_ID, FILE_REV_NUM FROM SIEBEL.S_ACCNT_ATT WHERE FILE_NAME = '%s')
	''' % (file_name)

	#executing the SQL statement and retrieving the ROW_ID and FILE_REV_NUM of each Siebel attachment
	for i in cursor.execute(SQL):
		#i = str(i)
		list(i)
		print "NOME DO ANEXO: {0}".format(file_name)
		print "ROW_ID: {0}".format(i[0])
		print "FILE_REV_NUM: {0}".format(i[1])
		
		print "Procurando arquivo .SAF"
		
		#finding the .SAF file
		for filename in glob.glob('\\\\netprd00\\crmoifls_fsexp\\*\\S_ACCNT_ATT_%s_%s.SAF' % (i[0], i[1])):
			print "ARQUIVO ENCONTRADO: \t", filename.split('\\')[-1]
			arquivo = filename.split('\\')[-1]
			arquivo = str(arquivo)
			
			#splitting the filepath
			Dir = filename.split('\\')[-2]
			print "DIRETORIO ENCONTRADO: %s" % Dir
			print "copiando arquivos..."


			source = "\\\\netprd00\\crmoifls_fsexp\\%s\\%s" % (Dir, arquivo)
			target = "\\\\crmoifls.telemar\\siebfileprd\\%s" % (Dir)

			output = os.system ("""xcopy "%s" "%s" """ % (source, target))

		print "ANEXOS RESTAURADOS!!!"
		
#closing the DB cursor
cursor.close()
#closing the DB connection
connection.close()

