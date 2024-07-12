class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [(i + 1) for i in range(n)] 
        step = k
        k -= 1 # 0-based indexing 
        while(len(friends) > 1):
            k %= len(friends)
            # print("k: ", k , "friends: ", friends)
            friends.pop(k)
            k += (step - 1)
        return friends[0]

