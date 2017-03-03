"""
基本思想：
将字符串中每一个字符当作键，值都为-1存入一个字典
flag保存离当前位置最近的一个重复字符的位置
如果发现重复字符，则改变flag的值
max保存当前无重复子字符串的最大长度。
max=（当前位置-flag）与max的较大值
遍历时将字符的位置存入字典
"""
class Solution(object):
    def lengthOfLongestSubstring(s):

        """

        :type s: str

        :rtype: int

        """

        d={i:-1 for i in s}

        max=0

        n=len(s)

        i=0

        flag=-1

        while i<n:

            if d[s[i]] !=-1:

                flag=d[s[i]] if d[s[i]]>flag else flag

            d[s[i]]=i
            max=i-flag if i-flag>max else max
            i+=1

        return max

