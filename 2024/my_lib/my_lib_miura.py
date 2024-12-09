def read_file(file_name):
    with open(file_name, mode='r') as f:
        content = f.readlines()
    content = list(map(lambda x: x.replace('\n',''), content))
    return content