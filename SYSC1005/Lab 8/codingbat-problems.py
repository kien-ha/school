def first_last6(nums):
    if (nums[0] == 6) or (nums[len(nums)-1] == 6):
        return True
    else:
        return False

def same_first_last(nums):
    if len(nums)>0:
        if nums[0] == nums[len(nums) - 1]:
            return True
        else:
            return False
    else:
        return False
    
def make_pi():
    return [3, 1, 4]

def sum3(nums):
    return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

def max_end3(nums):
    if nums[0]>nums[2]:
        return [nums[0],nums[0],nums[0]]
    else:
        return [nums[2],nums[2],nums[2]]
    
def sum2(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0
    else:
        return nums[0] + nums[1]

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    if (nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3):
        return True
    else:
        return False
    
def count_evens(nums):
    result = 0
    for a in nums:
        if a%2 == 0:
            result += 1
    return result

def big_diff(nums):
    max = nums[0]
    min = nums[0]
    for a in range(len(nums)):
        if nums[a] > max:
            max = nums[a]
        if nums[a] < min:
            min = nums[a]
    return max - min

def has22(nums):
    for x in nums:
        if (nums[y] == 2) and (nums[(y-1)] == 2):
            return True

    return False 