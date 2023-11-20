# # my_str = "bla BLA car"
# # my_list = []
# #
# # temp_list = list(my_str.lower())
# # print(temp_list)
# #
# # for i in temp_list:
# #     if i not in my_list:
# #         my_list.append(i)
# #
# # print(len(my_list))
# #
# # # my_str = "bla BLA car"
# # # my_list = []
# # #
# # # my_str_lower = my_str.lower()
# # #
# # # for char in my_str_lower:
# # #     if char not in my_list:
# # #         my_list.append(char)
# # #
# # # print(my_list)
# #
# # my_str = "bla BLA car"
# # my_list = []
# #
# # for index in range(len(my_str)):
# #     if index % 2 == 0:
# #         my_list.append(my_str[index])
# #
# # print(my_list)
# #
# #
# # my_str = "bla BLA car"
# # str_index = [0, 2, 4, 4, 8]
# # my_list = []
# #
# # for index in str_index:
# #     if index < len(my_str):
# #         my_list.append(my_str[index])
# #
# # print(my_list)
# #
# #
# # my_number = 228989
# # number_str = str(my_number)
# # digits_count = len(number_str)
# #
# # print(digits_count)
# #
# #
# # my_number = 228989
# # maximum  = max(str(my_number))
# # print(maximum)
# #
# # my_number = 123
# # reversed_number = int(str(my_number)[::-1])
# #
# # print(reversed_number)
# #
# #
# # my_number = 3254
# # sorted_number_ascending = int(''.join(sorted(str(my_number))))
# #
# # print(sorted_number_ascending)
# #
# # my_number = 3254
# # sorted_number_descending = int(''.join(sorted(str(my_number), reverse=True)))
# #
# # print(sorted_number_descending)
# #
# #
# # my_list_1 = [1, 2, 3]
# # my_list_2 = [10, 20, 30]
# #
# # my_result = []
# # for i in range(len(my_list_1)):
# #     my_result.append(my_list_1[i])
# #     my_result.append(my_list_2[i])
# #
# # print(my_result)
#
#
#
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30, 40]
#
# my_result = []
# min_length = min(len(my_list_1), len(my_list_2))
#
# for i in range(min_length):
#     my_result.append(my_list_1[i])
#     my_result.append(my_list_2[i])
#
# if len(my_list_1) > len(my_list_2):
#     my_result.extend(my_list_1[min_length:])
# else:
#     my_result.extend(my_list_2[min_length:])
#
# print(my_result)