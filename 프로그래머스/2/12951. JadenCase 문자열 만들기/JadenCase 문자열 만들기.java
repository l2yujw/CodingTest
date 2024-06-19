class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        s = s.toLowerCase();
        boolean flag = true;

        for (char c : s.toCharArray()) {
            if (c == ' ') {
                flag = true;
            } else if (flag) {
                c = Character.toUpperCase(c);
                flag = false;
            }
            answer.append(c);
        }

        return answer.toString();
    }
}