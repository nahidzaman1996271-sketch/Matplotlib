import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color = 'blue', linestyle = '--', linewidth = 2, marker = 'o', label = '2025 sales data')
plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.title('Monthly sales Data report')
plt.legend(loc = 'upper left',fontsize = 12)
plt.grid(color = 'gray',linestyle =':',linewidth = 1)
plt.xlim(1,4)
plt.ylim(0,2000)
plt.show()