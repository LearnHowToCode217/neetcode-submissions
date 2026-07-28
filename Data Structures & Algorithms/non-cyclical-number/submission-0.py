class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        while n != 1:
            h = n // 100
            m = (n % 100) // 10
            s = (n % 100) % 10

            n = h**2 + m**2 + s**2
            if n not in hash:
                hash.add(n)
            else:
                return False
        
        return True
        