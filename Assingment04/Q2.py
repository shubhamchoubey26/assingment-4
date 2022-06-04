from tokenize import Triple


num_list = [1, 2, 3, 4, 5, 6, 7]

def triple(lst):
     return lst * 3

data = list(map(triple,num_list))
print(data)

