#coding: utf-8

import hashlib
import os
import glob
import sys
import datetime

latest_folder = None
for name in os.listdir("."):
	if os.path.isdir(name):
		if latest_folder is None:
			latest_folder = name
		elif os.path.getmtime(latest_folder) < os.path.getmtime(name):
			latest_folder = name
			
print("Latest folder: {}    [{}]".format(latest_folder, datetime.datetime.fromtimestamp(os.path.getmtime(latest_folder))))

os.system("del {}.rar".format(latest_folder))
os.system("timeout 3")
error_level = os.system("\"C:/Programs/WinRAR/WinRAR.exe\" a -ma4 -md4 -m3 {}.rar {}\\* -ibck -r -ep1".format(latest_folder, latest_folder))
if error_level is None or error_level != 0:
	print("Fail compress files: {}".format(error_level))
	os.system("pause")
	exit(1)
print("rar: {}.rar".format(latest_folder))

f = open('{}.rar'.format(latest_folder), "rb")
md5_hex = hashlib.md5(f.read()).hexdigest()
f.close()
print("md5: {}".format(md5_hex))

f_md5 = open('{}_md5.txt'.format(latest_folder), 'wb')
f_md5.write("md5: {}\r\n".format(md5_hex).encode())
f_md5.close()

os.system("pause")