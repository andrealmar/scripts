__author__ = 'andrealmar'

"""
ANDRE ALMEIDA ARAUJO - github.com/andrealmar
"""

import os, shutil, stat, errno
from subprocess import Popen

# directory path
dirpath = 'E:\sea78\siebsrvr\LOGARCHIVE'

# if ACCESS_DENIED exception is raised, it will work on that
def readonly_handler(func, path, execinfo): 
    os.chmod(path, 128) #or os.chmod(path, stat.S_IWRITE) from "stat" module
    func(path)

print("EXCLUINDO os arquivos da pasta LOGARCHIVE...")
	
#search for files in directory, deletes it including folders and its sub-folders
for filename in os.listdir(dirpath):
	filepath = os.path.join(dirpath, filename)
	try:
		shutil.rmtree(filepath, ignore_errors=False, onerror=readonly_handler)
	except OSError:
		os.remove(filepath)

print("EXCLUINDO os arquivos da pasta LOG...")
p = Popen("remove_LOG_files.bat", cwd=r"E:/sea78/scripts")
stdout, stderr = p.communicate()
