# -*- coding: utf-8 -*-
__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar

usage: fab -R server_name function_name

e.g: fab -R sfapx09a kill_processes
"""

from fabric.api import *

prompt_pid = 'Digite o(s) numero(s) do pid(s) >> '

env.roledefs = {
    'sfapx09a': ['sfapx09a'],
    'sfapx09b': ['sfapx09b'],
    'sfapx10a': ['sfapx10a'],
    'sfapx10b': ['sfapx10b']
}

env.user = 'user_name'
env.key_filename = 'C:\\Users\\tr546391.OI\\Desktop\\andre_backup\\putty\\.ssh_crmadmin\\.ssh\\crmadmin.ppk'


def opmn_status_SFAPX09A():
	run('/oraclebi/MiddlewareHome/instances/instance1/bin/opmnctl status')


def opmn_status_SFAPX09B():
	run('/oraclebi/MiddlewareHome/instances/instance2/bin/opmnctl status')


def opmn_status_SFAPX10A():
	run('/oraclebi/MiddlewareHome/instances/instance3/bin/opmnctl status')


def opmn_status_SFAPX10B():
	run('/oraclebi/MiddlewareHome/instances/instance4/bin/opmnctl status')


def check_ports():
	run('netstat -anp|grep :7001[[:blank:]]') #check if port 7001 is still in use


def check_processes():
	run('ps -e -f | grep oraclebi') #check if processes are running


def kill_processes():
    pid = raw_input(prompt_pid)
    run('kill -9 {}'.format(pid)) #check if processes are running
