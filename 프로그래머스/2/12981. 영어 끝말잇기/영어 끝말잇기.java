import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];

        Set<String> record = new HashSet<>();

        record.add(words[0]);
        
        char last = words[0].charAt(words[0].length() - 1);
        for (int i = 1; i < words.length; i++) {
            if (record.contains(words[i]) || last != words[i].charAt(0)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            } else {
                record.add(words[i]);
            }
            last = words[i].charAt(words[i].length() - 1);
        }

        return answer;
    }
}