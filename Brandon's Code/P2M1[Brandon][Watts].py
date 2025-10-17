# [] create words after "G" following the Assignment requirements use of functions, methods and keywords
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

def words_after_g(quote_input, name):
    print(f"Welcome, {name}. Wheresoever you go, go with all your heart: {quote_input}")

    current_word = ""
    output_words = []

    for char in quote_input:
        if char.isalpha():
            current_word += char
        else:
            if current_word:
                if current_word.lower() > 'g':
                    output_words.append(current_word.upper())
            current_word = ""

    if current_word:
        if current_word.lower() > 'g':
            output_words.append(current_word.upper())

    print(" ".join(output_words))

my_name = "Brandon"
sample_quote = "Wheresoever you go, go with all your heart"
words_after_g(sample_quote, my_name)