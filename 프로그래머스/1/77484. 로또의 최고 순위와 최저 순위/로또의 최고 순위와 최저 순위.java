class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0, 0};

        for (int lotto : lottos) {
            System.out.println(lotto);
            for (int winNum : win_nums) {
                if (winNum == lotto) {
                    answer[0]++;
                    answer[1]++;
                }
            }
            if (lotto == 0) {
                answer[0]++;
            }
        }

        for (int i = 0; i < answer.length; i++) {
            if (answer[i] >= 2) {
                answer[i] = 7 - answer[i];
            } else {
                answer[i] = 6;
            }
        }
        return answer;
    }
}