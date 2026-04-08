class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for ch in s:
            if ch.isalnum():
                ch = ch.lower()
                string = string + ch

        n = math.floor(len(string)/2)
        
        for i in range(n):
            if string[i] != string[-(i+1)]:
                return False
        return True
            
