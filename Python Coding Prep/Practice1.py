#1. Two Sum

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
    


#3. Group Anagram
#4. Longest Substring Without Repeating Characters

#5. Missing number
# nums=[0,3,1]


#6. Merge two sorted lists
#7. Product of Array Except Self
#8. First Non Repeating Character



#9. Check if two strings contain the same characters in different order
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