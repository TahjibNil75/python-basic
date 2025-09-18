import asyncio
# import time

async def brew(name):
    print(f"{name}: Starting to brew coffee")
    # await asyncio.sleep(2)
    # time.sleep(2)  # Blocking call to simulate a long-running task
    print(f"{name}: Finished brewing coffee")


async def main():
    await asyncio.gather(
        brew("coffee 1"),
        brew("coffee 2"),
        brew("coffee 3"),
    )

asyncio.run(main())