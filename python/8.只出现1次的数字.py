# _*_coding:utf-8_*_
"""
@Time :    2021/12/26 11:17 下午
@Author:  bill
@File: 8.只出现1次的数字.py.py
@Software: PyCharm
"""

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 

 说明： 

 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 

 示例 1: 

 输入: [2,2,1]
输出: 1


 示例 2: 

 输入: [4,1,2,1,2]
输出: 4 
 👍 2164 👎 0

"""
"""
# 异或
1. 归零律：a ⊕ a = a
2. 恒等律：a ⊕ 0 = a
3. 交换律： a ⊕ b = b ⊕ a
4. 结合律： a ⊕ b ⊕ c = a ⊕ (b ⊕ c) =(a ⊕ b) ⊕ c
5. 自反：a ⊕ b ⊕ a = b
6. d = a ⊕ b ⊕ c 可以推出 a = d ⊕ b ⊕ c.
7.若x是二进制数0101，y是二进制数1011；
则x⊕y=1110
只有在两个比较的位不同时其结果是1，否则结果为0
即“两个输入相同时为0，不同则为1”！
"""


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res = res ^ i
        return res
# leetcode submit region end(Prohibit modification and deletion)
