# Author: Andre Almar - andre@y7mail.com

import os

os.system('tar -xvf jdk-8u121-linux-x64.tar')
os.system('mv jdk1.8.0_121 /webtools/oracle/jdk/jdk1.8.0_101_WLS')
os.system('ln -s /webtools/oracle/jdk/jdk1.8.0_101_WLS /webtools/oracle/plat1200/java')
