class Solution {
    public int solution(String t, String p) {
        int answer = 0;

        for (int i = 0; i <= t.length() - p.length(); i++) {
            long partT = Long.parseLong(t.substring(i, i + p.length()));
            if (partT <= Long.parseLong(p)) {
                answer += 1;
            }
        }

        return answer;
    }
}