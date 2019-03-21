import datetime

currentDate =  datetime.date.today()
# # print(currentDate)
# # print(currentDate.day)
# # print(currentDate.strftime("%d %y %b"))

# userinput = input("Pls enter your birthday: (dd/mm/yy)")
# birthday = datetime.datetime.strptime(userinput,"%m/%d/%y").date()
# days = currentDate - birthday
# print(days.days)


deadline = input("when is the deadline for your project? :(dd:mm:yy)")
day = datetime.datetime.strptime(deadline,"%d:%m:%y").date()
no_of_days = day - currentDate
print("you have",no_of_days.days, "days before deadline")