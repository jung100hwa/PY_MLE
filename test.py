alist = [1,2,3,3,3]

print(alist.index(3))
alist[alist.index(3)] = 5

# alist = [6 if x == 3 else x for x in alist]
alist[alist == 3] = 6
print(alist)