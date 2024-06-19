import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);
        int f = 0;
        int b = people.length - 1;

        for (int i = b; i >= f; i--) {
            if (people[i] + people[f] <= limit) {
                f++;
                answer++;
            } else {
                answer++;
            } 
        }
        return answer;
    }
}