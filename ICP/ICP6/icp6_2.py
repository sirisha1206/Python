import pandas as pd
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Reading the data from csv file using pandas library
data = pd.read_csv('sample_stocks.csv')

Y = data[['returns']]
X = data[['dividendyield']]

#predicting the value of k

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.show()

pca = PCA(n_components=1).fit(Y)
pca_d = pca.transform(Y)
pca_c = pca.transform(X)

clusters =  int(input('Enter number of clusters:'))
kmeans=KMeans(n_clusters=clusters)
kmeansoutput=kmeans.fit(Y)
kmeansoutput

pl.figure('Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()