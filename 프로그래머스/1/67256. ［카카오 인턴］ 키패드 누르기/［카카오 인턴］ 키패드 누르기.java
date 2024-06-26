class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
        int left = 10;
        int right = 12;

        for (int number : numbers) {
            if (number % 3 == 1) {
                sb.append("L");
                left = number;
            } else if (number % 3 == 0) {
                sb.append("R");
                right = number;
            } else {
                if (number == 0) {
                    number = 11;
                }

                int leftDist = Math.abs(number - left) / 3 + Math.abs(number - left) % 3;
                int rightDist = Math.abs(number - right) / 3 + Math.abs(number - right) % 3;

                if (leftDist < rightDist) {
                    sb.append("L");
                    left = number;
                } else if (leftDist > rightDist) {
                    sb.append("R");
                    right = number;
                } else {
                    if (hand.equals("left")) {
                        sb.append("L");
                        left = number;
                    } else {
                        sb.append("R");
                        right = number;
                    }
                }
            }
        }
        return sb.toString();
    }
}