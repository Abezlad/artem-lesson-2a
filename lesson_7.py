# my_number = 1000
# x = str(my_number).count('0')
# print(x)
#
#
# my_number = 1002000
#
# find_symbol = "0"
# new_list = []
# result = 0
#
# for symbol in str(my_number)[::-1]:
#     if symbol == find_symbol:
#         result += 1
#         new_list.append(symbol)
#     else :
#         break
# print(new_list, len(new_list))
# print(result)
#
#
# my_list_1 = ["q", "w", "e", "r", "t"]
# my_list_2 = ["1", "2", "3", "4", "5"]
#
# my_result = my_list_1[::2] + my_list_2[::2]
#
# print(my_result)
#
# my_list = [1, 2, 3, 4]
# new_list = my_list[1:] + [my_list[0]]
#
# print(new_list)
#
#
# my_list = [1, 2, 3, 4]
#
# first_element = my_list.pop(0)
# my_list.append(first_element)
#
# print(my_list)
#
#
# test_str = "43 більше ніж 34 але менше ніж 56"
# numb_list = []
#
# for word in test_str.split():
#     if word.isdigit():
#         numb_list.append(int(word))
#     else:
#         digit = ""
#         for symbol in word:
#             if symbol.isdigit():
#                 digit = symbol
#
# result = sum(numb_list)
# print(result)
#
# numbers = [2, 4, 1, 5, 3, 9, 0, 7]
# count = 0
#
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > numbers[i - 1] + numbers[i + 1]:
#         count += 1
#
# print(count)
#
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
#
#  for value in my_list:
#      if type(value) == str:
#          new_list.append(value)
#
# print(new_list)


# my_str = "helllllllllllllo"
# res_list = []
#
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         res_list.append(symbol)
#
#print(res_list)


# string1 = "hello"
# string2 = "world"
#
# new_list = list(set(string1) & set(string2))
#
# print(new_list)

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
# res_list = []
#
# for symbol in set(my_str_1).intersection(set(my_str_2)):
#     if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
#         res_list.append(symbol)
#
# print(res_list)

