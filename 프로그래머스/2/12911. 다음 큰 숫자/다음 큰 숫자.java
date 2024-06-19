class Solution {
    public int solution(int n) {
        int nCount = countBinary(n);
        int next = n + 1;
        while (true) {
            if (nCount == countBinary(next)) {
                return next;
            } else {
                next++;
            }
        }
    }

    public int countBinary(int next) {
        String binaryString = Integer.toBinaryString(next);
        int nCount = 0;

        for (char c : binaryString.toCharArray()) {
            if (c == '1') {
                nCount += 1;
            }
        }

        return nCount;
    }
}