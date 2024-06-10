import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings);
        Arrays.sort(strings, Comparator.comparing((String o) -> o.charAt(n)));
        return strings;
    }
}