#1. Two Sum(Given a list of numbers and a target value, return the indices of two numbers whose sum equals the target)


        


#2. Top k frequent elements
# nums=[1,2,2,3,1,3,5,2,7]
# top=int(input("How many most frequent element you want to see: "))
# freq={}
# for n in nums:
#         freq[n]=freq.get(n,0)+1
# # print(freq)
# list1=[]
# for k,v in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top]:
#     list1.append((k))
# print(list1)

#OR below is beter approach, its nlogn vs nlog(top), if you use heap you dont need to iterate all the elements 

# import heapq
# nums=[1,2,2,3,1,3,5,2,7]
# top=int(input("How many most frequent element you want to see: "))
# freq={}
# for n in nums:
#         freq[n]=freq.get(n,0)+1
# # print(freq)
# print(heapq.nlargest(top, freq, key=freq.get))
    
    


#3. Group Anagram(Check if two strings contain the same characters in different order.)
# str1= "Sougata"
# str2= "Sgouaat"

# if sorted(str1) == sorted(str2):
#     print("Both are same")
# else:
#     print("Both are not same!")
    

#OR Above is O(nlogn) below 2 are better O(n)

# str1 = "Sougata"
# str2 = "Sgouaat"
# freq1 = {}
# freq2 = {}

# for ch in str1:
#     freq1[ch] = freq1.get(ch,0) + 1

# for ch in str2:
#     freq2[ch] = freq2.get(ch,0) + 1

# if (freq1 == freq2):
#     print("Both are same")
# else:
#     print("Both are not same!")

#OR

# from collections import Counter
# str1 = "Sougata"
# str2 = "Sgouaat"
# if Counter(str1) == Counter(str2):
#     print("Both are same")
# else:
#     print("Both are not same")




#4. Longest Substring Without Repeating Characters




#5. Missing number
# nums = [3,0,1]
# n=len(nums)
# total=0
# for i in nums:
#     total +=i
# missing=(n*(n+1)//2)-total
# print(f"The missing number is: {missing}")

#OR

# nums = [3,0,1]
# n = len(nums)
# missing = (n*(n+1)//2) - sum(nums)
# print(missing)



#6. Merge two sorted lists
# list1=[1,4,2,5]
# list2=[1,4,7,8,4]
# merged_list= sorted(list1 + list2)
# print(merged_list)

#above sol" works but time complexity is O(nlogn), below is better approach O(n+m) which uses two pointer method like merge sort

# list1 = [1,2,4,5]
# list2 = [1,3,4]
# i,j = 0,0
# merged = []
# while i<len(list1) and j<len(list2):
#     if list1[i] <= list2[j]:
#         merged.append(list1[i])
#         i +=1
#     else:
#         merged.append(list2[j])
#         j +=1
# merged.extend(list1[i:])
# merged.extend(list2[j:])
# print(merged)




#7. Product of Array Except Self(ex: nums = [1,2,3,4], Output:[24,12,8,6])
# nums = [1,2,3,4]
# n = len(nums)
# result = [1]*n

# prefix = 1
# for i in range(n):
#     result[i] = prefix
#     prefix *= nums[i]

# suffix = 1
# for i in range(n-1,-1,-1):
#     result[i] *= suffix
#     suffix *= nums[i]

# print(result)


#8. First Non Repeating Character
# str1="Sougataso"
# freq={}
# for n in str1.lower():
#     freq[n]=freq.get(n,0)+1

# for k,v in freq.items():
#     if v==1:
#         print(k)
#         break
    
#OR (Both works in modern system, but the above one might not work on older python version(<3.7) cause it might not count frequency in the same order as the input string)

# str1="Sougataso"
# freq={}
# for n in str1.lower():
#     freq[n]=freq.get(n,0)+1
    
# for n in str1.lower():
#     if freq[n]==1:
#         print(n)
#         break

