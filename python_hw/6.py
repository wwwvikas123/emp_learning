
my_str = "строка для теста"
my_dict = {}

for n in my_str:
    my_dict[n] = my_dict.get(n,0) + 1
print (my_dict)
