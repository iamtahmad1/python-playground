class Solution:
    def __init__( self, number: int ):
        self.number = number

    def subtractProductAndSum(self):
        list_of_digits = list(map(int, str(self.number)))
        sum=0
        product=1
        for i in list_of_digits:
            sum=sum+i
            product=product*i
        return(product-sum)