import functions
import FreeSimpleGUI as Sg

label = Sg.Text('Hello')
input_box = Sg.InputText(tooltip='Enter To-do')
add_button = Sg.Button('Add')


window = Sg.Window('My To-do app', layout=[
    [label],
    [input_box, add_button]
])
window.read()
window.close()
