import functions
import FreeSimpleGUI as Sg

label = Sg.Text('Hello')
input_box = Sg.InputText(tooltip='Enter To-do', key='todo')
add_button = Sg.Button('Add')


window = Sg.Window('My To-do app',
                   layout=[
                            [label],
                            [input_box, add_button]
                    ],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)

        case Sg.WIN_CLOSED:
            break;

window.close()
