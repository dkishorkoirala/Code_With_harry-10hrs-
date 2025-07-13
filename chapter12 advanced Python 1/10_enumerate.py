l = [3, 4,53, 343,342]

# index = 1
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

#this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")