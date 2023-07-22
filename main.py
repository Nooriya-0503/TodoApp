import PySimpleGUI as sg
from functions import *

#Layout buttons and texts

text1 = sg.Text("Tye in a To-Do")
input_text = sg.Input(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add", size=(7))

list_todo = sg.Listbox(get_todos(), key="list", size=(45,10))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")


windows = sg.Window("ToDo App", layout=[[text1],
                                        [input_text, add_button],
                                        [list_todo, edit_button, complete_button],
                                        [exit_button]],
                                font=("Helvetica", 20))

# Kind Of BackEnd (Processing)
while True:
    event, values = windows.read()
    print(event, values)
    match event:
        case "Add":
            todos_list = get_todos()
            
            todos_list.append(values['todo'] + "\n")
            
            write_todo(todos_list)
            
            windows['list'].update(values=todos_list)
            windows["todo"].update("")


        case "Edit":
            todo_to_edit = values["list"][0]
            todo_to_write = values["todo"]

            todos_list = get_todos()

            Edit_index = todos_list.index(todo_to_edit)
            todos_list[Edit_index] = todo_to_write + "\n"

            write_todo(todos_list)
            windows["todo"].update("")
            windows["list"].update(todos_list)
           
        case "Complete":
            todo_to_complete = values["list"][0]
            todos_list = get_todos()
            todos_list.remove(todo_to_complete)
            write_todo(todos_list)
            windows["list"].update(todos_list)
           

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

windows.close()
            


