# Nothing tricky about this haha
def Counter(nums):
    counter = 0
    for i in range(len(nums)):
        counter += nums[i]

    return print(counter)

Counter([1,2,3,4,5,6,7,8,9,10])

# Same thing using enumerate
def CounterEnum(nums):
    counter = 0
    for i, num in enumerate(nums):
        counter += num

    return print(counter)

CounterEnum([1,2,3,4,5,6,7,8,9,10])