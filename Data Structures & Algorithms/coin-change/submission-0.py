class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([0])
        visit = set([0])
        numCoin = 0
        if amount == 0:
            return 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                val = queue.popleft()
                for coin in coins:
                    val_next = val + coin

                    if val_next == amount:
                        numCoin += 1
                        return numCoin

                    if val_next > amount:
                        continue

                    if val_next not in visit:
                        queue.append(val_next)
                        visit.add(val_next)
                
            numCoin += 1
        
        return -1