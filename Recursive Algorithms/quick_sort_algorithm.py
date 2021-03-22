class Solution:
    def quicksort(self, arr):
        '''
        :type arr: list of int
        :rtype: list of int
        '''

        self.quicksort_helper(arr, 0, len(arr) - 1)
        return arr

    def quicksort_helper(self, arr, left, right):

        if left < right:
            
            pivot_final_resting_position = self.partition(arr, left, right)
            self.quicksort_helper(arr, left, pivot_final_resting_position - 1)
            self.quicksort_helper(arr, pivot_final_resting_position + 1, right)
            


    def partition(self, arr, left, right):
        pivot = arr[right]
        
        print(f"{pivot} is our pivot")


        i = left - 1

        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1

                self.swap(arr, i, j)

        self.swap(arr, i + 1, right)
        return i + 1

    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp


obj = Solution()

arr = [23, 55, 53, 11, 6, 85, 54, 29]


print(obj.quicksort(arr))
