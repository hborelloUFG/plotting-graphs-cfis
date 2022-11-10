from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
import numpy as np

df = pd.read_csv('data/clustered-resources-125.csv')
print(df.head())
# df['Geo.Cluster'] = df['Geo.Cluster'].astype('int')+1

ncenters = df['Geo.Cluster'].max()
print('Number of clusters: ', ncenters)

X = pd.DataFrame(df).to_numpy()
cluster = 6
size = 30

f, axes = plt.subplots(1, 3, figsize=(14,4))
# f, axes = plt.subplots(3, 1, figsize=(3,9))

axes[0].set(xlabel='Longitude', ylabel='Latitude', title='A')
axes[1].set(xlabel='Longitude', ylabel='Latitude', title='B')
axes[2].set(xlabel='Longitude', ylabel='Latitude', title='C')
# for i in range(1, ncenters+1):
filter = X[:,8] == 6
R = X[filter]

print('Cluster: ', 6)
R[:,9] = np.where(R[:,9] == 1, 0.2, 1)
R[:,10] = np.where(R[:,10] == 1, 0.2, 1)
R[:,11] = np.where(R[:,11] == 1, 0.2, 1)
# print(R)

lb = 'Cluster ' + str(6)
color = 'teal'
    
# color = 'silver' if i==4 else 'white'
# color = 'silver' if i==4 else 'white'
# axes.scatter(R[:,2], R[:,1], label=lb, alpha=R[:,9]/2)
axes[0].scatter(R[:,2], R[:,1], c=color, alpha=R[:,9], s=size, marker='P')
axes[1].scatter(R[:,2], R[:,1], c=color, alpha=R[:,10], s=size, marker='P')
axes[2].scatter(R[:,2], R[:,1], c=color, alpha=R[:,11], s=size, marker='P')

# plt.legend()
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
           #fancybox=True, shadow=True, ncol=5)
# axes[0].get_xaxis().set_ticks([])
# axes[0].get_yaxis().set_ticks([])

#axes[1].get_xaxis().set_ticks([])
#axes[1].get_yaxis().set_ticks([])

#axes[2].get_xaxis().set_ticks([])
#axes[2].get_yaxis().set_ticks([])

f.tight_layout()
# plt.show()
plt.savefig('graphs/fog_nodes_mlbcbd_geoclusters_features.svg', bbox_inches='tight', format='svg')
