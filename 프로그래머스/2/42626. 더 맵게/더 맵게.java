import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        Arrays.sort(scoville);
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i : scoville) {
            q.add(i);
        }

        while (!q.isEmpty()) {
            if (q.size() > 1) {
                Integer first = q.poll();
                if (first < K) {
                    Integer second = q.poll();
                    q.add(first + second * 2);
                    answer++;
                }
            } else {
                Integer poll = q.poll();
                if (poll < K) {
                    return -1;
                }
            }
        }

        return answer;
    }
}