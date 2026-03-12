# 1. Find the duplicate integers in a list of integers.
# nums=[1,4,2,2,3,4]
# seen = set()
# duplicate=[] #make duplicate set instead of list if only unique duplicate nums are need to be shown 
# for n in nums:
#     if n in seen:
#         duplicate.append(n)
#     else:
#         seen.add(n)
        
# print(duplicate)



# 2. Find the common integers between two lists of integers.
# list1 = [1, 2, 3, 4, 5]
# list2= [4, 5, 6, 7, 8]
# common = set(list1) & (set(list2))
# print(common)



# 3. sort in descending order
# nums = [5, 1, 8, 2]
# #print(sorted(nums, key=lambda x: -x))
# nums.sort(reverse=True)
# print(nums)

#OR upper one is better approach with (reverse=True), because time complexity for all are same O(nlogn), space complexity is O(1) which is better than rest 2 which is O(n)

# def rev(s):
#     return s[::-1]

# num=[1,5,3]
# num.sort()
# print(rev(num))



# 4. WAP to find the largest, smallest of three numbers entered by the user.
# for i in range(3):
#     num=int(input("Enter a number: "))
#     if i==0:
#         largest=num
#         smallest=num
#     elif num>largest:
#         largest=num
#     elif num<smallest:
#         smallest=num
# print("The largest number is:", largest)
# print("The smallest number is:", smallest)



####################################################
            #List Problems
####################################################

#5. Remove duplicates
# list1=[1,4,2,2,3,2,4]
# list2=set(list1)
# print(list2)
# # list2=list(dict.fromkeys(list1))
# # print(list2)

        


#6. Reverse a list
# list1=[1,5,2,3,2,4]
# print(list1[::-1])




#7. Find second largest number
# list1=[10,8,5]
# largest1=float("-inf")
# largest2 = float("-inf")
# for n in list1:
#     if n > largest1:
#         largest2=largest1
#         largest1 = n
#     elif largest1> n > largest2:
#         largest2 = n
# if largest2==float("-inf"):
#     print("All elemnts are same")
# else:
#     print(f"2nd Largest number is: {largest2}")
       
#OR(above is more efficient O(n) vs O(nlogn))

# list1=[1,5,5,3,2,1]
# list2=list(set(list1))
# list2.sort()
# print(list2[-2])



#8. Count frequency of elements
# list1=[1,2,4,2,5,3]
# list2=set(list1)
# for n in list2:
#     print(f"{n} appears {list1.count(n)} times")

#OR Below is better approach O(n^2) vs O(n)

# list1=[1,2,4,2,5,3]
# freq={}
# for i in list1:
#     freq[i]=freq.get(i,0)+1
# print(freq)
    



#9. Check if two lists are equal
# list1=[1,4,3,2,3,4,4]
# list2=[1,4,3,2,3,4,4]
# if list1==list2: # if sorted(list1)==sorted(list2): [if order does not matter], if set(list1)==set(list2): [if duplicate does not matter]
#     print("Both lists are equal")
# else:
#     print("lists are not equal")
    
    
    
#10. Merge two lists
# list1=[1,3,2,3,4]
# list2=[1,4,3,4,9]
# #union_list=list(set(list1).union(set(list2)))
# union_list=list(set(list1) | (set(list2))) #Better approach
# #union_list=list1 + list2 #To maintain the order no duplicate removal
# print(union_list)


####################################################
            #Dictionary Problems
####################################################

#11. Count frequency using dict
# list1=[1,4,2,3,2,4,5]
# freq={}
# for n in list1:
#     freq[n]=freq.get(n,0)+1

# print(freq)



#12. Invert a dictionary
# fruit={
#     "apple": "red",
#     "banana": "yellow",
#     "Orange": "Orange",
#     "Cherry": "red"
#     }
# dict1={}

# for k,v in fruit.items():
#     if v not in dict1:
#         dict1[v]=[]
#     dict1[v].append(k)

# print(dict1)

#OR 

# fruit={
#     "apple": "red",
#     "banana": "yellow",
#     "Orange": "Orange",
#     "Cherry": "red"
#     }
# dict1={}

# for k,v in fruit.items():
#     dict1.setdefault(v, []).append(k)

# print(dict1)



#13. Sort dictionary by value in desc
# fruit={
#     "apple": 5,
#     "banana": 10,
#     "orange": 5,
#     "cherry": 2
# }
# print(dict(sorted(fruit.items(), key=lambda x: x[1],reverse=True)))



#####################################################
            #Set Problems
#####################################################

#14. Find intersection of two lists
# list1=[1,4,2,4,3,4,5]
# list2=[1,4,3,4,5,6,7]
# com= set(list1) & set(list2)
# print(com)



#15. Find difference(Which elements exist in the first set but not in the second set?)
# set1={1,2,3,4,5}
# set2={4,3,6,7}
# print(set1.difference(set2))
# #print(set1-set2)



#16. Unique elements
# list1=[1,2,2,3,2,4,5,4]
# print(set(list1))



####################################################
            #String Handling
####################################################

#17. Reverse a string
# name="Sougata"
# print(name[::-1])



#18. Check palindrome
# word=input("Enter the word: ").lower()
# if word==word[::-1]:
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"{word} is not a palindrome")



#19. Count vowels
# name="Sougata"
# vowels=['a','e','i','o','u']
# count=0
# for n in name.lower():
#     if n in vowels:
#         count+=1
# print(count)

#OR

# name="Sougata"
# vowels=['a','e','i','o','u']
# count={}
# for n in name.lower():
#     if n in vowels:
#         count[n]= count.get(n,0)+1

# print(f"Total Vowel Count is: {sum(count.values())}")
# print(count)



#20.Remove spaces
# line="How are you?"
# line= line.replace(" ", "")
# print(line)



#21. Split and join
# line="How are you?"
# line= "_".join(line.split())
# print(line)



#22. Find duplicate characters
# name="Sougatata"
# seen=set()
# dup=[] #make 'dup' set instead of list if only unique duplicate nums are need to be shown 
# freq={}
# for i in name.lower():
#     if i in seen:
#         dup.append(i)
#         freq[i]=freq.get(i,0)+1
#     else:
#         seen.add(i)

# print(dup)
# print(freq)



#24. Character frequency
# name="Sougata"
# freq={}
# for i in name.lower():
#     freq[i]=freq.get(i,0)+1
# print(freq)



#################################################################################################
            #List Comprehension[['expression' for 'item' in 'iterable' if condition]]
#################################################################################################

#25. Square numbers using list comprehension
# list1 = [1,7,3,2]
# list2 = [n**2 for n in list1]
# print(list2)

#OR below is normal python logic

# list1=[1,7,3,2]
# list2=[]
# for n in list1:
#     list2.append(n ** 2)
# print(list2)



#26. Filter even numbers
# list1 = [1,7,3,4,2]
# list2=[n for n in list1  if n%2==0]
# print(list2)



#27. Nested list comprehension
#i) Create a list of all coordinate pairs (x, y) where: x ranges from 0 to 2 and y ranges from 0 to 2
# list1=[(i,j) for i in range(0,3) for j in range(0,3)]
# print(list1)

#OR

# list1=[]
# for i in range(0,3):
#     for j in range(0,3):
#         nums=(i,j)
#         list1.append(nums)
# print(list1)


#ii) Flatten a Nested List
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# list2=[j for i in matrix for j in i ]
# print(list2)

#OR

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# flat_list = []

# for row in matrix:
#     for num in row:
#         flat_list.append(num)
# print(flat_list)


#iii) Create a list containing the products of numbers from 1 to 3 multiplied by numbers from 1 to 3
# list1 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list1)

#OR

# list1=[]
# for i in range(1,4):
#     for j in range(1,4):
#         list1.append(i*j)
# print(list1)



#28. print duplicate no and how many duplicates are there
# list1=[1,1,3,2,1,4,2]
# seen=set()
# dup=[]
# for n in list1:
#     if n in seen:
#         dup.append(n)
#     else:
#         seen.add(n)
# print(dup)
# freq={}
# for n in dup:
#     freq[n]=freq.get(n,0)+1
# print(freq)