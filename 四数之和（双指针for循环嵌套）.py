# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：答案中不可以包含重复的四元组。

# 示例 1：

# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 示例 2：

# 输入：nums = [], target = 0
# 输出：[]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
##################################################################################################
# 网络题解：

nums = [1,0,-1,0,-2,2]
target = 0

nums.sort() # [-2, -1, 0, 0, 1, 2]
# left = 0
# mid = 1
# right = len(nums) - 1
res_list = []
#
# # for i in range(len(nums)):
# #     left = i + 1
# #     mid = i + 2
# #     right = len(nums) - 1
#
# for index, num in enumerate(nums):
#     if left < index < right and index > mid:
#         res = nums[left] + nums[mid] + nums[index] + nums[right]
#         if res > target:
#             right -= 1
#         elif res == target:
#             res_list.append([nums[left], nums[mid], nums[index], nums[right]])
#         else:
#             mid += 1
#             if res < target:
#                 left += 1
#
# print(res_list)

# for i in range(len(nums) - 3):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
#         break
#     if nums[i] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] < target:
#         continue
#     for j in range(i+1, len(nums)-2):
#         if j - i > 1 and nums[j] == nums[j-1]:
#             continue
#         if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
#             break
#         if nums[i] + nums[j] + nums[len(nums)-1] + nums[len(nums)-2] < target:
#             continue
#
#         left = j + 1
#         right = len(nums) - 1
#         while left < right:
#             temp = nums[i] + nums[j] + nums[left] + nums[right]
#             if temp == target:
#                 res_list.append([nums[i], nums[j], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left+1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right-1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#             elif temp > target:
#                 right -= 1
#             else:
#                 left += 1
#
# print(res_list)

nums.sort()
ln = len(nums)
ret = []
if ln < 4:
    print([])
for i in range(0, ln - 3):
    num1 = nums[i]
    for j in range(i + 1, ln - 2):
        num2 = nums[j]
        left = j + 1
        right = ln - 1
        while left < right:
            total = num1 + num2 + nums[left] + nums[right]
            if total == target:
                tmp = [num1, num2, nums[left], nums[right]]
                if tmp not in ret:
                    ret.append(tmp)
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

print(ret)
