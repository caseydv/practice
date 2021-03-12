from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount,0)])# value, # no. of coins
        d = set([amount])
        while q:
            curr_val, num = q.popleft()
            if curr_val == 0:
                return num
            for c in coins:
                if curr_val - c >= 0 and curr_val-c not in d:
                    q.append((curr_val-c,num+1))
                    d.add(curr_val-c)           
        return -1
