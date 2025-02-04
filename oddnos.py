# while loop
''' def odd_series(n):
  i = 1
  series = ''
  while i <= n:
    if i % 2:
      series += str(i) + ' '
    i += 1
  return series
'''

# for loop
'''
for i in <<sequence of elements>>:
  I1
  I2
  I3
'''
def odd_series(n):
  # sequence of element ---> [1, n]
  # range(1, n + 1)
  # range(1, n + 1, 2) ---> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  series = ''
  for i in range(1, n + 1):
    if i % 2:
      series += str(i) + ' '
  return series


n = int(input('Enter n: '))
print(odd_series(n=n))