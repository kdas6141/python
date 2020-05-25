import os
import time
import pathlib
import platform

os_name = os.getenv('OS')
print(f"OS name is {os_name}")
go_dir = "C:\\GoClass"
cur_dir = os.getcwd()
print(f"current dir: {cur_dir}")
os.chdir(go_dir)
print(f"current dir: {os.getcwd()}")
os.chdir(cur_dir)
print(f"current dir: {os.getcwd()}")
print(f" "+str(os.listdir())) 
os.mkdir('ex1')
print(f" "+str(os.listdir())) 
os.rmdir('ex1')
print(f" "+str(os.listdir())) 

print("<<<<<<<<<<<<<<<<using listdir()>>>>>>>>>>>>>>>>>>>")
dir_list = os.listdir()
for dir_entry in dir_list:
	if os.path.isfile(dir_entry):
		print(f"{dir_entry} is a regular file")
		full_path_name = os.path.join(cur_dir, dir_entry)
		print(f" full-path name: {full_path_name}")
		print(f" os path: {cur_dir}")
		print(f" os stat: {os.stat(full_path_name)}")

print("<<<<<<<<<<<<<<<<using scandir()>>>>>>>>>>>>>>>>>>>")
dir_list = os.scandir()
print(f"List of files in directory: {cur_dir}:")
for dir_entry in dir_list:
	if os.path.isdir(dir_entry):
		print(f"{dir_entry}")

print("<<<<<<<<<<<<<<<<using walk()>>>>>>>>>>>>>>>>>>>")
for root_dir, sub_dirs, files in os.walk(cur_dir):
	for f in files:
		print(f"I am regular file: {os.path.join(root_dir, f)}")
	for d in sub_dirs:
		print(f"I am a directory: {os.path.join(root_dir, d)}")


cmd = 'dir ' + cur_dir
os.system(cmd)
plat_name = platform.platform()
print(plat_name)
print(platform.uname().system)
if plat_name.find("Windows") == -1:
	print("Not windows")
	print(platform.uname())
else:
	print("Windows OS")