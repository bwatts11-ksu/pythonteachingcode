# [ ] create, call and test the str_analysis() function  
def str_analysis(test_string): #str_analysis() function
    if test_string.isdigit():
        num = int(test_string)# takes user input
        if num > 99:
            return f'"{test_string}" is a pretty big number'
        else: 
            return f"{num} is a smaller number than expected"

    elif user_input.isalpha():
        return f'"{user_input}" is all alphabetical characters!'

    else:
        return f'"{user_input}" has multiple characters types'

while True:
    user_input = input("Enter word or integer: ").strip()

    if user_input == "":
        print(str_analysis(user_input))
    else:
        print("Input cannot be empty, please enter something.")
