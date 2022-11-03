# https://practice.geeksforgeeks.org/problems/quick-left-rotation3806/1
  
class Solution:
    def leftRotate(self, arr, k, n):
        k=k%n
        arr[:]=[*arr[k:],*arr[:k]]
        return arr

# Right Rotation:
  
# https://leetcode.com/problems/rotate-array/
  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=[*nums[n-k:],*nums[:n-k]]
        return nums
