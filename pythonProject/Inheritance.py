#Acquiring properties of parent class like  variables and method
# you will create a browser invocation code in your parent class and child class will have
from Oops import Calculate


class childImp(Calculate):
    num2=200

    #whenever your parent class constructor has some logic inside it, it should be envoked explicitly
    def  __init__(self):
        Calculate.__init__(self, 10,20)

    def getfulldata(self):
        return self.num2+self.num+self.sum()

b=childImp()
print(b.getfulldata())