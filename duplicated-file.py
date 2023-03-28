import os
from collections import Counter

# 指定要列出所有檔案的目錄路徑
print("Enter folder path:")
# folder_path = "/Users/jasonz/Documents/test"
folder_path_list = ["/Users/jasonz/Documents/test",
                    "/Users/jasonz/Documents/jason"]
# print(folder_path)

file_dict = {}
for folder_path in folder_path_list:
    # 使用os.walk方法列出所有檔案名稱
    for root, dirs, files in os.walk(folder_path):

        for file_name_full in files:
            file_name, file_ext = os.path.splitext(file_name_full)
            file_path = os.path.join(root, file_name)
            if file_name not in file_dict:
                print(file_name)
                file_dict[file_name] = [file_path]
            else:
                file_dict[file_name].append(file_path)


# 找出重複的檔案名稱
duplicate_files = set()
for file_name, file_paths in file_dict.items():

    if len(file_paths) > 1:
        print(file_name, file_paths)
        duplicate_files.add(file_name)

# 輸出重複的檔案名稱
if len(duplicate_files) > 0:
    print("以下是重複的檔案：")
    for file_name in duplicate_files:
        print(file_name)
        print(file_dict[file_name])
else:
    print("沒有重複的檔案。")
