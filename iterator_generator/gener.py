def my_genarator():
    x = 10
    yield x
    x = x + 10
    yield x
    x = x + 10
    yield x

mg = my_genarator()

for x in mg:
    print(x)

print(dir(mg))