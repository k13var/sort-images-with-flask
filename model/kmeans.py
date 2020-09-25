from sklearn.cluster import MiniBatchKMeans

def kmeans(features, n_clusters):
    '''
    The function will run the k-means algorithms on a preprocessed
    features array and return the cluster label for each feature.
    input: features array, desired number of clusters
    output: labels vector of the lenght of the fatures array
    '''
    kmeans = MiniBatchKMeans(n_clusters = n_clusters, n_init=20).fit(features)
    return kmeans.labels_