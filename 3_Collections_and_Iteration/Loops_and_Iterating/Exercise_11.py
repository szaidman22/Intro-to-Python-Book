my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

def printer(list):
    index = 0 
    while index < len(my_list):
        innerdex = 0
        while innerdex < len(my_list[index]):
            if my_list[index][innerdex] % 2 == 0:
                print(my_list[index][innerdex])
            innerdex += 1
        index += 1

printer(my_list)