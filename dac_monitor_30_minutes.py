# -*- coding: utf-8 -*-

__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

import os, glob, sys, cx_Oracle

# Monitor a ser executado a partir das 21:00 verificando a cada 30 min se o Status <> Completed or Running
# se retornar algum registro significa que deu erro na execução do DAC
SQL = ''' 
SELECT
  name,etl_defn_name,
  to_char(start_ts,'DD/MM/YYYY HH24:MI:SS'),
  to_char(end_ts,'DD/MM/YYYY HH24:MI:SS'),
  status,status_desc
FROM
  w_etl_defn_run
WHERE
  start_ts between sysdate-1 and sysdate and
  upper(status) NOT IN ('RUNNING', 'COMPLETED') and
  rownum = 1
'''

#connection with Oracle DB
print "Realizando conexao com o Banco de Dados..."
connstr = 'dacrep/bi#DACprdREP@sfapx13-scan.brasiltelecom.com.br:1549/dacprd'
connection = cx_Oracle.connect(connstr)

#if DB connection is successful
if connection:
    print "Conexao realizada com sucesso..."
#otherwise inform the user that there is something wrong with the DB connection
else:
    print "erro na conexao ao banco de dados"

cursor = connection.cursor()

for row in cursor.execute(SQL):
    # se row contiver algum registro...informa que deu erro de execução no DAC
    if row: # if row == True
      print "Erro na execucao do DAC"
      print row

#close cursor
cursor.close()
#close DB connection
connection.close()

print "FIM"
