class Solution {
    public static int sTarget = 0;
    public static int[] sNumbers;
    public int solution(int[] numbers, int target) {
        sTarget = target;
        sNumbers = numbers;

        dfs(0, 0);
        return count;
    }

    public static int count = 0;

    public static void dfs(int v, int total) {
        if (v == sNumbers.length) {
            if (total == sTarget) {
                count++;
            }
            return;
        }

        dfs(v + 1, total + sNumbers[v]);
        dfs(v + 1, total - sNumbers[v]);
    }
}