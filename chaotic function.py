#program to evaluate a chaotic behaviour



def chao():
    x= float(input("Enter the value of x between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

chao()    



