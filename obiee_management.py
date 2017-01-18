# -*- coding: utf-8 -*-
__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

from fabric.api import *

env.hosts = ['sfapx09a', 'sfapx09b', 'sfapx10a', 'sfapx10b']
env.user = 'crmadmin'
env.key_filename = 'C:\\Users\\tr546391.OI\\Desktop\\andre_backup\\putty\\.ssh_crmadmin\\.ssh\\crmadmin.ppk'

def opmn_status():
	if env.hosts[0] == 'sfapx09a':
		print env.hosts[0]
"""
		elif env.hosts[ 1] == 'sfapx09b':
		run('/oraclebi/MiddlewareHome/instances/instance2/bin/opmnctl status')
	elif env.hosts[2] == 'sfapx10a':
		run('/oraclebi/MiddlewareHome/instances/instance3/bin/opmnctl status')
	else:
		run('/oraclebi/MiddlewareHome/instances/instance4/bin/opmnctl status')
"""

def check_ports():
	run('netstat -anp|grep :7001[[:blank:]]') #check if port 7001 is still in use

def check_processes():
	run('ps -e -f | grep oraclebi') #check if processes are running
