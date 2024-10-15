import asyncio
import time
import httpx


from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com",) * 50


async def send_request(count: int, url: str, client: httpx.AsyncClient):
    print(f"Sending request #{count}")
    response = await client.get(url)
    print(f"got response for request {count}, status code: {response.status_code}")


async def main_asyncio(in_urls: Urls = urls):
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(send_request(count, url, client)) for count, url in enumerate(in_urls)]


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_asyncio(urls))
    async_duration = time.perf_counter() - start
    print(async_duration)
