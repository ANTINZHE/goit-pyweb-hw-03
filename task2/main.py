# Стандартний час +- 0.424074649810791
# Використання кількох ядер +- 0.6279635429382324

import time
import concurrent.futures

start_time = time.time()


def factorize(*number, executor):
    futures = [executor.submit(range_numbers, num) for num in number]
    return [f.result() for f in futures]


def range_numbers(num):
    list_of_numbers = [i for i in range(1, num + 1) if num % i == 0]
    return list_of_numbers


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        a, b, c, d = factorize(128, 255, 99999, 10651060, executor=executor)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]

    end_time = time.time()
    print(end_time - start_time)


if __name__ == "__main__":
    main()
