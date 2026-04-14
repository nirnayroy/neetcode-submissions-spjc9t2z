class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            else:
                if amount in dp:
                    return dp[amount]
                else:
                    min_coins = float('inf')
                    for coin in coins:
                        coins_num = dfs(amount-coin)+1
                        if coins_num != 0:
                            min_coins = min(coins_num, min_coins)
                    if min_coins == float('inf'):
                        ans = -1
                    else:
                        ans = min_coins
                    dp[amount] = ans
                    return ans

        ans = dfs(amount)

        return ans