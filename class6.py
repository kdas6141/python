#!/usr/bin/env python3
# Kaushik Das
import time
import sys
import argparse

version_nbr = str(1.1)
def print_current_time():
	print ("Hello current local time is {0}".format(time.ctime()))

def print_sys_functions():
	print ("sys.version : ", sys.version)
	print ("sys executable : ", sys.executable)
	print ("OS/host platform : ", sys.platform)
	print ("Path : ", sys.path)

def sum(base, a, b):
	if base not in {2, 8, 10, 16}:
		print(f"[ERROR Invalid base value {base}\n Valid options are 2, 8, 10, 16")
	if base == 2:
		return a+b
	if base == 8:
		return a+b

#print_sys_functions()
#print_current_time()
#time.sleep(1)
#print_current_time()

#sys.stdin = open('c:\PythonClass2\words.list', 'r')
#sys.stdin = open('words.txt', 'w')
#sys.stdin = open('words.error', 'w')

#for line in sys.stdin:
#	if len((line.split()) != 1):
#		sys.stderr.write("Invalid line. Expected only one word, got **"+ line[:-1] + "**\n")
#	else:
#		sys.stdout.write(line.title())

parser=argparse.ArgumentParser(description='Adds 2 integers in decimal, binary, octal or hex base', prog=)
parser.add_argument('-v', '--version', action='version', version=version_nbr)
parser.add_argument('int1', help='addend one', type=int, action='store')
parser.add_argument('int2', help='addend two', type=int, action='store')
parser.add_argument('-S', '--Stars', action='store_true', required=False, help='If present, it adds ****s to the output')
parser.add_argument('-b', '--base', action='store', type=int, required=False, help='Default base is 10. Specify 2,8, or 16', default=10)

args = parser.parse_args()
base = args.base
arg1 = args.int1
arg2 = args.int2
sum = arg1 + arg2
print("int1: ", )
print(f"sum of {arg1} and {arg2} is {sum}")

if args.Stars:
	print("Sum of {} and {} in base {} is {:*^12}".format(arg1, arg2, base, sum(base, arg1, arg2)))
else:
	print("Sum of {} and {} in base {} is {}".format(arg1, arg2, base, sum(base, arg1, arg2)))
#words_in = open('words.list', 'rt')
#words_out = open('words.txt', 'wt')
#words_err = open('words.error', 'wt')
#for line in sys.stdin:
#	print("line:", line)
#	if len((line.split()) != 1):
#		sys.stderr.write("Invalid line. Expected only one word, got **"+ line[:-1] + "**\n")
#	else:
#		sys.stdout.write(line.title())

#words_in.close()
#words_out.close()
#words_err.close()
