#coding: utf-8

import hashlib
import os
import glob
import sys

latest_folder = None
for name in os.listdir("."):
	if os.path.isdir(name):
		if latest_folder is None:
			latest_folder = name
		elif latest_folder < name:
			latest_folder = name
			
print("Latest folder: {}".format(latest_folder))

error_level = os.system("\"C:/Program Files/WinRAR/WinRAR.exe\" a {}.rar {} -ibck".format(latest_folder, latest_folder))
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
f_md5.write("md5: {}\r\n".format(md5_hex))
f_md5.close()

os.system("pause")