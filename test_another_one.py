import matplotlib.pyplot as plt

x = ['Mon','Tues','Wed','Thur','Fri'] # This is for X-axis
y = [10, 15, 7, 20, 12] # And this is for Y-axis

plt.plot(x, y)
plt.title('Bakery sales on this week')
plt.xlabel('Day of the week')
plt.ylabel('Sales per day')

plt.show()