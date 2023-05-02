class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n%3!=0 and n!=1:
            return False
        if n == 1 or n == 3:
            return True
        return self.isPowerOfThree(n/3)
    
    
mySol = Solution()
print(mySol.isPowerOfThree(48907))
print(54%3)
