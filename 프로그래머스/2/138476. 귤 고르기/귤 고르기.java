import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Arrays.sort(tangerine);

        ArrayList<Integer> arrayList = new ArrayList<>();
        int temp = 0;
        int count = 0;
        for (int i = 0; i < tangerine.length; i++) {
            if (temp == tangerine[i]) {
                count++;
            } else {
                temp = tangerine[i];
                arrayList.add(count);
                count = 1;
            }

            if (i == tangerine.length - 1) {
                arrayList.add(count);
            }
        }

        Collections.sort(arrayList);
        int minus = tangerine.length - k;
        int sum = 0;
        for (int i = 0; i < arrayList.size(); i++) {
            sum += arrayList.get(i);
            if (sum == minus) {
                return arrayList.size() - 1 - i;
            } else if (sum > minus) {
                return arrayList.size() - i;
            }
        }
        return 0;
    }
}