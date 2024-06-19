class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];

        int zero = 0;
        int count = 0;
        while (!s.equals("1")) {
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    zero++;
                }
            }
            s = s.replace("0", "");
            s = change(s);
            count++;
        }
        answer[0] = count;
        answer[1] = zero;
        return answer;
    }

    public String change(String s) {
        int c = s.length();
        return Integer.toBinaryString(c);
    }
}