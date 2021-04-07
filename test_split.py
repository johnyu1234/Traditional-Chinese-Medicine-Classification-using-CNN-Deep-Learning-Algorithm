import os
import random
location = r"B:\data\data\dataset-Traditional-Medicine\train"
location_3 = r"B:\data\data\dataset-Traditional-Medicine\folding"
location_2 = r"B:\data\data\dataset-Traditional-Medicine\test"
location_4= r"B:\data\data\dataset-Traditional-Medicine\folding\ori_data"
def create_folder(location):
    list = ["fold1","fold2","fold3","fold4","fold5"]
    for j in range(5):
        for i in range(41):
            if not os.path.exists(location+"\\"+"\\"+list[j]+"\\X"+str(i+1)):
                os.makedirs(location+"\\"+"\\"+list[j]+"\\X"+str(i+1))
      #      if not os.path.exists(location+"\\"+"train"+"\\"+list[j]+"\\X"+str(i+1)):
       #         os.makedirs(location+"\\"+"train"+"\\"+list[j]+"\\X"+str(i+1))
def fold_cross_val(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        for file in files :
            val = random.randint(1, 10)
            if val<= 2:
                new_root = root.replace("ori_data", "fold1")
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)
            if 2< val <= 4:
                new_root = root.replace("ori_data", "fold2")
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)
            if 4 < val <= 6:
                new_root = root.replace("ori_data", "fold3")
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)
            if 6 <val <= 8:
                new_root = root.replace("ori_data", "fold4")
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)
            if 8 < val <= 10:
                new_root = root.replace("ori_data", "fold5")
                os.rename(root+"\\"+file,new_root+"\\"+file)
                print(file)
def main(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        new_root = root.replace("train", "test")
        for file in files:
            if random.randint(1, 10) == 2:
                os.rename(root + "\\" + file, new_root + "\\" + file)
                print(file)
#create_folder(location_3)
#main(location)
fold_cross_val(location_4)