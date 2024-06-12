import java.util.*;

class Solution {
public int[] solution(int[] answers) {

        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = {0, 0, 0};

        for (int i = 0; i < answers.length; i++) {
            if (first[i % 5] == answers[i]) {
                score[0] += 1;
            }
            if (second[i % 8] == answers[i]) {
                score[1] += 1;
            }
            if (third[i % 10] == answers[i]) {
                score[2] += 1;
            }
        }

        int countMax = 0;
        for (int i = 0; i < score.length; i++) {
            if (score[i] > countMax) {
                countMax = score[i];
            }
        }

        List<Integer> answ = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (countMax == score[i]) {
                answ.add(i + 1);
            }
        }

        int[] answer = new int[answ.size()];
        for (int i = 0; i < answ.size(); i++) {
            answer[i] = answ.get(i);
        }

        return answer;
    }
}