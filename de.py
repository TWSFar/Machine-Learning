def subsets(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    
    return output



nums = [1, 2, 3, 4]
subsets(nums)
