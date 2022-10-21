student = {'name': 'Jhon', 'age': 25, 'courses': ['Math', 'CompSci']}

#student['phone'] = '555-5555'
#student['name'] = 'Jane'
#student.update({'name': 'Jane', 'age': 26, 'phone': '555-6666'})
#print(student.get('phone', 'Not Found'))

#del student['age']
age = student.pop('age')

print(student)
print(age)

print(len(student))
print(student.keys())
print(student.items())

for key in student:
    print(key)
    
for key, value in student.items():
    print(key,value)