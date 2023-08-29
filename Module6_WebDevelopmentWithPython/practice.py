nums1 = (input("Enter the list : ").split())
target = int(input("Enter Target Sum : "))
nums=[]
ans=[]
for i in nums1:
    nums.append(int(i))
for i in range(len(nums)-1):
    if nums[i]+nums[i+1]==target:
        ans.append(i)
        ans.append(i+1)
print(ans)

