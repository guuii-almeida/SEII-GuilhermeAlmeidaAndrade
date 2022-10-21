def hello_func():
    print('HELLO FUNC!')

print(hello_func())
print(hello_func())
print(hello_func())
print(hello_func())

def hello_world():
    return'Hello World.'

print(hello_world())

#print(len('Test'))

def hello_function(greeting, name = 'You'):
    return '{}, {}'.format(greeting,name)

print(hello_function('Hi',name='Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Maths', 'Art', name='Jhon', age=22)

courses = ['Math', 'Art']
info = {'name': 'Jhon', 'age': 22}

student_info(*courses,**info)

month_days = [1,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year %100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 2))
