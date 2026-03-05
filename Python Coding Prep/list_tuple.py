# 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# movie_names=[]
# for i in range(3):
#     movie_names.append(input("Enter movie name: "))
    
# print(movie_names)




# 2. WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# list1 = [1, 2, 3, 2, 1]
# list2 = list1.copy()
# list2.reverse()
# if list1 == list2:
#     print("The list is a palindrome.")
# else:
#     print("The list is not a palindrome.")

# OR

# list1 = [1, 2, 3, 2, 1]
# if list1 == list1[::-1]:
#     print("The list is a palindrome.")
# else:
#     print("The list is not a palindrome.")



# 3.WAP to count the number of students with the "A" grade in the tuple, Store the above values in a list & sort them from “A” to “D”.
# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))
# list1 = list(tup)
# list1.sort()
# print(list1)



# 4. Sum of the list elements.
# list1=[1,2,3,4,5]
# print(sum(list1))


# 5. Frequency of elements in a list.
# list1 = [1, 2, 3, 2, 1]
# fre = {}
# for n in list1:
#     fre[n] = fre.get(n, 0) + 1
# print(fre)


# OR

# lis1=[1,2,4,6,2,2,3,8]
# for i in set(lis1):
#     print(f"{i} occurs {lis1.count(i)} times")