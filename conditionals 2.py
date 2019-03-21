boys_age = int(input("Enter you age:"))

if boys_age >= 21:
    print("you are of the right age")
    payment = boys_age * 100
    print("take","USD "+str(payment))
    print("Please spend your money wisely")
    future = 50 - boys_age
    print("come back in", str(future),"years time for the next payment")
else:
    print("you deserve no money at all")
    tomorrow = 25 - boys_age
    print("Go to your daddy and come back in", tomorrow, "years time")    
       
