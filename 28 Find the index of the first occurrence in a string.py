class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            print(haystack.index(needle))
        else:
            print(-1)



    





a = Solution()

a.strStr(haystack= "leetcode", needle= "leeto")