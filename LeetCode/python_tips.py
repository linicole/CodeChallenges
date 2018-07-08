# Data Structures
# https://docs.python.org/3/tutorial/datastructures.html

# 1. List
# (1) Difference of lst.append(), lst.extend(), lst.insert() and lst+lst
# append: add an item to the end of the list = (a[len(a):]=[x])
# extend: extend the list by appending all the items from the iterable = (a[len(a):]=iterable)
# insert: insert an item at a given position --> lst.insert(0, x)
# lst+lst: same effect as append, but need to assign to a new object
mylst = ['a', 'b', 'list', 'z', 'example']
mylst.append("new")  # ['a', 'b', 'list', 'z', 'example', 'new']
mylst.extend("new")  # ['a', 'b', 'list', 'z', 'example', 'n', 'e', 'w']
mylst.extend(["new"])  # ['a', 'b', 'list', 'z', 'example', 'new']
mylst.insert(2, "new")  # ['a', 'b', 'new', 'list', 'z', 'example']
mylst_new = mylst + ["new"]  # ['a', 'b', 'list', 'z', 'example', 'new'] --> a new list # others will mutate the original list

# (2) remove, pop, clear, del
# remote: remove the 1st item from the list whose value is x. (x must be in the list)
# pop(i): remove the item at the given position and return it. If no i, remove & return the last item.
# clear: remove all items from the list
mylst = ['a', 'b', 'list', 'a', 'z', 'b', 'example']
mylst.remove('b')  # ['a', 'list', 'a', 'z', 'b', 'example']
mylst.pop(2)  # 'list'; ['a', 'b', 'a', 'z', 'b', 'example']
mylst.pop()  # ['a', 'b', 'list', 'a', 'z', 'b']
mylst.clear()
del mylst[2]  # ['a', 'b', 'a', 'z', 'b', 'example']
del mylst[2:4]  # ['a', 'b', 'z', 'b', 'example']
del mylst[:]  # [] --> same as mylst.clear()
# To remove all the specific item from a list:
list(filter(lambda a: a != 'a', mylst))  # ['b', 'z', 'b', 'example'] --> assign a new list
[i for i in mylst if i != 'a']  # ['b', 'z', 'b', 'example']
# To remove multiple items from a list
[i for i in mylst if i not in ['a', 'b']]  # ['z', 'example']

# (3) index
# index: return zero-based index in the list of the 1st item whose value is x
mylst = ['a', 'b', 'list', 'a', 'z', 'b', 'example']
mylst.index('a')  # 0
# to get all the occurrences of an item
[i for i, j in enumerate(mylst) if j == 'a']  # [0, 3]

# (4) count
# count: returns the number of times X appears in the list
mylst = ['a', 'b', 'list', 'a', 'z', 'b', 'example']
mylst.count('a')  # 2

# (5) Difference between lst.sort(reverse=False) and sorted(lst)
# lst.sort(): sorts the list mutating on the original list [in-place operation, faster]
# sorted(lst): returns a new sorted list. Works on any iterable (lists, strings, tuples, dicts, generators...)
mylst = ['a', 'b', 'list', 'a', 'z', 'b', 'example']
mylst.sort()  # ['a', 'a', 'b', 'b', 'example', 'list', 'z']
sorted(mylst)  # ['a', 'a', 'b', 'b', 'example', 'list', 'z']

mylstlst = [['a', 'b'], ['c','b'], ['b', 'd']]
sorted(mylstlst)  # [['a', 'b'], ['b', 'd'], ['c', 'b']]

# (6) reverse
mylstlst = [['a', 'b'], ['c','b'], ['b', 'd']]
mylstlst.reverse()  # [['b', 'd'], ['c', 'b'], ['a', 'b']]

# (7) How to copy a list
old_lst = ['a', 'b', 'c']
# new_lst = old_lst: don't actually have 2 lists - they're referring to the same list
old_lst = ['a', 'b', 'c']
new_lst = old_lst
old_lst[1] = 'd'  # new_lst = ['a', 'd', 'c']
# (a) slice: old_lst[:] --> affect as copy()
new_lst = old_lst[:]
# (b) list(): list(old_lst) --> affect as copy() --> faster
new_lst = list(old_lst)
# (c) copy.copy()
import copy
new_lst = copy.copy(old_lst)
# (d) copy.deepcopy() --> slowest
new_lst = copy.deepcopy(old_lst)
# More demonstration with id()
# id():  the identity of the location of the object in memory...
import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
# (a) assignment
d = c
print(id(d) == id(c))  # True
print(id(d[0]) == id(c[0]))  # True
# (b) copy
d = copy.copy(c)
print(id(d) == id(c))  # False
print(id(d[0]) == id(c[0]))  # True
# (c) deepcopy
d = copy.deepcopy(c)
print(id(d) == id(c))  # False
print(id(d[0]) == id(c[0]))  # False

# (8) List Comprehensions
xlst = range(10)  # [0,1,2,3,4,5,6,7,8,9] = range(0,10)
xsquare = [x**2 for x in xlst]
xsquare = list(map(lambda x: x**2, xlst))
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# flatten a list using a list-comp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]





# 2. Tuple & Sequence




# 3. Set




# 4. Dictionary




# 5. Looping





# 6. Operator
# (1) *: unpacks the sequence/collection into positional arguments
#        or used in function arguments
def sum(a, b): return a+b
values = (1, 2)
sum(*values)

def foo(*args):
    for a in args:
        print(a)
foo(1, 2, 3)

# (2) **: same as *, only using a dict
values = {'a':1, 'b':2}
sum(**values)



