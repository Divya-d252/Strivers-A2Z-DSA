# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def arraySortedOrNot(self, arr, n):
        flag=True
        for i in range(1,n):
            if(arr[i]<arr[i-1]):
                flag=False
                break
        return flag
      
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
      
class Solution:
    def check(self, arr: List[int]) -> bool:
        flag=True
        rotate_check=0
        for i in range(1,len(arr)):
            if(arr[i]<arr[i-1]):
                rotate_check+=1
                if(rotate_check==2):
                    flag=False
                    break
        if(rotate_check==1):
            if(arr[-1]>arr[0]):
                flag=False
        return flag
