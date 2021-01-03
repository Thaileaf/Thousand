import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.ticker import MaxNLocator

# calculates average time for bogosort on size n arrays, from low to high n
def sort_data(low, high, algo):
    data = []
    for i in range(low, high + 1):
        avg_times = []
        steps = []
        for j in range(0, 10):
            unsorted = [random.randint(0, i - 1) for x in range(0, i)]
            start = time.time()
            step = algo(unsorted)
            end = time.time()
            total = end - start
            avg_times.append(total * 1000)
            steps.append(step)

        mean = sum(avg_times) / len(avg_times)
        step_mean = sum(steps) / len(steps)
        print(f'It took  average {mean} milliseconds to {algo.__name__} an array with a size of {i}')
        data.append((steps, avg_times, step_mean, mean, i))
    return data

def plot_algo(low, high, algo):
    graphs = plt.figure(1, figsize=(24, 12))
    graphs.suptitle(f'{algo.__name__} data', fontsize=16)
    steps = graphs.add_subplot(121)
    steps.xaxis.set_major_locator(MaxNLocator(integer=True))
    steps.set_xlabel('List Size')
    steps.set_ylabel('Steps')

    time_ms = graphs.add_subplot(122)
    time_ms.xaxis.set_major_locator(MaxNLocator(integer=True))
    time_ms.set_xlabel('List Size')
    time_ms.set_ylabel('Time in ms')

    data = sort_data(low, high, algo)

    for i in data:
        steps.plot([i[4]] * len(i[0]), i[0], '-o')
        steps.plot([i[4]] * len(i[0]), [i[2]] * len(i[1]), 'Dk')
        time_ms.plot([i[4]] * len(i[1]), i[1], '-o')
        time_ms.plot([i[4]] * len(i[1]), [i[3]] * len(i[1]), 'Dk')


    plt.show()



