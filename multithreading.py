import time
import threading
from concurrent.futures import ThreadPoolExecutor

def func1(seconds):
    print(f'Waiting for {seconds} seconds')
    time.sleep(seconds)
    return f'waited for {seconds} seconds'

'''
# below is single threaded (no multithreading)
start = time.perf_counter()
func1(4)
func1(2)
func1(1)
print(time.perf_counter() - start)

# below is multi threaded (multithreading but will not wait for process to complete)
t1 = threading.Thread(target = func1, args = [4])
t2 = threading.Thread(target = func1, args = [2])
t3 = threading.Thread(target = func1, args = [1])

start = time.perf_counter()

t1.start()
t2.start()
t3.start()

print(time.perf_counter() - start)


# below is multi threaded (multithreading but will not wait for process to complete)
t1 = threading.Thread(target = func1, args = [4])
t2 = threading.Thread(target = func1, args = [2])
t3 = threading.Thread(target = func1, args = [1])

start = time.perf_counter()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(time.perf_counter() - start)
'''

def pooling_demo():
    with ThreadPoolExecutor() as executor:
        '''
        futures1 = executor.submit(func1, 4)
        futures2 = executor.submit(func1, 2)
        futures3 = executor.submit(func1, 1)

        print("printing results ...")
        print(futures1.result())
        print(futures2.result())
        print(futures3.result())
        '''

        time_list = [4,2,1]
        results = executor.map(func1, time_list)
        print('printing results ...')
        for result in results:
            print(result)

pooling_demo()
