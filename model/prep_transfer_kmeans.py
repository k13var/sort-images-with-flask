import os
import numpy as np
import cv2
import keras.backend as K
from tensorflow.keras import Sequential
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

def extract_vector(folder):
    '''
    The function will open every image in the given folder,
    apply a preprocessing methods and return a feartures array, 
    along with a labels vector and the image categories inferred
    from image titles.
    input: folder path
    output: features array
    '''
    transf_model = Sequential()
    transf_model.add(ResNet50(weights='imagenet', include_top=False))

    # say no to training first layer (ResNet) model. It is already trained
    transf_model.layers[0].trainable = False
    
    resnet_feature_list = []
    counter = 0
    for root, dirs, filenames in os.walk(folder):
        for file in filenames:
            # load and preprocess the image file
            imgFile = os.path.join(root,file)
            img = cv2.imread(imgFile)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_large = cv2.resize(img,(224,224))
            img_model = preprocess_input(np.expand_dims(img_large.copy(), axis=0))
            # for every image apply the ResNet50 to create a feature vector 
            resnet_feature = transf_model.predict(img_model)
            resnet_feature_np = np.array(resnet_feature)
            resnet_feature_list.append(resnet_feature_np.flatten())
            # keep track of processed images via a counter
            counter+=1
            if counter%100==0:
                print(f'{counter} images processed')
    # output a features matrix of all images
    features_array = np.array(resnet_feature_list)
    return features_array