'''
Author: szh
Date: 2023-02-27 16:21:20
LastEditors: szh
LastEditTime: 2023-02-27 18:59:07
Description: 
FilePath: /codet5-apps/test_apps/result_style.py
'''
import os
import pickle as pkl
import numpy as np

def deal_result(root_path):
    filename_list = os.listdir(root_path)
    save_result = {}
    for filename in filename_list:
        try:
            with open(os.path.join(root_path, filename), 'rb') as f:
                data = pkl.load(f)
            file_id = filename.split('.')[0]
            result = data[f"{file_id}"]["results"]
            # result = [[x[0] for x in result_dif1]]
            save_result[f"{file_id}"] = result
        except:
            continue
    return save_result

