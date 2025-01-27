import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
original_dataset_dir = 'dataset/original'
train_dir = 'dataset/train'
test_dir = 'dataset/test'
val_dir = 'dataset/val'

# Create train, test, and val directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Split the dataset
for _,category in zip(range(len(os.listdir(original_dataset_dir))),os.listdir(original_dataset_dir)):
    category_path = os.path.join(original_dataset_dir, category)
    if os.path.isdir(category_path):
        # List all images in the category
        images = os.listdir(category_path)
        
        # Split images into train, test, and validation sets
        train_images, temp_images = train_test_split(images, test_size=0.4, random_state=42)
        test_images, val_images = train_test_split(temp_images, test_size=0.5, random_state=42)
        
        _ = str(_)
        # Move and rename images
        for i, image in enumerate(train_images):
            src = os.path.join(category_path, image)
            os.makedirs(train_dir+"/"+_, exist_ok=True)
            dst = os.path.join(train_dir+"/"+_, image)#f"{category}_{i+1}.jpg")
            shutil.copyfile(src, dst)

        for i, image in enumerate(test_images):
            src = os.path.join(category_path, image)
            os.makedirs(test_dir+"/"+_, exist_ok=True)
            dst = os.path.join(test_dir+"/"+_, image)#f"{category}_{i+1}.jpg")
            shutil.copyfile(src, dst)

        for i, image in enumerate(val_images):
            src = os.path.join(category_path, image)
            os.makedirs(val_dir+"/"+_, exist_ok=True)
            dst = os.path.join(val_dir+"/"+_, image)# f"{category}_{i+1}.jpg")
            shutil.copyfile(src, dst)

print("Dataset has been split and images have been renamed and moved successfully!")


# Example list of elements
elements = os.listdir(original_dataset_dir)

# Specify the path and name of the file
file_path = 'output.txt'

# Open the file in write mode and write the list elements
with open(file_path, 'w') as file:
    for element in elements:
        file.write(f"{element}\n")

print(f"File '{file_path}' has been created and written successfully!")
