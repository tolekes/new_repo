boys_age = int(input("Enter you age:"))
gratitude = True

if boys_age >= 21:
    print("you are of the right age")
    payment = boys_age * 100
    print("take","USD "+str(payment))
    print("Please spend your money wisely")
    future = 50 - boys_age
    print("come back in", str(future),"years time for the next payment")


    if gratitude:
        print("you are a good child")

        if payment > 3000:
            print("you are now a big boy")
        else:
            print("you are still a cool boy")
    else:
        print("you are an ingrate")        
else:
    print("you are too young")        