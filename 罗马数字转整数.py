# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
#  
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
# 示例 2:
#
# 输入: "IV"
# 输出: 4
# 示例 3:
#
# 输入: "IX"
# 输出: 9
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/roman-to-integer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     if s == 'IV':
#         return 4
#
#     if s == 'IX':
#         return 9
#
#     if s == 'XL':
#         return 40
#
#     if s == 'XC':
#         return 90
#
#     if s == 'CD':
#         return 400
#
#     if s == 'CM':
#         return 900
#
#     output = 0
#
#     for item in range(len(s)):
#         if item >= 1:
#             if s[item] == 'M':
#                 if s[item - 1] == 'C':
#                     output += 900
#                 else:
#                     output += 1000
#             if s[item] == 'D':
#                 if s[item - 1] == 'C':
#                     output += 400
#                 else:
#                     output += 500
#             if s[item] == 'C':
#                 if s[item - 1] == 'X':
#                     output += 90
#                 else:
#                     if s[item - 1] != 'M':
#                         output += 100
#                     else:
#                         output += 0
#             if s[item] == 'L':
#                 if s[item - 1] == 'X':
#                     output += 40
#                 else:
#                     if s[item - 1] != 'M' and s[item - 1] != 'D':
#                         if s[item - 1] != 'C':
#                             output += 50
#                         else:
#                             output += 0
#             if s[item] == 'X':
#                 if s[item - 1] == 'I':
#                     output += 9
#                 else:
#                     if s[item - 1] != 'M' and s[item - 1] != 'D':
#                         # if s[item - 1] != 'C' and s[item - 1] != 'L':
#                         output += 10
#                     else:
#                         output += 0
#             if s[item] == 'V':
#                 if s[item - 1] == 'I':
#                     output += 4
#                 else:
#                     # if s[item - 1] != 'M' and s[item - 1] != 'D':
#                     #     if s[item - 1] != 'C' and s[item - 1] != 'L':
#                     #         if s[item - 1] != 'X':
#                     #             output += 5
#                     #         else:
#                     #             output += 0
#                     output += 5
#             if s[item] == 'I':
#                 if s[item - 1] != 'M' and s[item - 1] != 'D':
#                     if s[item - 1] != 'C' and s[item - 1] != 'L':
#                         # if s[item - 1] != 'X':
#                         output += 1
#                     else:
#                         output += 0
#         else:
#             if s[0] == 'I':
#                 if s[1] != 'V' and s[1] != 'X':
#                     output += 1
#             if s[0] == 'V':
#                 output += 5
#             if s[0] == 'L':
#                 output += 50
#             if s[0] == 'D':
#                 output += 500
#             if s[0] == 'M':
#                 output += 1000
#
#     return output

######################################################################
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    Roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0

    for item in range(len(s) - 1):
        if Roman_num[s[item]] < Roman_num[s[item + 1]]:
            output -= Roman_num[s[item]]
        else:
            output += Roman_num[s[item]]

    return output + Roman_num[s[-1]]


print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))

