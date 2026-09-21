class Solution(object):
    def findMaxAverage(self, nums, k):

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4

solution = Solution()
print(solution.findMaxAverage(nums, k))





print("-----------------------------------")

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()

        for i in range(len(nums)):

            
            if window and window[0] <= i - k:
                window.popleft()

            
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            
            window.append(i)

            
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
    
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

solution = Solution()
print(solution.maxSlidingWindow(nums, k))    
