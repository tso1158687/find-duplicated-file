import re
def cut_file_name(string1):
    # 分割字串，使用小寫來比較
    pattern = "[-_]"
    split1 = re.split(pattern, string1)[:2]
    lower1 = [s.lower() for s in split1]
    return lower1