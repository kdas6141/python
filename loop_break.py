#!/usr/bin/env python3
# Kaushik Das
# Version 0
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '

print("\nVersion:0")
if len(first_str) == len(second_str) :
   for char1 in first_str:
      for char2 in second_str:
         if char1 == char2 :
            print(f"Char {char1} is in both strings")

#
#Version 1
#
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '
print("\nVersion:1")

if len(first_str) == len(second_str) :
   for char1 in first_str:
      for char2 in second_str:
         if char1 == char2 :
            print(f"Char {char1} is in both strings")
            break

#
#Version 2
#
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '
print("\nVersion:2")

if len(first_str) == len(second_str) :
   for char1 in first_str:
      for char2 in second_str:
         if char1 == char2 :
            print(f"Char {char1} is in both strings")
         break

#
#Version 3
#
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '
print("\nVersion:3")

if len(first_str) == len(second_str) :
   for char1 in first_str:
      for char2 in second_str:
         if char1 == char2 :
            print(f"Char {char1} is in both strings")
      break

#
#Version 4
#
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '
print("\nVersion:4")

if len(first_str) == len(second_str) :
   for char1 in first_str:
      for char2 in second_str:
         if char1 == char2 :
            pass #print(f"Char {char1} is in both strings")
#   break
print('Compilation error for "break" outside scope')

#
#Version 5
#
first_str =  'Python*programming is fun'
second_str = 'How do*you like Python?  '

print("\nVersion:5")
if len(first_str) == len(second_str) :
   for char1 in first_str :
      for char2 in second_str :
         break
         if char1 == char2 :
            print(f"Char {char1} is in both strings")

