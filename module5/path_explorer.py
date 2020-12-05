import os

def displayFiles(path):
    if os.path.isfile(path):
        f_input = open(path, "r")
        print("File name:", path)
        # print(f_input.read())
        f_input.close()
    else:
        directory_items = os.listdir(path)
        print("Directory name:", path)
        for item in directory_items:
            displayFiles(path + os.sep + item)


# print(os.getcwd())
os.chdir("..")
displayFiles(os.getcwd())