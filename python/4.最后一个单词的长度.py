# _*_coding:utf-8_*_
"""
@Time :    2021/12/23 12:30 上午
@Author:  bill
@File: 4.最后一个单词的长度.py
@Software: PyCharm
"""
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
#
#  单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "Hello World"
# 输出：5
#
#
#  示例 2：
#
#
# 输入：s = "   fly me   to   the moon  "
# 输出：4
#
#
#  示例 3：
#
#
# 输入：s = "luffy is still joyboy"
# 输出：6
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 仅有英文字母和空格 ' ' 组成
#  s 中至少存在一个单词
#
#  Related Topics 字符串 👍 407 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l.pop())
# leetcode submit region end(Prohibit modification and deletion)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        end_index = l - 1
        while end_index >= 0 and s[end_index] == " ":
            end_index -= 1
        start_index = end_index
        while start_index >= 0 and s[start_index] != " ":
            start_index -= 1
        return end_index - start_index
# leetcode submit region end(Prohibit modification and deletion)