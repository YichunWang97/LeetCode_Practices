# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 示例 1：

# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：

# 输入：digits = ""
# 输出：[]
# 示例 3：

# 输入：digits = "2"
# 输出：["a","b","c"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#########################################################################################
# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		# 注意边界条件
		if not digits:
			return []
		# 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
		# 这里也可以用map，用数组可以更节省点内存
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		# 最终输出结果的list
		res = []
		
		# 递归函数
		def dfs(tmp,index):
			# 递归的终止条件，注意这里的终止条件看上去跟动态演示图有些不同，主要是做了点优化
			# 动态图中是每次截取字符串的一部分，"234"，变成"23"，再变成"3"，最后变成""，这样性能不佳
			# 而用index记录每次遍历到字符串的位置，这样性能更好
			if index==len(digits):
				res.append(tmp)
				return
			# 获取index位置的字符，假设输入的字符是"234"
			# 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
			# subString每次都会生成新的字符串，而index则是取当前的一个字符，所以效率更高一点
			c = digits[index]
			# map_string的下表是从0开始一直到9， ord(c)-48 是获取c的ASCII码然后-48,48是0的ASCII
			# 比如c=2时候，2-'0'，获取下标为2,letter_map[2]就是"abc"
			letters = d[ord(c)-48]
			
			# 遍历字符串，比如第一次得到的是2，页就是遍历"abc"
			for i in letters:
				# 调用下一层递归，用文字很难描述，请配合动态图理解
				dfs(tmp+i,index+1)
		dfs("",0)
		return res
  #########################################################################################
  #自己题解：
  
  digits = '234'

  number_list = ['2', '3', '4', '5', '6', '7', '8', '9']
  char_list = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

  res_list = []
  for num in digits:
      if num in number_list:
          key = int(num) - 2

          if len(digits) == 1:
              print(char_list[key])

          if len(digits) > 1:
              res = char_list[key]
              res_list.append(res)

  print(res_list)

  right = range(1, len(res_list))
  final_list = []
  for number in range(1, len(res_list)):
      for i in res_list[number-1]:
          for j in res_list[number]:
              output = i + j
              final_list.append(output)

  # for循环太多，需要运用递归知识
  i = 0
  final_list_1 = []
  while i <= len(res_list) - len(digits):
      for char_1 in res_list[i]:
          for char_2 in res_list[i+1]:
              for char_3 in res_list[i+2]:
                  output = char_1 + char_2 + char_3
                  final_list_1.append(output)
      i += 1
  # for i in res_list[right-1]:
  #     for j in res_list[right]:
  #         output = i + j
  #         final_list.append(output)

  print(final_list)
  print(final_list_1)
