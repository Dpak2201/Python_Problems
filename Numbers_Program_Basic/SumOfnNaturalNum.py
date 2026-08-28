class negativenumberexception(Exception):
    pass
class SumOfnNaturalNumbers:
    def __init__(self,rangeofnum):
        self.rangeofnum = rangeofnum
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
N=SumOfnNaturalNumbers(-10)
print(N.sumofn())