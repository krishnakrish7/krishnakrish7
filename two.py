##nums=list(map(int,input().split()))
##val=int(input())
##for i in nums:
##    for j in nums:
##        if i==val:
##            nums.remove(j)
##print(nums)
nums=list(map(int,input().split()))
val=int(input())
i=0
while i<len(nums):
    if nums[i]==val:
        del nums[i]
        break
    print(len(nums))
