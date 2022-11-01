#Exemplo 1
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 2
import multiprocessing
import time

start = time.perf_counter()
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 3
import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 4
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 5
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 6
import concurrent.futures
from locale import currency
import time

start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
# for process in processes:
#     process.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

#Exemplo 7
import concurrent.futures
from locale import currency
import time
start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
# for process in processes:
#     process.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')