courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
courses.insert(0,'Chemistry')
courses_2 = ['Art', 'Education']
courses.insert(0,courses_2)
courses.extend(courses_2)

courses.remove('Art')
courses.pop()
courses.remove(courses_2)
popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
courses.sort()
print(courses)

nums = [1,5,2,4,3]
nums.sort()

nums.sort(reverse=True)
print(nums)

sorted_courses = sorted(courses)

print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))

print('Art' in courses)
print('Math' in courses)

for item in courses:
    print(item)
    
for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)
    
courses_str = ', '.join(courses)
new_list = courses_str.split(' - ')
print(courses_str)
print(new_list)   
 
#mutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
#empty list
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
# empty_Set = {} #this is wrong
empty_set = set()

#print('Math' in cs_courses)
