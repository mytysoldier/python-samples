def print_text_twice(text):
    def add_exclamation(text):
        return text + '!'
    
    text_e = add_exclamation(text)
    print(text)
    print(text_e)

print_text_twice('this is an apple')