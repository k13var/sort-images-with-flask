import os

# path to the folder where we'll store the data
DATA_FOLDER = 'data'

def show_cluster_images(index):
    for root, folders, filenames in os.walk(DATA_FOLDER):
        full_filename = str(DATA_FOLDER + '/' +filenames[index])
    full_filename = full_filename
    print(full_filename)
    return full_filename