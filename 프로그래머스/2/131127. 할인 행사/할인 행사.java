import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }

        for (int i = 0; i <= discount.length - 10; i++) {
            Map<String, Integer> map2 = new HashMap<>();
            for (String value : want) {
                map2.put(value, 0);
            }
            for (int j = i; j < i + 10; j++) {
                if (map2.containsKey(discount[j])) {
                    map2.replace(discount[j], map2.get(discount[j]) + 1);
                }
            }
            if (map.equals(map2)) {
                answer++;
            }
        }

        return answer;
    }
}