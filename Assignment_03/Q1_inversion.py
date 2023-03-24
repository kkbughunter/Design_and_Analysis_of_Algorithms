def count_inversions1(nums):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] > nums[j]):
                print("(",nums[i] , nums[j],") ",end="")
num=[3,2,8,1]
count_inversions1(num)