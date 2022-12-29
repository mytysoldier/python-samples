# with open('files/test2.txt', 'w') as f:
#     f.write('あああ\nいいい\nううう')

# with open('files/test2.txt', 'a') as f:
#     f.write('\nえええ\nおおお')

x_list = ['apple', 'orange', 'banana']
s = '\n'.join(x_list)

with open('files/test3.txt', 'w') as f:
    f.writelines(s)