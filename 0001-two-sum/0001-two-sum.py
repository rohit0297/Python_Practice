class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} # Dictionary to store{number: index}
        
        for i, num in enumerate(nums):
            complement = target - num # Find the required number to reach the target
            if complement in num_dict:
                return [num_dict[complement], i] # Return indices of the two numbers
            num_dict[num] = i # Store the current number and its index   
        return []