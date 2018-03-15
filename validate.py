# Author: Andre Almar - andre@y7mail.com

import os, subprocess
from subprocess import call

print 'Validando FileSystem /webaplic'
if os.path.isdir('/webaplic'):
    print "Diretorio /webaplic ja existe"
else:
    try:
        os.makedirs('/webaplic')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Validando FileSystem /webtools'
if os.path.isdir('/webtools'):
    print "Diretorio /webtools ja existe"
else:
    try:
        os.makedirs('/webtools')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Validando FileSystem //webtools/oracle'
if os.path.isdir('/webtools/oracle'):
    print "Diretorio /webtools/oracle ja existe"
else:
    try:
        os.makedirs('/webtools/oracle')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Validando FileSystem /webtools/oracle/jdk'
if os.path.isdir('/webtools/oracle/jdk'):
    print "Diretorio /webtools/oracle/jdk ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/jdk')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Validando FileSystem /webtools/oracle/plat1200'
if os.path.isdir('/webtools/oracle/plat1200'):
    print "Diretorio /webtools/oracle/plat1200 ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Validando FileSystem /webtools/oracle/plat1200/filestores'
if os.path.isdir('/webtools/oracle/plat1200/filestores'):
    print "Diretorio /webtools/oracle/plat1200/filestores ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/filestores')
    except OSError:
        if not os.path.isdir(path):
            raise


print 'Validando FileSystem /webtools/oracle/plat1200/logs'
if os.path.isdir('/webtools/oracle/plat1200/logs'):
    print "Diretorio /webtools/oracle/plat1200/logs ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/logs')
    except OSError:
        if not os.path.isdir(path):
            raise


print 'Validando FileSystem /webtools/oracle/plat1200/middleware'
if os.path.isdir('/webtools/oracle/plat1200/middleware'):
    print "Diretorio /webtools/oracle/plat1200/middleware ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/middleware')
    except OSError:
        if not os.path.isdir(path):
            raise


print 'Validando FileSystem /webtools/oracle/domains/plat1200'
print os.path.isdir('/webtools/oracle/domains/plat1200')

print '\n ########## VALIDANDO CRONTAB ########## \n'
call(["crontab", "-e"])

print '\n ########## VERIFICANDO VALORES DE OPEN FILES ########## \n'
os.system("cat /etc/security/limits.conf | grep beaadmin")

print '\n ########## VERIFICANDO VALORES DO KERNEL ########## \n'
os.system('cat /etc/sysctl.conf')

print '\n ########## VERIFICANDO kernel.shmmax ##########'
shmmax = subprocess.Popen(['cat', '/proc/sys/kernel/shmmax'], stdout=subprocess.PIPE).communicate()[0]
print shmmax

print '\n ########## VERIFICANDO TOTAL DE MEMORIA RAM (GB)##########'

p1 = subprocess.Popen(["free", "-g"], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
p2 = subprocess.Popen(["awk", "/Mem:/ { print $2 }"], stdin=p1.stdout, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
out, err = p2.communicate()
print 'TOTAL DE MEMORIA RAM (GB): ' + out

print '\n ########## CALCULO (kernel.shmmax / 1073741824) ##########'

total = int(shmmax) / 1073741824
print total

print '########## CRIANDO PASTAS ADICIONAIS ##########'

print 'Criando pasta /webtools/oracle/plat1200/install'
if os.path.isdir('/webtools/oracle/plat1200/install'):
    print "Diretorio /webtools/oracle/plat1200/install ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/install')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Criando pasta /webtools/oracle/plat1200/bin'
if os.path.isdir('/webtools/oracle/plat1200/bin'):
    print "Diretorio /webtools/oracle/plat1200/bin ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/bin')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Criando pasta /webtools/oracle/filestores/FileStore'
if os.path.isdir('/webtools/oracle/plat1200/filestores/FileStore'):
    print "Diretorio /webtools/oracle/plat1200/filestores/FileStore ja existe"
else:
    try:
        os.makedirs('/webtools/oracle/plat1200/filestores/FileStore')
    except OSError:
        if not os.path.isdir(path):
            raise

print 'Criando pasta /webaplic/backup'
if os.path.isdir('/webaplic/backup'):
    print "Diretorio /webaplic/backup ja existe"
else:
    try:
        os.makedirs('/webaplic/backup')
    except OSError:
        if not os.path.isdir(path):
            raise


print '########## REMOVENDO DIRETORIO /webtools/oracle/plat1200/middleware/lost+found ##########'

os.rmdir('/webtools/oracle/plat1200/middleware/lost+found/')
