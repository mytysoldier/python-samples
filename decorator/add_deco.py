def start_end(func):
    def add_start_end(*args, **kwargs):
        print('start')
        x = func(*args, **kwargs)
        print('end')
        return x
    return add_start_end

@start_end
def add_exclamation(text):
    print('add_exclamation executed')
    return 'test', text + '!'

result1, result2 = add_exclamation('this is an apple')
print(result1)
print(result2)