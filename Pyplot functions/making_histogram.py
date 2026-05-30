import matplotlib.pyplot as plt

scores = [45,67,89,56,88,98,12,70,77,88,25,69,11,10]

plt.hist(scores, bins=5, color = 'purple',edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of students')
plt.title('Score distribution of Students')
plt.show()