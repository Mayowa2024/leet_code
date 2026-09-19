def sum_even(nums: list[int]) -> int:
    """
    This functions returns the sum of even numbers in a list
    """
    sum=0
    for num in nums:
        if num % 2==0:
            sum += num
    return sum

def count_vowels(s: str) -> int:
    vowels=["a","e","i","o","u"]
    count=0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]


nums = [2, 7, 11, 15]
target = 17
print(two_sum(nums,target))

        

