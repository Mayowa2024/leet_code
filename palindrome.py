class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        flipped=x[::-1]
        return x==flipped
#there is a mathematical way of doing it
def is_palindrome_math(num):
    # Negative numbers are never palindromes (e.g., -121 reversed is 121-)
    if num < 0:
        return False
        
    original = num
    reversed_num = 0
    
    while num > 0:
        # 1. Get the last digit using modulo %
        last_digit = num % 10
        
        # 2. Push the digit onto our reversed number
        reversed_num = (reversed_num * 10) + last_digit
        
        # 3. Chop off the last digit from the original number using floor division //
        num = num // 10
        
    # Check if the original number matches the fully reversed number
    return original == reversed_num

# Example:
print(is_palindrome_math(121))  # Returns True


Solution=Solution()
print(Solution.isPalindrome(303))