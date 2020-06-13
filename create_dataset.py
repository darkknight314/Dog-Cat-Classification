import matplotlib.image as mpimg
import numpy as np
import os

data_dir = "D:\\Study\\Sem 6\\CS 419 - Intro to ML\\Project\\images\\resized256\\"

images = []
labels = []
class_idx = []
species = []
breed_idx = []

mapping = {
    'Abyssinian': [1, 1, 1],
    'american_bulldog': [2, 2, 1],
    'american_pit_bull_terrier': [3, 2, 2],
    'basset_hound': [4, 2, 3],
    'beagle': [5, 2, 4],
    'Bengal': [6, 1, 2],
    'Birman': [7, 1, 3],
    'Bombay': [8, 1, 4],
    'boxer': [9, 2, 5],
    'British_Shorthair': [10, 1, 5],
    'chihuahua': [11, 2, 6],
    'Egyptian_Mau': [12, 1, 6],
    'english_cocker_spaniel': [13, 2, 7],
    'english_setter': [14, 2, 8],
    'german_shorthaired': [15, 2, 9],
    'great_pyrenees': [16, 2, 10],
    'havanese': [17, 2, 11],
    'japanese_chin': [18, 2, 12],
    'keeshond': [19, 2, 13],
    'leonberger': [20, 2, 14],
    'Maine_Coon': [21, 1, 7],
    'miniature_pinscher': [22, 2, 15],
    'newfoundland': [23, 2, 16],
    'Persian': [24, 1, 8],
    'pomeranian': [25, 2, 17],
    'pug': [26, 2, 18],
    'Ragdoll': [27, 1, 9],
    'Russian_Blue': [28, 1, 10],
    'saint_bernard': [29, 2, 19],
    'samoyed': [30, 2, 20],
    'scottish_terrier': [31, 2, 21],
    'shiba_inu': [32, 2, 22],
    'Siamese': [33, 1, 11],
    'Sphynx': [34, 1, 12],
    'staffordshire_bull_terrier': [35, 2, 23],
    'wheaten_terrier': [36, 2, 24],
    'yorkshire_terrier': [37, 2, 25]
}

k = 0

for image in os.listdir(data_dir):
    if image.endswith(".jpg"):
        im = mpimg.imread(data_dir + image)
        
        images.append(im)
        labels.append(image[:-4])
        
        s = image[:-4].split("_")
        breed = "_".join(s[:-1])
        
        class_idx.append(mapping[breed][0])
        
        species.append(mapping[breed][1])
        
        breed_idx.append(mapping[breed][2])
        
        if(k==200):
            print(image)
            k=0
        k = k+1
        
np.savez_compressed('images.npz', images)
np.savez_compressed('labels.npz', labels)
np.savez_compressed('class_idx.npz', class_idx)
np.savez_compressed('species.npz', species)
np.savez_compressed('breed_idx.npz', breed_idx)