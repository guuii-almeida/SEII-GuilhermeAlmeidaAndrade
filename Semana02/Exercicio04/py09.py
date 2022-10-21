import random
import math
import datetime
import calendar
import os
#from my_module import find_index, test
from my_module import *
import sys

courses = ['History', 'Math', 'Physics','CompSci']

index = find_index(courses, 'Math')
#print(index)
#print(test)

#print(sys.path)
rads = math.radians(90)

print(math.sin(rads))

print(calendar.isleap(2017))
today = datetime.date.today()
print(today)

random_course = random.choice(courses)

print(random_course)

print(os.getcwd())
print(os.__file__)
