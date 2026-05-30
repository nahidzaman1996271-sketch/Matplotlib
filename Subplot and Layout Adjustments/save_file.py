import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

#create plot
plt.plot(x,y, color='blue',marker='o')
plt.title('Sample Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.savefig('line_plot.png',dpi=300,bbox_inches='tight')
plt.show()