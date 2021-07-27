# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

 

# 示例 1：

# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：

# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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
    # print(temp_set)
    if len(temp_set) == 1:
        res_str += temp[0]
        # print(temp[0])
    else:
        break

print(res_str)
