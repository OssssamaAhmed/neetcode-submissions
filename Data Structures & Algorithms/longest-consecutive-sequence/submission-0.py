class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_list = set(nums)
        longest_streak = 0
        
        for n in num_list:
            if n-1 in num_list:
                continue

            current_streak = 1
            while n + current_streak in num_list:
                current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak

        return longest_streak