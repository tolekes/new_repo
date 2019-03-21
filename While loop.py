# name = "adaku"

# index = 0
# while index < 5:
#     print(name[index])
#     index += 1


py_class_stud = ""
response = ""

while True:
    response = input("please enter your name:")
    if response == "end":
        break    
        
    py_class_stud += response if len(py_class_stud) == 0 else "," + response

print(py_class_stud)


