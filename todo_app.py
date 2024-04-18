import functions
import time

print(f'Today is: {time.strftime("%b %d, %Y %H:%M:%S")}')

while True:
    action = input("Type add, show edit, complete or exit:").strip()
    # Depending on the input, we perform a certain block of code.
    if action.startswith('add'):
        # The user is expected to enter their to-do with the word 'add' on the start.
        # This line just takes in count the input only from index 4 and on, excluding the word 'add'
        todo = action[4:] + '\n'

        todos = functions.read_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif action.startswith('show'):
        todos = functions.read_todos()

        # Give a presentation to the to-dos that were read from the read_todos function
        # We use enumerate just to print them with their indexes for the user. The index is modified for user.
        for index, to_do in enumerate(todos):
            print(f"{index + 1}. {to_do}", end='')

    elif action.startswith('complete'):
        try:
            index = int(input("What todo number is completed? "))
            todos = functions.read_todos()
            # Since the user sees the index incremented by 1, we subtract 1 to pop the correct to-do index.
            removed_todo = todos[index - 1]

            todos.pop(index - 1)

            functions.write_todos(todos)
            print(f"To-do '{removed_todo.strip('\n')}' was removed from the list")

        # Just in case user enters an index that doesn't exist, we catch that error.
        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith('edit'):
        try:
            # We expect to get 'edit' followed by the number of the to-do to edit. Ex: 'edit 2'
            todo_to_edit = int(action[5:])

            todos = functions.read_todos()

            new_todo = input("Enter a new todo: ") + '\n'
            # Replaced
            todos[todo_to_edit - 1] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            continue

    elif action.startswith('exit'):
        break

    else:
        print("Invalid option.")
