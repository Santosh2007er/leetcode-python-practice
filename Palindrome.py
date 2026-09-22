class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result=False
        revnum=0
        temp=x
        while temp>0:
            remainder=temp%10
            revnum=revnum*10+remainder
            temp=temp//10

        if revnum==x:
            result=True
            return result
        else:
            return result