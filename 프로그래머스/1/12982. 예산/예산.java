import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
        Arrays.sort(d);
        int total = 0;
        for (int a : d) {
            int temp = total + a;
            if (temp > budget) {
                break;
            } else {
                total += a;
                answer += 1;
            }
        }

        return answer;
    }
}