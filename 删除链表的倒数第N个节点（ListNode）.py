# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 进阶：你能尝试使用一趟扫描实现吗？

# 示例 1：

# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：

# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：

# 输入：head = [1,2], n = 1
# 输出：[1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
##############################################################################
# 题解：

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 新建空白的ListNode并且填入head
        dummy = ListNode(None)
        dummy.next = head 

        # 計算長度
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        
        # 找到倒數第n個節點的前面一位節點
        current = dummy
        for _ in range(count - n):
            current = current.next

        #跳過倒數第n個節點
        current.next = current.next.next
        return dummy.next 

# 作者：wu-xian-sen-2
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/san-chong-fang-fa-shan-chu-dao-shu-di-nge-jie-dian/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
