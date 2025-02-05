# built in class - str

msg_of_day = 'Good morning to all'
print(type(msg_of_day))

# indexing
print(msg_of_day[0])
print(msg_of_day[2])
print(msg_of_day[-1]) # last
print(msg_of_day[-3]) # third last

# slicing
print(msg_of_day[0:4]) # 0 to 3
print(msg_of_day[:4]) # 0 to 3
print(msg_of_day[5:]) # 5 to end
print(msg_of_day[-6:]) # last 6 characters

print(len(msg_of_day)) # 19

# looping
for v in msg_of_day:
  print(v)

u = msg_of_day.upper()
print(u)

print(msg_of_day.capitalize())
print(msg_of_day.startswith('Good'))
print(msg_of_day.endswith('night'))

print(msg_of_day.replace('morning', 'evening'))

t = 'hello to all. hello everybody'
print(t.count('hello'))

user_input = '45'
print(user_input.isnumeric())

user_input = 'good'
print(user_input.isnumeric())
print(user_input.isalpha())

print(msg_of_day.find('night'))
print(msg_of_day.find('morning'))