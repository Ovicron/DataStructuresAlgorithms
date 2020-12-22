# Binary Search to find the index of a target value on a given sorted array

def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
