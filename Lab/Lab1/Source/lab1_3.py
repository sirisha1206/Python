nums = list()
num = input("Enter the size of the array:")
print('Enter numbers in array: ')
for i in range(int(num)):
    n = input()
    nums.append(int(n))
print('List of Numbers: ',nums)

triplet_result = []
nums.sort() # sort the numbers in ascending order
r=len(nums)-1 #index of the last number in an array
for i in range(len(nums)-2): # repeat the loop from 1st number to last but one number
    l = i + 1  # start l with value greater than i
    while (l < r): # repeat the loop till l is less than r
        sum = nums[i] + nums[l] + nums[r] # add first two numbers and last number and assign its value to sum variable
        if (sum < 0):
            l = l + 1 #if sum is less than zero then increment l
        if (sum > 0):
            r = r - 1 # if sum is greater than zero then decrement r
        if not sum:  # check if sum is zero
            triplet_result.append([nums[i],nums[l],nums[r]]) # append the triplet list into result variable
            l = l + 1  # increment l when we find a combination whose sum is zero
print('Triplets list: ',triplet_result)