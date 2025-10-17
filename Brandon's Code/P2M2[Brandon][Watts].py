# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 

def list_o_matic(item, item_list):
    
    if item == "":
        if item_list:
            popped_item = item_list.pop()
            return f"{popped_item} popped from list"
        else:
            return "List is empty, nothing to pop."
    elif item in item_list:
        item_list.remove(item)
        return f"1 instance of {item} removed from list"
    else:
        item_list.append(item)
        return f"1 instance of {item} appended to list"


my_name = "[Brandon Watts]"  
my_list = ['axolotl', 'capybara', 'tuna']  

print(f"Welcome, {my_name}.")

while True:
    print(f"Look at all the animals {my_list}")
    user_input = input("enter the name of an animal: ").lower()

    if user_input == "quit":
        print("Goodbye!")
        break
    
    message = list_o_matic(user_input, my_list)
    print(message)

    if not my_list:  
        print("Goodbye!")
        break