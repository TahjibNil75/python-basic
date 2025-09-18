import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(3)  # non-blocking wait
    print(f"{name} finished")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())


# import time

# def main():
#     print("Start")
#     time.sleep(3)   # blocks everything for 3 seconds
#     print("End")

# main()
