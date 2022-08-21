import os


def read_data(file_name):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'input_data', f'{file_name}.txt'))) as reader:
        return [int(i) for i in reader.readlines()]
