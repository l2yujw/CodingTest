import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;

        for (int i = 0; i < s.length(); i++) {
            StringBuilder sb = new StringBuilder(s);
            String rotation = sb.substring(0, i);
            sb.delete(0, i);
            sb.append(rotation);

            if (checkStr(sb)) {
                answer += 1;
            }
        }
        return answer;
    }

    public static boolean checkStr(StringBuilder s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(']', '[');
        map.put(')', '(');
        map.put('}', '{');

        for (int j = 0; j < s.length(); j++) {
            if (stack.isEmpty()) {
                stack.push(s.charAt(j));
            } else {
                if (stack.peek() == map.get(s.charAt(j))) {
                    stack.pop();
                } else {
                    stack.push(s.charAt(j));
                }
            }
        }

        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}