FILEPATH = "todo.txt"

def get_todos(FILEPATH="todo.txt"):
    """This function returns the list of ToDo items"""
    with open(FILEPATH, "r") as f:
        r = f.readlines()
    return r 

def write_todo(todo_to_write, FILEPATH="todo.txt"):
    """This function write todos in file"""
    with open(FILEPATH, "w") as f:
        f.writelines(todo_to_write)


# This is executed when This is is execut
if __name__=="__main__":
    todo = input("Enter Todo To Add: ")
    write_todo(todo)
    print(get_todos())

