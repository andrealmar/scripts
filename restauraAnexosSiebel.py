__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

import os
import glob
import sys
import cx_Oracle


row_id = raw_input("Digite o ROW_ID: ")
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
print "Realizando conexao com o Banco de Dados..."
connstr = 'USERNAME/PASSWORD@HOST:PORT/SERVICENAME'
connection = cx_Oracle.connect(connstr)

if connection:
    print "Conexao realizada com sucesso..."
else:
    print "erro na conexao ao banco de dados"

cursor = connection.cursor()

for row in cursor.execute(SQL):
    print "FILE_REV_NUMBER: %s" % row

cursor.close()
connection.close()


print "Procurando arquivo .SAF"

for filename in glob.glob('\\\\DIGITE-O-PATH-DA-REDE\\*\\S_ACCNT_ATT_%s_%s.SAF' % (row_id, row[0])):
    print "ARQUIVO ENCONTRADO: \t", filename.split('\\')[-1]
    arquivo = filename.split('\\')[-1]
    arquivo = str(arquivo)
    #split the filepath
    Dir = filename.split('\\')[-2]
    print "DIRETORIO ENCONTRADO: %s" % Dir
    print "copiando arquivos..."


source = "\\\\NETWORK-PATH-ORIGEM\\%s\\%s" % (Dir, arquivo)
target = "\\\\NETWORK-PATH-DESTINO\\%s" % (Dir)

output = os.system ("""xcopy "%s" "%s" """ % (source, target))

print "ANEXOS RESTAURADOS!!!"
