# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
###############################################################################

# 代碼超時了
nums = [-1, 2, 1, -4]
target = 1

left = 0
right = len(nums) - 1
nums.sort() # [-4, -1, 1, 2]
res_list = []
res_target_list = []

for index, num in enumerate(nums):
    while left + 1 < right:
        if index != right and index != left:
            res = nums[left] + nums[index] + nums[right]
            res_target = target - res
            res_list.append(res)
            res_target_list.append(res_target)
            if res_target > 0:
                left += 1
            if res_target < 0:
                right -= 1
        else:
            break

    # if nums[left] < nums[right]:
    #     left += 1
    # else:
    #     right -= 1

print(res_list)
print(res_target_list)

temp = 0
res_key = 0
final_res = 0
for key, item in enumerate(res_target_list):
    if res_target_list[key] < 0:
        res_target_list[key] = -res_target_list[key]
    min_res = min(res_target_list)
    if res_target_list[key] == min_res:
        res_key = key

for key, item in enumerate(res_list):
    final_res = res_list[res_key]

print(final_res)
########################################################################
# 網絡題解：

ret = float('inf')
nums.sort()
length = len(nums)

for i in range(length - 2):
    left = i + 1
    right = length - 1
    while left < right:
        tmp = nums[i] + nums[left] + nums[right]
        ret = tmp if abs(tmp - target) < abs(ret - target) else ret
        if tmp == target:
            print(target)
        if tmp > target:
            right -= 1
        else:
            left += 1
print(ret)
