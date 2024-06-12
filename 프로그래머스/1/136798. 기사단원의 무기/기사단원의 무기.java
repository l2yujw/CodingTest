class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            int check = sub(i);
            if (check > limit) {
                check = power;
            }
            answer += check;
        }

        return answer;
    }

    public int sub(int num) {
        int count = 0;
        for (int i = 1; i < Math.sqrt(num); i++) {
            if (num % i == 0) {
                count += 1;
            }        }
        count *= 2;
        if (num % Math.sqrt(num) == 0) {
            count += 1;
        }
        return count;
    }
}