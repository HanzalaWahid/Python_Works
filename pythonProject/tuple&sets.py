# t = ( 8 , 78 , 98 , 23 , 45 )
# print(t)

a1 = {23, 32, 52, 57, 34, 78, 4, 3, 3}
a2 = {4, 54, 43, 32, 87, 98, 23, 5, 6, 3, 6}
print(a1.pop())
print(a2.clear())
print(a2.union(a1))
print(a1.difference(a2))
(a1.add(39))
print(a1)
(a2.discard(a1))
print(a1)
(a2.update({32, 22, 223, 322, 32}))
print(a2)
print(a1.isdisjoint(a2))
