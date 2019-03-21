class Person:    #class declaration
    mouth = 1   #(class variable or attribute)
    hand = 2
    leg = 2

    def __init__(self, eye_color, skin_color): #initializer for instance variables
        self.eye_color = eye_color
        self.skin_color = skin_color

    def walk(self):
        print("walk walk walk walk")

   

class Politician(Person):   #class declaration
    pass

new_person1 = Person("brown","pale")   #an object (instance of a class)
new_person2 = Person("red","black")
new_person3 = Politician("blue","blue black")


def adder(x,y):      #function
    return x + y




#ENCAPSULATION
class Data:
    def  __init__(self,main_data):
        self.main_data = main_data
        self.length = len(main_data)
        self.unique = str(set(main_data))
        self.mean = self.mean_()
        self.standard = self.Mean_Deviation()

    
      
    def mean_(self):
        MEAN = sum(self.main_data)/self.length
        return MEAN

    def Mean_Deviation(self):
        num = 0
        for i in self.main_data:

            num += abs(i - self.mean)
            print(i,abs(i - self.mean),num)
            
        mean_deviation = num / self.length
        return mean_deviation
         

rand = Data([1,2,5,4,5])  #object instantiation
print(rand.standard)