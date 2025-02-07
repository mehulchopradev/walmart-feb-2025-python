from math import pi

msg = 'good morning' # str object
print(type(msg))

# function object
# a variable which is the name of the function is assigned to the function object
# and is created when the function is defined in the file scope
def area_of_circle(radius):
  return pi * (radius ** 2)

print(type(area_of_circle))
# functions are first class objects in python

# msg is a variable -- non callable variable
# area_of_circle is a variable --- callable variable
print(area_of_circle(radius=5))
# print(msg()) # error

# Functional programming
# in python a function can be defined inside another function
def abc(i):
  # i (int) -> abc
  j = 10 # j (int) -> abc

  # xyz (function) -> abc
  def xyz():
    k = 20 # k (int) -> xyz
    return i + j + k # inner function can access the enclosing function variables
  
  l = xyz()
  return l ** 2

print(abc(i=4))

# a function returning another function
def mno(a): # a (int) -> mno
  b = 10 # b (int) -> mno

  # pqr (function) -> mno
  def pqr():
    c = 20 # c (int) -> pqr
    # inner function remembers the context of the enclosing function 
    # even after the enclosing function has finished returning
    # Closures
    return (c + b) ** a
  
  return pqr

f = mno(a=2) # f (function) -> entire file
print(f())

# passing a function as an argument to another function -- Callback functions
# fn1 (function) -> entire file
def fn1(fn): # fn (function) -> fn1
  i = 10 # i (int) -> fn1
  j = fn(i)
  return i + j

# fn2 (function) -> entire file
def fn2(x):
  # x (int) -> fn2
  y = 5 # y (int) -> fn2
  return (x + y) ** 2

print(fn1(fn2))