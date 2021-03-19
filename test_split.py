import os
import random
location = r"B:\data\data\dataset-Traditional-Medicine\train"
location_2 = r"B:\data\data\dataset-Traditional-Medicine\test"

def create_folder(location):
    for i in range(41):
        if not os.path.exists(location+"\\"+str(i+1)):
            os.makedirs(location+"\\X"+str(i+1))
def main(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        new_root = root.replace("train","test")
        for file in files :
            if random.randint(1, 10)== 2:
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)

#create_folder(location_2)
main(location)