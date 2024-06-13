class Solution {
    public int solution(String s) {
        int answer = 0;
        String check = String.valueOf(s.charAt(0));
        int notX = 0;
        int yesX = 1;
        for (int i = 1; i < s.length(); i++) {
            if (yesX == notX) {
                answer++;
                check = String.valueOf(s.charAt(i));
                notX = 0;
                yesX = 1;
            } else {
                String x = String.valueOf(s.charAt(i));
                if (x.equals(check)) {
                    yesX++;
                } else {
                    notX++;
                }
            }

        }
        return answer + 1;
    }
}