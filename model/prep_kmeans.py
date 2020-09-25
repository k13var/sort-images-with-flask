import os
import numpy as np
from PIL import Image 

def prep_data(folder):
    '''
    The function will open every image in the given folder,
    apply a preprocessing methods and return a feartures array, 
    along with a labels vector and the image categories inferred
    from image titles.
    input: path to the folder
    output: features array
    '''
    features = []
    newsize = (300, 300) # the final image size
    for root, folders, filenames in os.walk(folder):
        for file in filenames:
            # preprocess the images 
            imgFile = os.path.join(root,file)
            img = Image.open(imgFile)
            # resize the image by keeping the aspect ratio
            img_resize = img.resize(newsize, Image.ANTIALIAS)
            img_resize = np.array(img_resize)
            features.append(img_resize.ravel())
    # output a features matrix of all images
    features = np.array(features)/255.
    return features