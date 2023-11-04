import pytest

def write_file(file_name, file_content):

    full_file_name = str(file_name) + ".txt"

    with open(full_file_name, "w") as file:
        file.write(file_content)


    pass

def append_file(file_name, append_content):

    full_file_name = str(file_name) + ".txt"

    with open(full_file_name, "a") as file:
        file.write(append_content + "\n")


    pass

def read_file(file_name):

    full_file_name = str(file_name) + ".txt"

    with open(full_file_name, "r") as file:
        content = file.read()
        return content 


    pass
