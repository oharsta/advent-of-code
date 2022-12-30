import os


def read_lines(file_name: str) -> str:
    file = f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}"
    with open(file) as f:
        return f.readlines()
