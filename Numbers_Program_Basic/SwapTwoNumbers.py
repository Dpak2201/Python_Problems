class swaptwonumbers:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def simpleunpacking(self):
        self.number1,self.number2 =self.number2,self.number1
        return self.number1,self.number2
    def withthirdarugument(self):
        temp=0
        temp=self.number1 
        self.number1=self.number2
        self.number2=temp
        return self.number1,self.number2
    def withairthematicops(self):
        sum=0
        sum=self.number1+self.number2
        self.number1=sum-self.number1
        self.number2=sum-self.number2
        return self.number1,self.number2
s=swaptwonumbers(2,5)
print(s.simpleunpacking())
print(s.withthirdarugument())
print(s.withairthematicops())