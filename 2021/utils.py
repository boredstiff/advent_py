import os


def read_data(file_name, as_int=False):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'input_data', f'{file_name}.txt'))) as reader:
        if as_int:
            return [int(i) for i in reader.readlines()]
        return reader.readlines()
