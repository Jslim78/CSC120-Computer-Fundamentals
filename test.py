#playing with lists
import random

def create_list():

    my_list = []
MAX_LEN = 29

for i in range(MAX_LEN):
    my_list.append(random.randint(1,29))
print(my_list)
create_list()
