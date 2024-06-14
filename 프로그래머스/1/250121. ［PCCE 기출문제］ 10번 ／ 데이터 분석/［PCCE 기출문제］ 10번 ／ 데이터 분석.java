import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> extMap = new HashMap<>();
        extMap.put("code", 0);
        extMap.put("date", 1);
        extMap.put("maximum", 2);
        extMap.put("remain", 3);

        ArrayList<Integer> arrayList = new ArrayList<>();

        int sortByNum = extMap.get(sort_by);
        Arrays.sort(data, Comparator.comparingInt(o -> o[sortByNum]));
        int extNum = extMap.get(ext);
        for (int i = 0; i < data.length; i++) {
            if (data[i][extNum] < val_ext) {
                arrayList.add(i);
            }
        }

        int[][] answer = new int[arrayList.size()][4];

        int i = 0;
        for (Integer integer : arrayList) {
            answer[i++] = data[integer];
        }

        return answer;
    }
}