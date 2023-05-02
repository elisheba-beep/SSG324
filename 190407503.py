class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n:int
        :rtype:bool
        """
        if n <= 0:
            return False
        
        if n%3!=0 and n!=1:
            return False
        
        if n==3 or n==1:
            return True
        
        return self.isPowerOfThree(n/3)
    
solution = Solution()
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(0))
print(solution.isPowerOfThree(-1))