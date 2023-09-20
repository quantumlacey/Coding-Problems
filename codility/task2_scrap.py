
# ###### TASK 2 #####
# def task2(A):
#     def task2code(A):
#         concat = ""
#         used_letters = {}
#         concat_strings = []

#         for string in A:

#             useString = True
#             letter_list = []
            
#             #check if string has any repeating characters
#             for letter in string:
#                 letter_count = string.count(letter)
#                 #repeating letters, don't use string
#                 if letter_count > 1:
#                     useString = False
#                     break
#                 #unique letter, append to list
#                 elif letter_count == 1:
#                     #need to check if it's in dict
#                     if letter in used_letters:
#                         useString = False
#                         break
#                     else:
#                         letter_list.append(letter)
            

#             if useString:
#                 #append letters in letter_list to dictionary
#                 for letter in letter_list:
#                     used_letters[letter] = letter
#                 concat += string
#         concat_strings.append(concat)    
#         return concat_strings

#     A = ["abc","yyy","def","csv"]
#     print(task2code(A))





