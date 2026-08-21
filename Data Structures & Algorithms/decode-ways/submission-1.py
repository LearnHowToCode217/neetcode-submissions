class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in dp:
                return dp[i]

            # Take 1 digit
            res = dfs(i + 1)

            # Take 2 digits
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)