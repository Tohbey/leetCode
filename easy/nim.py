class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# the idea is once the stones is divisable by 4 your friend automatically wins.
# number of stones => 1 2 3 4 5 6 7 8 9 10 11 12
# status           => W W W L W W W L W W  W   L
