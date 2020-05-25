#!/usr/bin/env python3
# Kaushik Das
version_nbr = str(1.0)
import os, argparse, sys

def parseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--version', action='version',version=version_nbr)
  parser.add_argument('path', action='store', type=str, help='File or directory path/name')
  parser.add_argument('-l', '--line', action='store_true', required=False, help='If present, return the line count')
  parser.add_argument('-w', '--word', action='store_true', required=False, help='If present, return the word count') 
  parser.add_argument('-c', '--char', action='store_true', required=False, help='If present, return the character count') 
  args = parser.parse_args() 
  return (os.path.join(os.getcwd(), args.path), args.line, args.word, args.char)

def validatePath(path):

  if not os.path.exists(path):
    print("\n[ERROR] Invalid file/directory {0}, it does not exist\n".format(path))
    sys.exit(1)
  elif os.path.isdir(path):
    flist = os.listdir(path)
    if len(flist) == 0:
      print("\n[INFO] {0} is empty\n".format(path))
      sys.exit(0)
  elif os.path.isfile(path):
    print(f"File Path = {path}")
  else:
    print("\nInvalid file mode {0}\n".format(path))
    sys.exit(1)

def lineWordCharCountPrint(fname, lc, wc, cc, line, word, char):
  print(f" {fname}")
  if line:
    print("\tline count = {0}".format(lc))
  if word:
    print("\tword count = {0}".format(wc))
  if char:
    print("\tchar count = {0}".format(cc))


def lineWordCharCountFile(fname):
  lc = 0
  wc = 0
  cc = 0
  words_in = open(fname, "rb")
  for line in words_in.readlines():
    lc += 1
    wlist = line.split()
    for word in wlist:
      wc += 1
      cc += len(word)
  words_in.close() 

  return (lc, wc, cc)

def lineWordCharCountDir(path, line, word, char):
  for root_dir, subdirs, files in os.walk(path):
    for f in files:
      lc, wc, cc = lineWordCharCountFile(os.path.join(root_dir, f))
      lineWordCharCountPrint(os.path.join(root_dir, f), lc, wc, cc, line, word, char)
    for d in subdirs:
      dir_list = os.listdir(os.path.join(root_dir, d)) 

def lineWordCharCount(path, line, word, char):

  if os.path.isdir(os.path.join( os.getcwd(), path)):
    lineWordCharCountDir(path, line, word, char)
  else:
    lc, wc, cc = lineWordCharCountFile(path)
    lineWordCharCountPrint(path, lc, wc, cc, line, word, char)

def main():

  path, line, word, char = parseArgs()
  if line == False and word == False and char == False:
    line = word = char = True

  validatePath(path)
  lineWordCharCount(path, line, word, char)

if __name__ == "__main__":
  main()