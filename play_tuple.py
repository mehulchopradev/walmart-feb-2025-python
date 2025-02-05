s1 = ('mehul', 10, 'm', 90)
print(s1)
print(type(s1))

et = ()
print(type(et))

s2 = ('jane',) # single element tuple
print(type(s2))

# looping
for d in s1:
  print(d)

# indexing
print(s1[0])
print(s1[-2]) # 2nd last element

# slicing
s3 = s1[0:2]
print(s3)

# no modification
# s1[1] = 12 # error
# no pop, append, extend, remove, insert, clear, sort, reverse