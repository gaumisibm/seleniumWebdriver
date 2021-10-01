#classes are user defined blueprint or prototype
# sum, subtraction, multiplication, division
#self keyword is mandatory for calling variables names into method

#methods, class variables, constructor, instance variables


class Calculate:  # When functions are declared inside the class it is called method
    num=100 #class variable

    #self is basically instance of object that is created
    def __init__(self,a,b): # In other oops language constructor name should be same as class name but in python __init__
        self.firstnumber= a; #instance variable
        self.secondnumber= b;
        print("I'll be called everytime object for my class is created")

    #class variable will be constant for each object but instance variable will be dependent on the object parameters

    def sum(self):
        return self.firstnumber+self.secondnumber
    def subs(self):
        return self.firstnumber-self.secondnumber
    def mulp(self):
        return self.firstnumber*self.secondnumber
    def divi(self):
        return self.firstnumber/self.secondnumber

a=Calculate(8,3) # creating obj in python is very simple we don't have to use any kind of new() operator
print(a.divi())
print(a.subs())
print(a.mulp())
print(a.sum())



#Constructor
#It is a method which is called whenever object is created, If you have created constructor then it'll called
#else default constructor will be called.



