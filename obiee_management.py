# -*- coding: utf-8 -*-
from fabric.api import *

__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

env.hosts = ['sfapx09a', 'sfapx09b', 'sfapx10a', 'sfapx10b']
env.user = 'crmadmin'
env.key_filename = 'C:\\Users\\tr546391.OI\\Desktop\\andre_backup\\putty\\.ssh_crmadmin\\.ssh\\crmadmin.ppk'


def opmn_status():
    run('/oraclebi/MiddlewareHome/instances/instance2/bin/opmnctl status')


def check_ports():
	run('netstat -anp|grep :7001[[:blank:]]') #check if port 7001 is still in use


def check_processes():
	run('ps -e -f | grep oraclebi') #check if processes are running
