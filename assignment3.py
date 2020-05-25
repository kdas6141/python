#!/usr/bin/env python3
# Kaushik Das

'''
 Input: a string
 Output: a string which is the same as the input string with all its non-alphanumeric characters removed
 Note: the given implementation below is not the most efficient, but it is OK for this assignment
'''
def remove_non_alphanumeric(s):
   alphanum_s =''
   for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' :
         alphanum_s += c
   return alphanum_s

def is_pal_no_loop_recur(s):

   return(s.lower() == s[::-1].lower())

def is_pal_loop(s):
   for i in range(len(s)//2): 
      if s[i].lower() != s[len(s)-1-i].lower():
         return False
   return True

def is_pal_recur(s):
   if len(s) == 1:
      return True;

   if s[:1:].lower() == s[-1:].lower():
      return True;

   return is_pal_recur(s[1:-1:])

# list of is_pal functions your are going to write
func_list = [is_pal_no_loop_recur, is_pal_loop, is_pal_recur]

phrase = ''
while phrase.title() != 'Exit' :
   # Prompt the user to enter a string/phrase
   phrase = input("Enter a phrase on a single line. To exit, enter [Exit/exit/EXIT]: ")
   if phrase.title() == 'Exit':
      print("Exiting the program ... Bye")
      exit(0)

   # Remove non-alphanumeric characters
   alphanum_phrase = remove_non_alphanumeric(phrase)
   if len(alphanum_phrase) == 0:
      print("The phrase you entered, did not have any alphanumeric characters in it...skipping it\n")
      continue

   for f in func_list:  #executes each is_pal function in the function list
      if f(alphanum_phrase):
         print("{}: Phrase '{}' is a palindrome".format(f.__name__, phrase))
      else:
         print("{}: Phrase '{}' is NOT a palindrome".format(f.__name__, phrase))