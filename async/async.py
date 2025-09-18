import asyncio


async def brew_coffe():
    print("Starting to brew coffee")
    await asyncio.sleep(3)
    print("Finished brewing coffee")

asyncio.run(brew_coffe())
