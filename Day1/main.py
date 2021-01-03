import BogoSort
import random
import time

# calculates average time for bogosort on size n arrays, from low to high n
def avg_bogosort(low, high):
    for i in range(low, high + 1):
        avg_times = []
        for j in range(0, 10):
            unsorted = [random.randint(0, i - 1) for x in range(0, i)]
            start = time.time()
            BogoSort.bogosort(unsorted)
            end = time.time()
            total = end - start
            avg_times.append(total)

        mean = 0
        for j in avg_times:
            mean += j
        mean = mean / len(avg_times)
        print(f'It took  average {mean * 1000} milliseconds to bogosort an array with a size of {i}')
        time.sleep(3)


if __name__ == '__main__':
    avg_bogosort(5, 10)