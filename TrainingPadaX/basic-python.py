# !/usr/bin/python2
# coding:utf-8

# 題目一：計算最小值到最大值之間，所有整數的總和。
def calculate(min, max):
    sum=0
    for item in range(min, max+1):
        sum = sum + item
    print(sum)
    return sum

calculate(1, 3)     #你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)     #你的程式要能夠計算 4+5+6+7+8，最後印出 30
 



# 題目二：正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
    count=data["count"]
    sum=0
    for employees in data["employees"]:
        sum=sum+employees["salary"]
    avgSalary = sum/count
    print(avgSalary)
    return avgSalary

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})      #呼叫 avg 函式




# 題目三：找出至少包含兩筆整數的列表(Python) 或陣列(JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    maxProduct = nums[0] * nums[1]
    idx=0
    for i in nums[0:len(nums)-1]:
        idx+=1
        for j in nums[idx:len(nums)]:
            product=i * j
            if product > maxProduct:
                maxProduct=product
    print(maxProduct)
    return maxProduct


maxProduct([5, 20, 2, 6])   #得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) #得到 30 因為 10 和 3 相乘得到最大值



# 題目四：
#     Given an array of integers, show indices of the two numbers such that they add up to a
#     specific target.You can assume that each input would have exactly one solution, and you
#     can not use the same element twice.
def twoSum(nums, target):
    x=0
    while x < len(nums)-1:   
        y=x+1     
        while y < len(nums):
            # print(nums[x], nums[y])
            if nums[x]+nums[y]==target:
                # print(nums[x], nums[y])
                return [x, y]
            y+=1
        x+=1

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9




# 題目五：給定只會包含 0 或 1 兩種數字的列表(Python) 或陣列(JavaScript) ，計算連續出現 0 的最大長度。
def maxZeros(nums):
    currentLen=0
    maxLen=0
    for a in  nums:
        if a == 0:
            currentLen+=1
            if currentLen > maxLen:
                maxLen=currentLen
        else:
            currentLen=0
    print(maxLen)
    return maxLen

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0