import os
from model.kmeans import kmeans
from model.prep_kmeans import prep_data
from model.prep_transfer_kmeans import extract_vector

# path to the folder where we'll store the data
DATA_FOLDER = os.path.join('static','data')

def sort_images(n_clusters,model):
    n_clusters = int(n_clusters)
    if model=='option1':
        print('Preparing features...')
        features = prep_data(DATA_FOLDER)
        print('Features ready')
        print('Computing clusters...')
        labels = kmeans(features, n_clusters)  
    else:
        print('Preparing features...')
        features = extract_vector(DATA_FOLDER)
        print('Features ready')
        print('Computing clusters...')
        labels = kmeans(features, n_clusters)
    print('Images sorted')
    return labels