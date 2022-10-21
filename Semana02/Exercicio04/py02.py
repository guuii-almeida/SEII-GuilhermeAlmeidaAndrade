from _hashlib import new


message_one =  'HELLO WORLD'
print (message_one)
message_two = "Bobby's World"
print(message_two)
message_three = """Bob was a very 
famous character in 90s"""
print(message_three)

print(len(message_one))
print(message_one[0])

print(message_one[0:5])
print(message_one[:5])
print(message_one[6:])

print(message_one.lower())
print(message_one.upper())
print(message_one.count('HELLO'))
print(message_one.find('W'))
new_message = message_one.replace('WORLD', 'Universe')
print(new_message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name
message = '{}, {}. Welcome!'.format(greeting, name)
#message = f'{greeting}, {name.upper()}.Welcome!'
print(message)

print(dir(name))
print(help(str))
print(help(str.lower))

