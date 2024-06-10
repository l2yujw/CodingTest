import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int num = 0;
        for (int[] command : commands) {
            int i = command[0] - 1;
            int j = command[1] - 1;
            int k = command[2] - 1;
            int[] temp = new int[j - i + 1];
            for (int l = i; l < j + 1; l++) {
                temp[l - i] = array[l];
            }
            Arrays.sort(temp);
            answer[num++] = temp[k];
        }
        return answer;
    }
}