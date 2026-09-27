class negativeexeption(Exception):
    pass

class SumOfDigits:
    #sum=0
    #Remainder=0
    def __init__(self,number):
        self.number=number
        self.sum=0
        self.Remainder=0

    #number validation 
    @property #(pass and get the setted value)
    def number(self):
        return self._number
    @number.setter
    def number(self,value):
        if value<0:
            raise negativeexeption("number must be greater than zero")
        else:
            self._number=value#(set the value to the variable)
    def digits(self):
        while self.number>0:
          #SumOfDigits.Remainder = self.number%10
          #SumOfDigits.sum=SumOfDigits.sum+SumOfDigits.Remainder
          self.Remainder=self.number%10
          self.sum=self.sum+self.Remainder
          self.number=self.number//10
        return self.sum

try:
    value=int(input("enter a positive number"))
    if value<0:
        raise negativeexeption("enter a positive number")
except negativeexeption as e:
    print(e)
except ValueError:
    print("enter only integer")
S=SumOfDigits(value)
print(S.digits())  