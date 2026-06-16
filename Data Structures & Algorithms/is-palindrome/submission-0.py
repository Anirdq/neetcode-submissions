class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for ch in s:
            if ch.isalnum():
                filtered.append(ch.lower())
        A = "".join(filtered)

        left, right = 0 , len(A)-1
        
        while left < right:
            if A[left] != A[right]:
                return False
            left+=1
            right-=1
        return True
            