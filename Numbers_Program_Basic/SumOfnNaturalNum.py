class negativenumberexception(Exception):
    pass
class SumOfnNaturalNumbers:
    def __init__(self,rangeofnum):
        self.rangeofnum = rangeofnum
#input validation using @property decorator

    @property
    def rangeofnum(self):
        return self._rangeofnum
    @rangeofnum.setter
    def rangeofnum(self,value):
        if value<0:
            raise negativenumberexception("number should be positive integer")
        self._rangeofnum=value
    
    def sumofn(self):
        sum=0
        if self.rangeofnum==0:
            return sum
        elif self.rangeofnum>0:
            for i in range(0,self.rangeofnum+1):
                sum = sum+i
            return sum
        else:
            raise negativenumberexception("range should be a positive integer value")
    def sumusingfor(self):
            sum=0
            if self.rangeofnum>=0:
                sum=(self.rangeofnum*(self.rangeofnum+1))//2
                return sum
            else:
                raise negativenumberexception("enter positive number")
    def sumrecurssion(self,rangeofnum):
        self.rangeofnum=rangeofnum
        sum=0
        if self.rangeofnum==0:
            return 0
        return self.rangeofnum+self.sumrecurssion((self.rangeofnum - 1 ))
    #input validation using @property decorator

    @property
    def rangeofnum(self):
        return self._rangeofnum
    @rangeofnum.setter
    def rangeofnum(self,value):
        if value<0:
            raise negativenumberexception("number should be positive integer")
        self._rangeofnum=value


N=SumOfnNaturalNumbers(6)
#print(N.sumofn()) #timecomplexity= 0(n) , use formula to improve 
print(N.sumusingfor()) #best method time complexity =0(1)
#print(N.sumrecurssion(10))