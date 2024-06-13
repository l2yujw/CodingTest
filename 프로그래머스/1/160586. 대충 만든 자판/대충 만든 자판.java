import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];

        Map<String, Integer> minNums = new HashMap<>();

        for (int i = 0; i < keymap.length; i++) {
            for (int j = 0; j < keymap[i].length(); j++) {
                String c = String.valueOf(keymap[i].charAt(j));
                if (minNums.containsKey(c)) {
                    if (minNums.get(c) > j) {
                        minNums.put(c, j + 1);
                    }
                } else {
                    minNums.put(c, j + 1);
                }
            }
        }


        int n = 0;
        for (String target : targets) {
            boolean flag = true;
            int tot = 0;
            for (int i = 0; i < target.length(); i++) {
                String c = String.valueOf(target.charAt(i));
                if (minNums.containsKey(c)) {
                    tot += minNums.get(c);
                } else {
                    flag = false;
                }
            }
            if (flag) {
                answer[n++] = tot;
            } else {
                answer[n++] = -1;
            }        }

        return answer;
    }
}