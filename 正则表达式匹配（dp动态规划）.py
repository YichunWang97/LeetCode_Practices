# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 示例 1：

# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。

# 示例 2:

# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

# 示例 3：

# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

# 示例 4：

# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

# 示例 5：

# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################################
# 自己题解：（有问题-多种情况下不符合要求）

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(p) != len(s) and p.find('*') == -1 and p.find('.') == -1:
#             return False 
        
#         if p == '.*':
#             return True
        
#         for item_p in range(len(p)):
#             for item_s in range(len(s)):
#                 #if p[0] == s[0] and p[1] == '*':
#                 if len(p) == len(s) and s.find(p[item_p]) != -1 :
#                     return True
#                 if p.find('.*') != -1 and s.find(p[item_p]) == -1:
#                     return False
#                 if s.find(p[item_p]) == -1 and p[item_p] != '*':
#                     if item_p+1 < len(p) and p[item_p+1] == '*':
#                         return True
#                 else:
#                     return False

######################################################################################
# 网络题解：（dp动态规划-内容复杂，需要重复研究）

class Solution(object):
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        #S和P都为空时，匹配
        dp[0][0] = True
        #当S为空，P不空，要看P是否为 a*b*这种结构
        for j in range(1, m + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                #当前字符串是*，可以将 字符+*全部忽略掉，取f[i][j-2]的值
                #或者看模式串P的上一个字符串是否能跟字符串S匹配
                #如果能匹配上，可以忽略掉模式串的 字符+*，也可以忽略掉字符串S中的当前字符
                #这里其实跟递归一样，也有两条转移路径
                if p[j - 1] == "*":
                    if p[j - 2] in (s[i - 1], "."):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                #单个字符匹配的情况        
                else:
                    if p[j - 1] in (s[i - 1], "."):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/liang-chong-shi-xian-xiang-xi-tu-jie-10-48bgj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
