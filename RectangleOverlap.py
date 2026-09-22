class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1=rec1[0]
        y1=rec1[1]
        x2=rec1[2]
        y2=rec1[3]
        a1=rec2[0]
        b1=rec2[1]
        a2=rec2[2]
        b2=rec2[3]

        return True if max(x1, a1)<min(x2, a2) and max(y1, b1)<min(y2, b2) else False