import multiprocessing
import time
import httpx


from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com",) * 50


def send_request(count: int, url: str):
    print(f"Sending request #{count}")
    response = httpx.get(url)
    print(f"got response for request {count}, status code: {response.status_code}")


def main_multiprocess(in_urls: Urls = urls):

    tasks = []
    for num, url in enumerate(in_urls):
        tasks.append(multiprocessing.Process(target=send_request, args=(num, url)))
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main_multiprocess(urls)
    multiprocess_duration = time.perf_counter() - start
    print(multiprocess_duration)
