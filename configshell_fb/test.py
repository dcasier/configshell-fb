import asyncio
import time


async def main():
    print('ENTER')


st = time.time()
asyncio.run(main())
et = time.time()

print(et - st)
