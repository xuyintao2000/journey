import asyncio
import requests


async def hello1(url):
    print('55555555555555555555')
    async with requests.get(url) as resp:
        print(url, resp.status_code)
    print('666666666666')


async def hello(n, url):
    print("协程" + str(n) + "启动")
    await hello1(url)
    print("协程" + str(n) + "结束")


if __name__ == "__main__":
    tasks = []
    url = 'http://www.baidu.com'
    for i in range(0, 3):
        tasks.append(hello(i, url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
