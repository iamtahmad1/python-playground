class Solution:
    def __init__( self, number: int ):
        self.number = number

    def hammingWeight(self):
        n=format(self.number, "b").zfill(33)
        n=str(n)
        count=0
        for i in n:
            if i == "1":
                count+=1
        print(count)

            