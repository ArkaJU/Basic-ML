

from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_xlabel("PC1")
ax1.set_ylabel("PC2")
ax1.set_zlabel("PC3")
ax1.scatter(reduced[:, 0], reduced[:, 1], reduced[:, 2], c=color1)
plt.show()

