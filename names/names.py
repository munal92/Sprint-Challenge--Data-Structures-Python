
import time
from binary_search_tree import BSTNode


start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)  # ~ 10 sec

bst = BSTNode("")
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)  # ~ 0.14  sec


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

f = open('names/names_1.txt', 'r')
n1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
n2 = f.read().split("\n")  # List containing 10000 names
f.close()
new_duplicate = []


# new_list = {1, 2, 3, 4, 3, 2}
# new_list2 = {1, 2}
new_list = set(n1)
new_list2 = set(n2)
new_duplicate = new_list.intersection(new_list2)


end_time = time.time()

# print(new_duplicate)
print(f"{len(new_duplicate)} duplicates:\n\n{', '.join(new_duplicate)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
