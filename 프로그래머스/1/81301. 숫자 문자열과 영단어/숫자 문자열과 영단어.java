import java.util.*;

class Solution {
    public int solution(String s) {
        StringBuilder sb = new StringBuilder();

        Map<String, String> words = new HashMap<>();
        words.put("zero", "0");
        words.put("one", "1");
        words.put("two", "2");
        words.put("three", "3");
        words.put("four", "4");
        words.put("five", "5");
        words.put("six", "6");
        words.put("seven", "7");
        words.put("eight", "8");
        words.put("nine", "9");

        String temp = "";
        for (int i = 0; i < s.length(); i++) {
            temp += String.valueOf(s.charAt(i));
            if (words.containsKey(temp)) {
                sb.append(words.get(temp));
                temp = "";
            } else if (words.containsValue(temp)) {
                sb.append(temp);
                temp = "";
            }
        }

        return Integer.parseInt(sb.toString());
    }
}