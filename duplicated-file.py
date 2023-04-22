import os
from collections import Counter

from cut_file_name import cut_file_name
import json

def duplicateToJsonFile():
    # 將結果輸出成json格式
    result_json = {'duplicate_files': []}
    for file_name in duplicate_files:
        file_paths = file_dict[file_name]
        result_json['duplicate_files'].append({
            'file_name': file_name,
            'file_paths': file_paths
        })
    with open('duplicate.json', 'w') as f:
        json.dump(result_json, f, indent=4)

def allToJsonFile():
    # 將結果輸出成json格式
    result_json = {'all_files': []}
    for file_name in all_files:
        file_paths = file_dict[file_name]
        result_json['all_files'].append({
            'file_name': file_name,
            'file_paths': file_paths
        })
    with open('all.json', 'w') as f:
        json.dump(result_json, f, indent=4)

# 指定要列出所有檔案的目錄路徑
# print("Enter folder path:")

folder_path_list = []
# print(folder_path)
video_file_ext_list=['.mp4','.avi','.wmv']
file_dict = {}
for folder_path in folder_path_list:
    # 使用os.walk方法列出所有檔案名稱
    for root, dirs, files in os.walk(folder_path):
        # print(folder_path)
        for file_name_full in files:
            file_name, file_ext = os.path.splitext(file_name_full)
            # print(file_name)
            process_file_name=cut_file_name(file_name)
            # print(process_file_name)

            if file_ext not in video_file_ext_list:
                break


            file_path = os.path.join(root, file_name)
            string_process_file_name = '-'.join(process_file_name)

            if string_process_file_name not in file_dict:
                # print(file_name)
                file_dict[string_process_file_name] = [file_path]
            else:
                file_dict[string_process_file_name].append(file_path)


# 找出重複的檔案名稱
duplicate_files = set()
all_files = set()
# 輸出檔案列表


for file_name, file_paths in file_dict.items():
    all_files.add(file_name)
    if len(file_paths) > 1:
        # print(file_name, file_paths)
        duplicate_files.add(file_name)


allToJsonFile()
# 輸出重複的檔案名稱
if len(duplicate_files) > 0:
    print("以下是重複的檔案：")
    for file_name in duplicate_files:
        print(file_name)
        print(file_dict[file_name])
    duplicateToJsonFile()
else:
    print("沒有重複的檔案。")
