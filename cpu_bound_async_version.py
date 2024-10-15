import time
import asyncio
from typing import Sequence, Tuple


SequenceInt = Sequence[int]
TupleIntDivisors = Tuple[int]

numbers = (
    3_111_000,
    3_111_001,
    3_111_011,
    3_111_088,
    3_222_000,
    3_444_025,
    4_111_189,
    7_777_777
)


async def factorize_single(number: int) -> TupleIntDivisors:
    return tuple([x for x in range(1, number + 1) if number % x == 0])


async def factorize_single_print(index: int, number: int):
    print(f"start task #{index}")
    dividers = await factorize_single(number)
    print(f"Result {index}, factorize single: {number} = {dividers}")
    print("-" * 25)


async def main_async(in_number: SequenceInt):
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(factorize_single_print(index, number))
         for index, number in enumerate(in_number)]


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_async(numbers))
    async_duration = time.perf_counter() - start
    print(async_duration)
