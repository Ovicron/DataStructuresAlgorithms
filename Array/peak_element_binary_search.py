 def findPeakElement(nums: List[int]) -> int:
      low = 0 
      high = len(nums) - 1

      while low <= high:
          mid = low + (high - low) // 2
          
          mid_left = float('-inf') if mid - 1 < 0 else nums[mid - 1]
          mid_right = float('-inf') if mid + 1 == len(nums) else nums[mid + 1]
          
          if nums[mid] > mid_left and nums[mid] > mid_right:
              return mid

          if nums[mid] < mid_left:
              high = mid - 1

          if nums[mid] > mid_left and nums[mid] < mid_right:
              low = mid + 1

      return -1
