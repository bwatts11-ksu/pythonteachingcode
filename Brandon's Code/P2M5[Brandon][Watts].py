# [] create Element_Quiz
def get_names():
    elements_list = []
    while len(elements_list) < 5:
        element_name = input("Enter the name of an element: ").strip().lower()
        if element_name == "":
            print("Empty input is not allowed. Try again.")
        elif element_name in elements_list:
            print(f"{element_name} was already entered. No duplicates allowed.")
        else:
            elements_list.append(element_name)
    return elements_list

with open("elements1_20.txt", "r") as file:
    elements = [line.strip().lower() for line in file]

user_name = input("Brandon Watts: ")
print(f"Welcome {user_name}! List any 5 of the first 20 elements in the Period table?")

quiz_responses = get_names()

correct_responses = []
incorrect_responses = []
for response in quiz_responses:
    if response in elements:
        correct_responses.append(response)
    else:
        incorrect_responses.append(response)

percentage_correct = len(correct_responses) * 20

print(f"{percentage_correct}% correct")
print("Found:", " ".join(correct_responses))
print("Not Found:", " ".join(incorrect_responses))
