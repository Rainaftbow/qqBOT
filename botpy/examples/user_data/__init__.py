import json
import os

if __name__ == "__main__":
    print('[Warning] Initializing all user ToDo lists.')
    print('\n[Warning] Do you wish to continue?[Y/N]')
    flag = input()

    if flag == 'Y' or flag == 'y':
        base_dir = '..\\user_data'
        files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
        for file in files:
            if file == '..\\user_data\\__init__.py':
                print("skip __init__.py")
                continue

            json_data = {'ToDo': ['还没有待办qwq']}
            with open(file, 'w') as json_file:
                json.dump(json_data, json_file)

            print(f'\'{file}\' initialized.')

        print('\n[Info] ***Initialization Complete***')
    elif flag == 'N' or flag == 'n':
        print('[Info] Initialization aborted.')

    else:
        print('[Warning] Illegal argument, process finished.')

"""
此程序会初始化所有的用户待办。
使用方法：
    启动脚本，并确认执行。
程序会遍历所有本目录下的json文件，
并将其全部初始化为空的状态。
"""
