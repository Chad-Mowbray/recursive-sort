from get_max import get_max

def bubble_sort(nums: list[int], new_list=None) -> list[int]:
    new_list = new_list if new_list else []
    if len(nums) == 0:
        return new_list
    else:
        # We need to create a copy because get_max mutates the original list.
        # This is an example of a side effect, which should be avoided as much as possible.
        nums_copy = [n for n in nums] 
        max_int = get_max(nums)
        new_list.insert(0, max_int)
        nums_copy.remove(max_int)
        return bubble_sort(nums_copy, new_list)
        

if __name__ == "__main__":
    bubble_sort([9,1])