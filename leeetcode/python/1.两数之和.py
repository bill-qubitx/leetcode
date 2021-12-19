# _*_coding:utf-8_*_
"""
@Time :    2021/12/19 12:58 下午
@Author:  bill
@File: 1.两数之和.py
@Software: PyCharm
"""

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
#  你可以按任意顺序返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#
#  示例 3：
#
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 10⁴
#  -10⁹ <= nums[i] <= 10⁹
#  -10⁹ <= target <= 10⁹
#  只会存在一个有效答案
#
#
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？
#  Related Topics 数组 哈希表 👍 12896 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# 解法1
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# leetcode submit region end(Prohibit modification and deletion)

# 解法2
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict: dict = {}
        nums_dict.update({nums[0]: 0})
        for i in range(1, len(nums)):
            idx = nums_dict.get(target - nums[i])
            if idx is not None:
                return [idx, i]
            nums_dict.update({nums[i]: i})
