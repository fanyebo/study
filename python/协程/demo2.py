# coding: utf-8
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return delay


async def main():
    # asyncio.create_task封装成Task后, 多个task可并发运行
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    # 执行总共需要2秒
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

    # 执行总共需要3秒
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

    # 多任务并行简化写法
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, 'hello'))
        tg.create_task(say_after(2, 'world'))
        print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")

    # 并行运行任务, 返回任务的结果列表
    res_list = await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )
    print(res_list)


if __name__ == '__main__':
    asyncio.run(main())
