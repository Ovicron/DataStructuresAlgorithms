# Find peak element in an array

def findPeakElement(self, nums: List[int]) -> int:
    low = 0 
    high = len(nums) - 1
    if len(nums) < 3:
        return None

    while low <= high:
        mid = low + (high - low) // 2
        mid_left = nums[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = nums[mid + 1] if mid + 1 < len(nums) else float('inf') 

        if mid_left > nums[mid] and mid_right < nums[mid]:
            high = mid - 1
        elif mid_left < nums[mid] and mid_right > nums[mid]:
            low = mid + 1
        elif mid_left < nums[mid] and mid_right < nums[mid]:
            return mid 
