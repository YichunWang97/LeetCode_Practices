# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是
# "abc"，所以其长度为
# 3。
#
# 示例
# 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是
# "b"，所以其长度为
# 1。
#
# 示例
# 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是
# "wke"，所以其长度为
# 3。
# 请注意，你的答案必须是
# 子串
# 的长度，"pwke"
# 是一个子序列，不是子串。
#
# 示例
# 4:
#
# 输入: s = ""
# 输出: 0

def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)

    # 初始化左指针和最大长度
    left = 0
    max_length = 0

    # 创建Hash表来跟踪每一个重复字符的位置
    hashMap = {}

    # 移动右指针
    for right in range(len(s)):
        current_char = s[right]

        if current_char in hashMap:
            if hashMap[current_char] + 1 >= left:
                left = hashMap[current_char] + 1

        hashMap[current_char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))

######################################################################
# 通过enumerate查找重复字符划分滑动窗口
# 存在问题：第三个示例结果出错（输出为2）

def lengthOfLongestSubString2(s):
    if len(s) <= 1:
        return len(s)

    left, max_length = 0, 0
    hashMap = {}

    for index, char in enumerate(s):
        if char in hashMap:
            hashMap[char] = index
            max_length = max(max_length, hashMap[char] - left)
            if hashMap[char] + 1 >= left:
                left = hashMap[char] + 1
        else:
            hashMap[char] = index

    return max_length


print(lengthOfLongestSubString2('abcabcbb'))
print(lengthOfLongestSubString2('bbbbb'))
print(lengthOfLongestSubString2('pwwkew'))
