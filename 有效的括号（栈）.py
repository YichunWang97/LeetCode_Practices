# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
 

# 示例 1：

# 输入：s = "()"
# 输出：true
# 示例 2：

# 输入：s = "()[]{}"
# 输出：true
# 示例 3：

# 输入：s = "(]"
# 输出：false
# 示例 4：

# 输入：s = "([)]"
# 输出：false
# 示例 5：

# 输入：s = "{[]}"
# 输出：true

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
###############################################################################
# 网络题解：

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_dic = {')':'(', ']':'[', '}':'{'}
        temp_list = []

        for ch in s:
            if ch in '([{':
                temp_list.append(ch)
            elif ch in ')]}':
                # 右括号比左括号先出现, 不能闭合
                if not temp_list:
                    return False

                # 遇到右括号, 必然要与上一个左括号闭合, 如果不匹配就 False
                if match_dic[ch] == temp_list[-1]:
                    temp_list.pop(-1)
                else:
                    return False
        # 正常闭合的情况下, 栈里面应该全都弹出去了, 所以应该是空的
        if not temp_list:
            return True
        else:
            return False
