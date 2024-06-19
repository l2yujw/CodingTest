class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        double board = brown + yellow;
        
        for (int i = 3; i <= (int) Math.sqrt(board); i++) {
            if (board % i != 0) {
                continue;
            }
            int m = (int) (board / i);
            if ((i - 2) * (m - 2) == yellow) {
                answer[0] = m;
                answer[1] = i;
                return answer;
            }
        }

        return answer;
    }
}