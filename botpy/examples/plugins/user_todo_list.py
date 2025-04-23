import json
import os


def show(user_name):
    base_dir = '..\\examples\\user_data\\'
    files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
    flag = False
    # print(files)
    for file in files:
        if file == f'..\\examples\\user_data\\{user_name}.json':
            flag = True
            print(f'[info] File found: \'{base_dir}{user_name}.json\'')
    if flag:
        with open(f'..\\examples\\user_data\\{user_name}.json', 'r') as file:
            json_data = json.load(file)
        todo_list = json_data['ToDo']
        return todo_list

    else:
        return file_not_found(base_dir, user_name)


"""
显示某一用户的所有待办。
调用方式：
    将用户的openid作为user_name传入函数。
    在user_data目录下找到存储该用户待办的json文件。读取并转化为list类别返回。
    如果不存在该文件，则会以用户openid为文件名创建一个新的json文件。
"""


def insert(user_name, todo):
    base_dir = '..\\examples\\user_data\\'
    files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
    flag = False
    for file in files:
        if file == f'..\\examples\\user_data\\{user_name}.json':
            flag = True
    if flag:
        with open(f'..\\examples\\user_data\\{user_name}.json', 'r') as file:
            json_data = json.load(file)
        todo_list = json_data['ToDo']
        is_empty = False
        for todo1 in todo_list:
            if todo1 == '还没有待办qwq':
                is_empty = True
                break
        if is_empty:
            todo_list.clear()
        todo_list.append(todo)
        # todo_list.append(" ")
        json_data = {'ToDo': todo_list}
        with open(f'..\\examples\\user_data\\{user_name}.json', 'w') as file:
            json.dump(json_data, file)
        return 1

    else:
        return file_not_found(base_dir, user_name)


"""
为用户添加一条新的待办。
调用方式：
    找到存储用户待办的json文件，读取待办数据。
    转化为list类型。之后向list变量中添加一条新的元素。
    将该变量赋值给json文件。
    
    如果待办列表为空，即存在一条提示为空的字段，则删除所有字段，并添加新字段。
    
存在问题：
    若用户输入的字段为'还没有待办qwq'，则下一次无法正常添加。
    
    好吧其实我刚刚才意识到这个问题（汗）
"""


def delete(user_name, num):
    base_dir = '..\\examples\\user_data\\'
    files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
    flag = False
    for file in files:
        if file == f'..\\examples\\user_data\\{user_name}.json':
            flag = True

    if flag:
        with open(f'..\\examples\\user_data\\{user_name}.json', 'r') as file:
            json_data = json.load(file)
        todo_list = json_data['ToDo']

        if len(todo_list) <= 2:
            print('[Info] ToDo list will be empty after this process.')
            print('[Info] Initializing ToDo list instead.')
            init(user_name)
            return 1

        if num > len(todo_list):
            print('[Warning] List length out of range.')
            return -2

        todo_list.pop(num - 1)
        json_data = {'ToDo': todo_list}
        with open(f'..\\examples\\user_data\\{user_name}.json', 'w') as file:
            json.dump(json_data, file)
        return 1

    else:
        return file_not_found(base_dir, user_name)


"""
删除某一条待办。
调用方式：
    传入用户openid(user_name)和删除序号(num)。
    将json字典转为list。
    删除list中序号为num - 1的元素。
    再赋值给json字典，导入json文件中，覆盖掉原有内容。
"""


def init(user_name):
    print(f'[Warning] Initializing ToDo List of \'{user_name}\'')
    base_dir = '..\\examples\\user_data\\'
    files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
    for file in files:
        if file == f'..\\examples\\user_data\\{user_name}.json':
            json_data = {'ToDo': ['还没有待办qwq']}
            with open(file, 'w') as json_file:
                json.dump(json_data, json_file)

            print(f'\'{file}\' initialized.')
            return 1

    return file_not_found(base_dir, user_name)


"""
初始化用户待办。
调用方法：
    传入用户openid为user_name。并将以该openid命名的json文件初始化。
"""


def file_not_found(base_dir, user_name):
    print(f'[Waring] File \'{base_dir}{user_name}.json\' not found')
    print(f'[Info] Creating file \'{base_dir}{user_name}.json\'')
    json_data = {'ToDo': ['还没有待办qwq', ' ']}
    with open(f'..\\examples\\user_data\\{user_name}.json', 'w') as file:
        json.dump(json_data, file)
    not_found = -1
    return not_found


"""
不存在该用户时，调用此函数。
调用方法：
    传入用户openid为user_name.
    以此openid为文件名创建一个新的json文件。
"""
