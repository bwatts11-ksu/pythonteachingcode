# [ ] create, call and test fishstore() function 
name = "Brandon Watts"
def fishstore(fish, price):
    return f"Fish Type: {fish} costs ${price}"

fish_entry = input("Enter the fish type: ")
price_entry = input("Enter the price of the fish: ")

result = fishstore(fish_entry, price_entry)
print("Hi", name, "fish costs {$1}")