def start_end(func):
    def add_start_end():
        print('Start')
        func()
        print('End')
    return add_start_end

@start_end
def print_apple():
    print('this is an apple')

# start_end(print_apple)()

print_apple()