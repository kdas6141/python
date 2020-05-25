#Do not change a list while iterating over it

#Example: Remove the list elements from list_1 that are also in list_2

#WRONG way: do not alter the list (list_1) while iterating over it
list_1 = [2, -10, 12, 24]
list_2 = [2, -10, 15, 43]
print(f"Original lists:\n  list_1 = {list_1}\n  list_2 = {list_2}\n")


for el in list_1:
   if el in list_2:
      list_1.remove(el)

print(f"Modified lists(incorrect):\n  list_1 = {list_1}\n  list_2 = {list_2}\n")

#RIGHT way: make a copy of list_1; iterate over the copy
list_1 = [2, -10, 12, 24]
list_2 = [2, -10, 15, 43]

copy_list_1 = list_1.copy()
for el1 in copy_list_1:
   if el1 in list_2:
      list_1.remove(el1)

print(f"Modified lists(correct):\n  list_1 = {list_1}\n  list_2 = {list_2}\n")