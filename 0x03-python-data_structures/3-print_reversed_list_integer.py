#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenn = len(my_list)
    while lenn > 1:
        for j in range(lenn - 1):
           #print(f"is {my_list[j]} < {my_list[j + 1]}")
            if my_list[j] < my_list[j + 1]:
                #print(f"swap {my_list[j]} and {my_list[j + 1]}")
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
            #else:
               # print(f"Dont swap {my_list[j]} and {my_list[j + 1]}")
        lenn -= 1
        #print("END OF LOOP")
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
