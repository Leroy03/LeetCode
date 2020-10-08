class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bi = bin(N)[2:]
        ans = [(int(i) + 1) % 2 for i in bi]
        ans_bi = ""
        for i in ans:
            ans_bi += str(i)
        return (int(ans_bi, 2))
