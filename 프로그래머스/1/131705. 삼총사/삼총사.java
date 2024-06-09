class Solution {
    public static int[] numbers;
    public static int answer = 0;
    public int solution(int[] number) {
        numbers = number;
        dfs(0, 0, 0);
        return answer;
    }
    
    public void dfs(int v, int count, int tot) {
        if (count == 3) {
            if (tot == 0) {
                answer += 1;
            }
            return;
        }
        for (int i = v; i < numbers.length; i++) {
            dfs(i + 1, count + 1, tot + numbers[i]);
        }
    }
}