import os

# define the name of the directory to be created
cryptocurrency_raw='../../data/raw/cryptocurrency'
iris_raw='../data/raw/iris'
measures_raw='../data/raw/measures'
cryptocurrency_processed='../../data/processed/cryptocurrency'
iris_processed='../data/processed/iris'
measures_processed='../data/processed/measures'

try:
    os.makedirs('../../data/raw/')
    os.makedirs('../../data/processed/')
    for dr in [cryptocurrency_raw, iris_raw, measures_raw, cryptocurrency_processed, iris_processed, measures_processed]:
        os.mkdir(dr)
except OSError:  
    print ("Creation of the directory failed ", dr)
else:  
    print ("Successfully created the directory")