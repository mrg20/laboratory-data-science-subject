import os

# define the name of the directory to be created
cryptocurrency_raw='../../data/raw/cryptocurrency'
iris_raw='../../data/raw/iris'
measures_raw='../../data/raw/measures'
cryptocurrency_processed='../../data/processed/cryptocurrency'
iris_processed='../../data/processed/iris'
measures_processed='../../data/processed/measures'

for dr in [cryptocurrency_raw, iris_raw, measures_raw, cryptocurrency_processed, iris_processed, measures_processed]:
    os.makedirs(dr, exist_ok=True)
