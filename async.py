import time
import asyncio
import datetime

'''
async def func1():
    time.sleep(2)
    for i in range(1, 5):
        print('func1: '+str(i))

async def func2():
    time.sleep(2)
    for i in range(1, 5):
        print('func2: '+str(i))

async def func3():
    time.sleep(2)
    for i in range(1, 5):
        print('func3: '+str(i))

async def main():
    await func1()
    await func2()
    await func3()

asyncio.run(main())
'''

# the above code still runs in synchronous manner

# below is asynchronous manner
async def func1():
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func1 start time: ',value)
    for i in range(1, 10):
        await asyncio.sleep(0.5)
        print('func1: '+str(i))
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func1 end time: ',value)
    return "func1"

async def func2():
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func2 start time: ',value)
    for i in range(1, 10):
        await asyncio.sleep(0.5)
        print('func2: '+str(i))
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func2 end time: ',value)
    return "func2"

async def func3():
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func3 start time: ',value)
    for i in range(1, 10):
        await asyncio.sleep(0.5)
        print('func3: '+str(i))
    #value = datetime.datetime.fromtimestamp(time.time())
    #print('func3 end time: ',value)
    return "func3"
'''
async def func4(text):
    for i in range(10):
        await asyncio.sleep(1)
        print(f'func4: {text}')
'''

async def main():
    '''
    # in below func2 runs and when the moment it gets time func1 gets executed 
    # and then after 2 seconds func3 gets executed
    task = asyncio.create_task(func1())
    #await func1()
    await func2()
    await func3()
    '''

    # run all functions at the same time
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print(L)

asyncio.run(main())
