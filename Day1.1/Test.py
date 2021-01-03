import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
x1 = [1, 2, 3]
y1 = [4, 5, 6]
# y1 = 2  Must match dimensions
x2 = [1, 3, 5]
y2 = [6, 5, 4]

plot1 = plt.figure(1, figsize=(12, 12))  # Makes figure class with int identifier of 1, border size of 12 by 12
chart1 = plot1.add_subplot(211)
chart2 = plot1.add_subplot(212)
# plt.plot(x1, y1)  # Adds x1 and y1 to last figure/subplot

chart1.plot(x1, y1, '--k')  # Line, third parameter is line properties
chart2.scatter(x1, y1)  # Scatter points

chart1.set_xlabel('xlabel')  # Sets x and y labels on subplots
chart1.set_ylabel('ylabel')

chart2.set_xlabel('xlabel')
chart2.set_ylabel('ylabel')

chart1.axis([0, 5, 0, 10])
chart2.axis([0, 5, 0, 10])

chart1.set_title('chart1 title')
chart2.set_title('chart2 title')

# plt.xlabel('X axis')  # X axis label, cannot label subplots individually
# plt.ylabel('Y axis')

plot2 = plt.figure(2)
plt.plot(x2, y2)

plt.show()