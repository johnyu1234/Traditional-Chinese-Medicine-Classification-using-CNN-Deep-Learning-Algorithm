import os
location = r"B:\data\data\dataset-Traditional-Medicine\train"
location_2 = r"C:\Users\johny\OneDrive\Desktop\Fall 2021\Project\dataset\train"
def main(file_dir):
    f = open("dataset_TCM.txt", "a")
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        f.write(os.path.basename(root)+"\n")
        counter=0
        for file in files :
            counter +=1
        print(counter)
        if(counter != 0):
            f.write(str(counter))
            f.write("\n")
    f.close()


main(location)
print("****************************************")
#main(location_2)
