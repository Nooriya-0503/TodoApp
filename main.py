import PySimpleGUI as sg
from functions import *
import time
import os 


if not os.path.exists("todo.txt"):
    with open("todo.txt","w") as f:
        pass

sg.theme("BlueMono")

#Layout buttons and texts

clock = sg.Text("", key="clock", text_color="Green")
text1 = sg.Text("Type in a To-Do")
input_text = sg.Input(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add", size=(7), mouseover_colors="black")

list_todo = sg.Listbox(get_todos(), key="list", size=(45,10))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")


windows = sg.Window("ToDo App", layout=[[clock],
                                        [text1],
                                        [input_text, add_button],
                                        [list_todo, edit_button, complete_button],
                                        [exit_button]],
                                font=("Helvetica", 20))

# Kind Of BackEnd (Processing)
while True:
    event, values = windows.read(timeout=200)
    windows["clock"].update(time.strftime("%B %d, %Y %X"))
    
    match event:
        case "Add":
            todos_list = get_todos()
            
            todos_list.append(values['todo'] + "\n")
            
            write_todo(todos_list)
            
            windows['list'].update(values=todos_list)
            windows["todo"].update("") #Write key in [] brackets or event


        case "Edit":
            try:
                todo_to_edit = values["list"][0]
                todo_to_write = values["todo"]

                todos_list = get_todos()

                Edit_index = todos_list.index(todo_to_edit)
                todos_list[Edit_index] = todo_to_write + "\n"

                write_todo(todos_list)
                windows["todo"].update("")
                windows["list"].update(todos_list)

            except IndexError:
                sg.popup("Please enter a ToDo", font=("Helvetica", 20), text_color="Red")
           
        case "Complete":
            try:
                todo_to_complete = values["list"][0]
                todos_list = get_todos()
                todos_list.remove(todo_to_complete)
                write_todo(todos_list)
                windows["list"].update(todos_list)
                

            except IndexError:
                sg.popup("Please choose a ToDo to complete", font=("Helvetica", 20), text_color="Red")
           

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

windows.close()
            


