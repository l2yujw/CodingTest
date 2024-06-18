import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, Integer> id = new HashMap<>();
        int i = 0;
        for (String friend : friends) {
            id.put(friend, i++);
        }

        int[][] jugoBodgo = new int[friends.length][friends.length];
        for (String gift : gifts) {
            String[] split = gift.split(" ");
            jugoBodgo[id.get(split[0])][id.get(split[1])]++;
        }

        int[] jisoo = new int[friends.length];
        for (int j = 0; j < jugoBodgo.length; j++) {
            int left = 0;
            int right = 0;
            for (int k = 0; k < jugoBodgo.length; k++) {
                left += jugoBodgo[j][k];
                right += jugoBodgo[k][j];
            }
            jisoo[j] = left - right;
        }

        int[] result = new int[friends.length];
        for (int j = 1; j < jugoBodgo.length; j++) {
            for (int k = 0; k < j; k++) {
                if (jugoBodgo[j][k] > jugoBodgo[k][j]) {
                    result[j]++;
                } else if (jugoBodgo[j][k] < jugoBodgo[k][j]) {
                    result[k]++;
                } else {
                    if (jisoo[j] > jisoo[k]) {
                        result[j]++;
                    } else if (jisoo[j] < jisoo[k]) {
                        result[k]++;
                    }
                }
            }
        }

        int answer = 0;
        for (int i1 : result) {
            answer = Math.max(answer, i1);
        }

        return answer;
    }
}