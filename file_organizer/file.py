import os #it is used to read all the files or it is used to create the fies thats y we are importing 
import shutil # it is used to move one file to another like moving 
folder_path=input("enter path here : ")

for file in os.listdir(folder_path):
    file_path=folder_path + "/" + file #filepath=c:/download/photo.jpg

    if os.path.isfile(file_path):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            targest_folder=folder_path + "/images"
        elif file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".docx"):
            targest_folder=folder_path + "/documents"
        elif file.endswith(".mp4"):
            targest_folder=folder_path + "/videos"
        else:
            targest_folder=folder_path + "/others"


        if not os.path.exists(targest_folder):
            os.makedirs(targest_folder)

        destination=targest_folder + "/" + file


        counter=1

        while os.path.exists(destination):

            name = file.split(".")[0]
            extension = file.split(".")[-1]

            new_name = name + "_" + str(counter) + "." + extension

            destination=targest_folder + "/" + new_name

            counter+=1

        try:
            shutil.move(file_path, destination)
            print(file, "moved successfully")

        except:
            print("Error moving", file)

