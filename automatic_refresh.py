# -*- coding: utf-8 -*-

__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

from selenium import webdriver
import time
import urllib
import urllib2

x = raw_input("Enter the URL")
refreshrate = raw_input("Enter the number of seconds")
refreshrate = int(refreshrate)
driver = webdriver.Firefox()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
