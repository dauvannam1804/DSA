# https://viblo.asia/p/bai-toan-chia-keo-euler-L4x5xqvqKBM
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C(x):
            return comb(x,2) if x >= 0 else 0

        total = C(n + 2)

        # Trừ những trường hợp a > limit, b > limit, c > limit
        over_a = C(n - limit - 1 + 2)
        over_b = C(n - limit - 1 + 2)
        over_c = C(n - limit - 1 + 2)

        # Cộng lại những trường hợp a, b > limit
        over_ab = C(n - 2 * (limit + 1) + 2)
        over_ac = C(n - 2 * (limit + 1) + 2)
        over_bc = C(n - 2 * (limit + 1) + 2)

        # Trừ những trường hợp a, b, c > limit
        over_abc = C(n - 3 * (limit + 1) + 2)

        return total - (over_a + over_b + over_c) + (over_ab + over_ac + over_bc) - over_abc