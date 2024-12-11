def read_file(file_name):
    with open(file_name, mode='r') as f:
        content = f.read()
    return content