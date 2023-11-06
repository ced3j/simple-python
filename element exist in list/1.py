# Check if element exists in list in Python


lst = [2,4,5,7,10,32,16,71]
x = 10

if x in lst:
    print(f"{x} is exist")
else:
    print(f"{x} is not exist")



print("------------------------")



test_list = [1,4,5,16,6,47,23]
for i in test_list:
    if i == 10:
        print("Element exist")



print("------------------------")


x = [True if 16 in test_list else False]
print(x)


