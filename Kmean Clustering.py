import pandas as pd
import matplotlib.pyplot as mpt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


"""
KMean Clustering: It is unsupervised machine learning algorithm in which data points are clustured and classified 
"""

df = pd.read_csv("TSf Dataset.csv")
mpt.scatter(df.Hours, df.Scores, color="orange")
mpt.show()

km = KMeans(n_clusters=4)

mod = km.fit_predict(df[["Hours", "Scores"]])

df['Cluster'] = mod

df0 = df[df['Cluster'] == 0]
df1 = df[df['Cluster'] == 1]
df2 = df[df['Cluster'] == 2]
df3 = df[df['Cluster'] == 3]

mpt.scatter(df0.Hours, df0.Scores, color="purple", label="Cluster 0")
mpt.scatter(df1.Hours, df1.Scores, color="green", label="Cluster 1")
mpt.scatter(df2.Hours, df2.Scores, color="blue", label="Cluster 2")
mpt.scatter(df3.Hours, df3.Scores, color="black", label="Cluster 3")
mpt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='red', marker='*')
mpt.xlabel("Hours")
mpt.ylabel("Scores")
mpt.legend(loc='best')
mpt.show()

k_range = range(1, 25)
sse = []
for k in k_range:
    km1 = KMeans(n_clusters=k)
    km1.fit(df[['Hours', 'Scores']])
    sse.append(km1.inertia_)

mpt.scatter(k_range, sse)
mpt.show()
