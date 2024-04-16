def hello(name= "friend"):
    print("hello",name)
hello("Owen")
hello()

course = "Platform Computing"
platform = course[0:8]
computing = course[9:18]
print(platform,computing)

# Exercise 
swap = [0,3,4,5,8]
temp = swap[2]
swap[2] = swap[4]
swap[4] =temp
print(swap)

## HW 1 practice
nums = [1, 1, 5, 5, 10, 8, 7]
max_index = 0
min_index = 0
for i in range(1,len(nums)):
    if nums[i] < nums[min_index]:
        min_index = i
    if nums[i] > nums[max_index]:
        max_index = i
print(nums)

temp = nums[min_index]
nums[min_index] = nums[0]
nums[0] = temp

temp2 = nums[max_index]
nums[max_index] = nums[-1]
nums[-1] = temp2
print(nums)

total = 0
for i in range(1,len(nums)-2):
    if nums[0] == nums[1]:
     index_popped = nums.pop(1)
     print(index_popped)  
     total = nums[i] + total
    else:
        total = nums[i] + total
    print(total)
if nums[0] == nums[1]:
    nums.append(index_popped)
    mean = total / (len(nums)-2)
else:
    mean = total / (len(nums)-1)
print(mean)

#Testing my_functions program 
list = [4,6,8,2,4,10]
values_multipled = 1
for i in list:
        values_multipled = values_multipled * i
print(values_multipled)
def centered_average(nums):
    # Remove the largest and smallest values
    nums.remove(max(nums))
    nums.remove(min(nums))
    
    # Calculate the mean average using floor division
    average = sum(nums) // len(nums)
    
    return average

# Test cases
result1 = centered_average([1, 2, 3, 4, 100])
result2 = centered_average([1, 1, 5, 5, 10, 8, 7])

print(result1)  # Output should be 3
print(result2)  # Output should be 5

