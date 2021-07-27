
strs = ["flower","flow","flight"]
common_list = []

# def longestCommonPrefix(strs):
#     for key, strings in enumerate(strs):
#         for index, char in enumerate(strings):
#             if key <= len(strs) - 2:
#                 if strs[key][index] == strs[key + 1][index]:
#                     common_list.append(strs[key][index])
#
#     return common_list
#
#
# print(longestCommonPrefix(strs))

res_str = ""
for temp in zip(*strs):
    # print(temp)
    temp_set = set(temp)
    print(temp_set)
    if len(temp_set) == 1:
        res_str += temp[0]
        print(temp[0])
    else:
        break

print(res_str)