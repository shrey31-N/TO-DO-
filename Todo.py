import modules
import time
time.strftime("%b %d ,%Y - %H:%M:%S")
print(f"the current time is {time.strftime('%b-%d-%Y , %H:%M:%S')}")
while True:

    #it takes user input
    user_input = input("Enter a task wether you want to add,edit, show ,complete or exit : ")
    user_input = user_input.strip()


         #this will allows user to add TODO
    if user_input.startswith("add"):
        todo = user_input[4:]

        #it reads the text file
        todos = modules.get_todo()

        todos.append(todo + '\n')

        # it allows to write todo's in text file
        modules.write_todo(todos)

    #it showes the todo's
    elif user_input.startswith("show"):

        todos = modules.get_todo()

        for index,items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index + 1}---> {items}")

    #it helps to edit the todo
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number -= 1
            try:
                todos = modules.get_todo()
                new_todo = input("you'r new todo: ")
                todos[number] = new_todo + '\n'

                modules.write_todo(todos)

            except IndexError:
                print("You Don't have this number in list")
                continue
        except ValueError:
            print("invalid command")
            continue
    #if the user todo is completed it will remove the todo from the list
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])

            todos = modules.get_todo()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            modules.write_todo(todos)

            message = f"you'r TODO {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("You Don't have this number in list")
            continue
    #it helps to exit from the loop
    elif "exit" in user_input:
        break
    else:
        print("invalid command")
print('\n')
print(" have a good day bye... :)")
