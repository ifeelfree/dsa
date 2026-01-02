
def isPalindrome(s: str) -> bool:
    import re
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    print(s)
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True
def demo_is_palindrome():
    print(isPalindrome("Was it a car or a cat I saw?"))

from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        ele_i = numbers[i]
        ele_j = numbers[j]
        ele_sum = ele_i + ele_j
        if ele_sum == target:
            return [i + 1, j + 1]
        elif ele_sum < target:
            i = i + 1
        else:
            j = j - 1

def demo_two_sum():
    numbers = [1, 2, 3, 4]
    target = 3
    print(twoSum(numbers, 3))

def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

def demo_three_sum():
    nums = [-1, 0, 1, 2, -1, -4]
    r_result = threeSum(nums)
    for i in r_result:
        print(i)


if __name__ == "__main__":
    demo_three_sum()