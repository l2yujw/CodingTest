class Solution {
    public long solution(int n) {
        long[] a = new long[n + 1];
        a[0] = 1;
        a[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            a[i] = (a[i - 1] + a[i - 2]) % 1234567;
        }
        return a[n];
    }
}