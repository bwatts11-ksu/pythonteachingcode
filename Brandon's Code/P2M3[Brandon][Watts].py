def word_mixer(original_list):
    
    original_list.sort()  
    new_list = []

    while len(original_list) > 5:
        new_list.append(original_list.pop())
        if len(original_list) >= 5:
            new_list.append(original_list.pop(-5))
        new_list.append(original_list.pop(0))
        if original_list:
            new_list.append(original_list.pop())
        new_list.append("\n")

    return new_list

print("Welcome [Brandon Watts]")
poem_input = input("enter a saying or poem: ")


words = []
for word in poem_input.split():
    cleaned_word = word.strip(".,!?;:")
    words.append(cleaned_word)

for i in range(len(words)):
    if len(words[i]) <= 3:
        words[i] = words[i].lower()
    elif len(words[i]) >= 7:
        words[i] = words[i].upper()

mixed_poem = word_mixer(words)
print("".join(mixed_poem))