#Jaden
#11/11/2021
# This code takes a list of numbers and returns it to the user.
def uniquel(alist):
    unique_list = []
    for i in alist:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

y = [1, 3, 3, 3, 6, 2, 3, 5, 500, 500,]
print(uniquel(y))
        