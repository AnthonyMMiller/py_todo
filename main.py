####
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if "add" in user_action:
        todo = user_action[4:] + "\n"
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i + 1}. {item.capitalize()}")
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo:")
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print('Edit successful')
    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
       # for i, item in enumerate(todos):
        #    item = item.strip('\n')
         #   print(f"{i + 1}. {item.capitalize()}")
 #       un = int(input("what item number would you like to mark as complete?"))
 #       with open('todos.txt', 'r') as file:
  #          todos = file.readlines()
    #        rem = todos[un - 1].strip('\n')
     #       todos.pop(un - 1)
        for i, item in enumerate(todos):
            item = item.strip('\n')
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} has been removed from list."
        print(message)
    elif 'exit' in user_action:
        break
print("Bye!")

# Define the initial list of usernames
#usernames = ["john 1990", "alberta1970", "magnola2000"]

# Use list comprehension to calculate the number of characters for each username
#chars = [len(item) for item in usernames]

# Print the list of character counts
#print(chars)