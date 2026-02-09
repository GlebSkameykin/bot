import nest_asyncio
import asyncio

nest_asyncio.apply()

async def print1():
    print(1)
    
async def print2():
    await asyncio.sleep(10)
    print(2)
    
async def print3():
    print(3)

async def main():
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())
    
    await asyncio.gather(task1, task2, task3)
    
asyncio.run(main())