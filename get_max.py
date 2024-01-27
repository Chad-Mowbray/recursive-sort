

def get_max(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        if nums[0] <= nums[1]:
            return get_max(nums[1:])
        elif nums[1] < nums[0]:
            nums.pop(1) # This mutates the original list
            return get_max(nums)
            
            
