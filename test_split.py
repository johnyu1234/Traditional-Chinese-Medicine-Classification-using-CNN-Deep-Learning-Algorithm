import os
import random
import shutil
location = r"B:\data\data\dataset-Traditional-Medicine\train"
location_3 = r"B:\data\data\dataset-Traditional-Medicine\folding"
location_2 = r"B:\data\data\dataset-Traditional-Medicine\test"
location_4= r"B:\data\data\dataset-Traditional-Medicine\folding\ori_data"
list_fold = ["fold1", "fold2", "fold3", "fold4", "fold5"]
list_train = ["train_1", "train_2", "train_3", "train_4", "train_5"]
def create_proper_data(location):
    counter = 0
    for i in list:
        #final=location+"\\"+i
        counter += 1
        for j in range(5):

            if(j+1) == counter :
                print("val")
            else:
                for root, _, files in os.walk(location+"\\"+list_fold[j]):
                    print(os.path.basename(root))
                    print(root)
                    final = root.replace(list_fold[j],i)
                    print(final)
                    for file in files:
                        print(file)
                        shutil.copyfile(root+"\\"+file, final+"\\"+file)
def create_folder_only(location):
        for i in range(41):
            if not os.path.exists(location+"\\"+"\\X"+str(i+1)):
                os.makedirs(location+"\\"+"\\"+"\\X"+str(i+1))
def create_folder(location,list):
    for j in range(list):
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
        for file in files:
            val = random.randint(1, 10)
            if val <= 2:
                new_root = root.replace("train", "test")
                os.rename(root + "\\" + file, new_root + "\\" + file)
                print(file)
            elif 2 <val <=4:
                new_root = root.replace("train", "val")
                os.rename(root + "\\" + file, new_root + "\\" + file)
                print(file)
def object_detect(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        for file in files:
                new_root = root.replace("test", "object_detect")
                shutil.copyfile(root + "\\" + file, new_root+ "\\" + file)
                print(file)
                break


#create_folder(location_3)
#main(location)
#fold_cross_val(location_4)
#create_folder_2(location_3)
#create_proper_data(location_3)
#list=list()
create_folder_only(r"B:\data\data\dataset-Traditional-Medicine\11_4\object_detect")

#main(r"B:\File\data_TCM\train")
object_detect(r"B:\data\data\dataset-Traditional-Medicine\11_4\test")
# to test push