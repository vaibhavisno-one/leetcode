class Solution {
    static final int MOD = 1_000_000_007;


    private long modPow(long base, long exp, int mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1)
                result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }

    public int countGoodNumbers(long n) {
        long evenPositions = (n + 1) / 2;  // ceil(n/2)
        long oddPositions = n / 2;         // floor(n/2)
        long part1 = modPow(5, evenPositions, MOD);
        long part2 = modPow(4, oddPositions, MOD);
        long result = (part1 * part2) % MOD;
        return (int) result;
    }
}
