import time
import threading
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


def main_treads(in_number: SequenceInt):
    tasks = []
    for index, number in enumerate(in_number):
        tasks.append(
            threading.Thread(
               target=factorize_single_print,
               args=(index, number)
            )
        )
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main_treads(numbers)
    treads_duration = time.perf_counter() - start
    print(treads_duration)
