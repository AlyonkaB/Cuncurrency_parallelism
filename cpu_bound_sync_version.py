import time
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


def factorize_single(number: int) -> TupleIntDivisors:
    return tuple([x for x in range(1, number + 1) if number % x == 0])


def factorize_single_print(index: int, number: int):
    print(f"start task #{index}")
    dividers = factorize_single(number)
    print(f"Result {index}, factorize single: {number} = {dividers}")
    print("-" * 25)


def main_sync(in_number: SequenceInt = numbers):
    for index, number in enumerate(in_number):
        factorize_single_print(index, number)


if __name__ == "__main__":
    start = time.perf_counter()
    main_sync()
    sync_duration = time.perf_counter() - start
    print(sync_duration)
