# 1. add new key-value pair in a nested dictionary
# word_meanings = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat": "a small animal",
#     "animal":{
#         "cat": "a small animal",
#         "dog": "a loyal animal"
#     }}

# word_meanings["animal"].update({"lion": "king of jungle"})
# print(word_meanings)
# word_meanings["animal"]["lion"] = "king of jungle"
# print(word_meanings["animal"])



# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students?
# subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(subjects))



# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
# marks = {}
# for i in range(3):
#     subject = input("Enter subject name: ")
#     score = int(input("Enter score: "))
#     marks[subject] = score
# print(marks)



# 4. Figure out a way to store 9 & 9.0 as separate values in the set.
# set1 = {9, "9.0"}
# print(set1)



#5. WAP to enter marks of all the subjects from the user and store them in a dictionary.
# n=int(input("Enter how many subjects are there: "))
# marks={}
# for i in range(n):
#     sub=input("Enter the sub name: ")
#     score=int(input("Enter the score: "))
#     marks[sub]=score
# print(marks)