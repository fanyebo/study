# coding: utf-8
import asyncio

# 声明一个协程函数
async def main():
    print('hello')
    # 挂起程序, 在执行长时间的操作时可以挂起程序去执行其它异步程序
    # await 后面只能跟异步程序或有__await__属性的对象
    # 同一个协程中多个await是串行的
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    # 执行异步程序并返回结果
    res = asyncio.run(main())
