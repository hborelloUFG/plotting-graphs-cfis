from cProfile import label
from distutils.archive_util import make_archive
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
import numpy as np

SMALL_SIZE = 16
MEDIUM_SIZE = 18
BIGGER_SIZE = 20

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

df = pd.read_csv('data/clustered-resources-125.csv')

# df = df.drop(labels=range(0, 13), axis=0)
print(df.head())

ncenters = df['Geo.Cluster'].max()+1
print('Number of clusters: ', ncenters)

X = pd.DataFrame(df, columns=['Latitude','Longitude','MIPS','RAM','BW','Geo.Cluster']).to_numpy()

colors = ['gray', 'darkorange', 'gold', 'silver', 'blue', 'teal', 
        'violet', 'green', 'cyan', 'navy', 'black', 'red']

m = ['o', '^', '1', 's', 'p', 'P', '*', '+', 'h', 'd', 'x', '2']

f, axes = plt.subplots(figsize=(15,8))
axes.set(xlabel='Longitude', ylabel='Latitude', title='Melbourne CBD Fog Nodes')
for i in range(1, ncenters):
    filter = X[:,5] == i
    R = X[filter]

    l = 'Geo-Cluster ' + str(i)
    axes.scatter(R[:,1], R[:,0], label=l, c=colors[i-1], marker=m[i-1], s=60)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=4)

# plt.show()
plt.savefig('graphs/fog_nodes_mlbcbd_geoclusters.svg', bbox_inches='tight', format='svg')