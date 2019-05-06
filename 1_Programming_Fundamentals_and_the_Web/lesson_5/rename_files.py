import os
def rename_files():
    # get file names from folder
    file_list = os.listdir(r"/Users/souvikbanerjee/Desktop/Data_Science/Full-Stack-Nanodegree/1_Programming_Fundamentals_and_the_Web/lesson_5/prank")
    print(file_list)
    # change name of files
    save_directory = os.getcwd()
    os.chdir(r"/Users/souvikbanerjee/Desktop/Data_Science/Full-Stack-Nanodegree/1_Programming_Fundamentals_and_the_Web/lesson_5/prank")
    for file_name in file_list:
        print('old file name: 'file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print('new file name: 'file_name)
    os.chdir(save_directory)
rename_files()