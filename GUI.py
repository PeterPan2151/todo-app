import functions
import FreeSimpleGUI as Sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

Sg.theme('DarkTeal')

time_label = Sg.Text('', key='time')
label = Sg.Text('Type in a to-do')
input_box = Sg.InputText(tooltip='Enter To-do', key='todo')
add_button = Sg.Button('Add')
list_box = Sg.Listbox(values=functions.read_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = Sg.Button('Edit')
complete_button = Sg.Button('Complete')
exit_button = Sg.Button('Exit')


window = Sg.Window('My To-do app',
                   layout=[
                        [time_label],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]

                    ],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=200)
    window['time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup('Please select an item first', font=('Helvetica', 15))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.read_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup('Please select an item first', font=('Helvetica', 15))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case Sg.WIN_CLOSED:
            break;

window.close()
