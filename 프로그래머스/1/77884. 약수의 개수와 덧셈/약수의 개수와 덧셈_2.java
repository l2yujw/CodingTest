class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            int ans = find(i);
            System.out.println(ans);
            if (ans % 2 == 0) {
                answer += i;
            } else {
                answer -= i;
            }
        }
        return answer;
    }
    
    public static int find(int num) {
        int count = 0;

        double sqrt = Math.sqrt(num);

        for (int i = 1; i < sqrt; i++) {
            if (num % i == 0) {
                count += 1;
            }
        }

        if (num % sqrt == 0) {
            return count * 2 + 1;
        }

        return count * 2;
    }
}