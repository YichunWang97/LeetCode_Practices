# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。
 
# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

# 示例 2：

# 输入：nums = []
# 输出：[]

# 示例 3：

# 输入：nums = [0]
# 输出：[]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
##########################################################################

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 代碼時長超時...
        # left = 0
        # right = len(nums) - 1
        # target_list = []
        # nums.sort()

        # if len(nums) == 3:
        #     if nums[0] + nums[1] + nums[2] == 0:
        #         target_list.append([nums[0], nums[1], nums[2]])

        # if len(nums) > 3: 
        #     for key in range(len(nums)):
        #         while left + 2 < right:
        #             for index in range(left + 1, right):
        #                 if nums[left] + nums[right] + nums[index] > 0:
        #                     right -= 1
        #                 if nums[left] + nums[right] + nums[index] < 0:
        #                     left += 1
        #                 else:
        #                     if index < right:
        #                         target_list.append([nums[left], nums[index], nums[right]])
        
        # return target_list

        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

# 作者：carlsun-2
# 链接：https://leetcode-cn.com/problems/3sum/solution/15-san-shu-zhi-he-ha-xi-fa-shuang-zhi-zh-jk8s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
