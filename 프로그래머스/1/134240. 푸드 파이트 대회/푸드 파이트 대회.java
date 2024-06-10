class Solution {
    public String solution(int[] food) {
        StringBuilder leftSb = new StringBuilder();
        StringBuilder rightSb = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            if (food[i] % 2 == 1) {
                for (int j = 0; j < food[i] / 2; j++) {
                    leftSb.append(i);
                    rightSb.append(i);
                }
            } else {
                for (int j = 0; j < food[i] / 2; j++) {
                    leftSb.append(i);
                    rightSb.append(i);
                }
            }
        }
        rightSb.reverse();

        return leftSb.append(0).append(rightSb).toString();
    }
}