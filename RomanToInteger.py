class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000

        for i in range(len(s)-1):
            if s[i]=="I":
                if s[i+1]=="V" or s[i+1]=="X":
                    num-=I
                else:
                    num+=I
            elif s[i]=="V":
                num+=V
            elif s[i]=="X":
                if s[i+1]=="L" or s[i+1]=="C":
                    num-=X
                else:
                    num+=X
            elif s[i]=="L":
                num+=L
            elif s[i]=="C":
                if s[i+1]=="D" or s[i+1]=="M":
                    num-=C
                else:
                    num+=C
            elif s[i]=="D":
                num+=D
            elif s[i]=="M":
                num+=M
        
        if s[-1]=="I":
            num+=I
        elif s[-1]=="V":
            num+=V
        elif s[-1]=="X":
            num+=X
        elif s[-1]=="L":
            num+=L
        elif s[-1]=="C":
            num+=C
        elif s[-1]=="D":
            num+=D
        elif s[-1]=="M":
            num+=M
        return num