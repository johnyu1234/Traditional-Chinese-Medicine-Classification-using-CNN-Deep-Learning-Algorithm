import os
location = r"B:\data\data\dataset-Traditional-Medicine\train"
location_2 = r"C:\Users\johny\OneDrive\Desktop\Fall 2021\Project\dataset\train"
def main(file_dir):
    f = open("check_fold5.txt", "a")
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))
        f.write(os.path.basename(root)+"\n")
        counter=0
        for file in files :
            f.write(str(file))
            counter +=1
        print(counter)
        if(counter != 0):
            f.write(str(counter))
            f.write("\n")
    f.close()

def check_total(file_dir):
    total = 0
    for root, _, files in os.walk(file_dir):
        #print(os.path.basename(root))
        counter=0
        for file in files :
            counter +=1
            total+=1
        #print(counter)
    print(total)
#main(r"B:\data\data\dataset-Traditional-Medicine\folding\fold5")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding\fold1")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding\fold2")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding\fold3")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding\fold4")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding\fold5")
print("****************************************")
check_total(r"B:\data\data\dataset-Traditional-Medicine\folding")

