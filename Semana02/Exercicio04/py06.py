from pickle import TRUE, FALSE

if True:
    print('CONdicional was true')
    
if False:
    print('CONdicional was not true')
    
language = 'Python'
language2 = 'Java'

if language == 'Python':
    print('Conditional was True')
    
if language2 == 'Python':
    print('Language is Python')
else:
    print('No match')
    
if language2 == 'Python':
    print('Language is Python')
elif language2 == 'Java':
    print('Language is Java')
elif language2 == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('PLease Log In')
else:
    print('Welcome')
    
a = [1,2,3]
b = [1,2,3]

print (a==b)
print(a is b)
print(id(a))
print(id(b))
    
a = b
print(a is b)

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')