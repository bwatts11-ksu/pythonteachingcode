# [ ] create, call and test the adding_report() function
def adding_reports(report="T"):
    total = 0
    items = ""
    print("Input an integer to add to the total or \"Q\" to quit")

    while True:
        user_input = input("Enter an integer or \"Q\"): ")

        if user_input.isdigit():
            num = int(user_input)
            total += num
            if report == "A":
                items += str(num) + "\n"
        elif user_input.upper().startswith("Q"):
            if report == "A":
                print("Items")

                if items:
                    print(items.strip())
                print("Total", total)
            elif report == "T":
                print("Total", total)
            print("Calculated by: [Brandon Watts]")
            break
        else:
            print(user_input, "is invalid input")
            
# Call the function with "A" for all items + total
adding_reports("A")

print("\n--- New Report ---\n")

# Call the function with "T" for only total
adding_report("T")