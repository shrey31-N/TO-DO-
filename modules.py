
FILEPATH = 'todos.txt'
"""it Reads a todo items and returns a todo """
def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

"""it take the todo to write on text file"""
def write_todo(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
