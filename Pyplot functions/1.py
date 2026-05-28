import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1800]

plt.title('Just a random line chart')
plt.plot(months, sales, color = 'blue', linestyle = '--', linewidth = 2, marker = 'o', label = '2025 sales data')
plt.show()