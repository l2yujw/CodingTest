import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        for (int truckWeight : truck_weights) {
            q.add(truckWeight);
        }

        Queue<Integer> crossQ = new LinkedList<>();

        for (int i = 0; i < bridge_length; i++) {
            crossQ.offer(0);
        }

        if (bridge_length == 1) return truck_weights.length;
        if (truck_weights.length == 1) return bridge_length + 1;

        int total = 0;
        while (!q.isEmpty()) {
            total -= crossQ.poll();
            answer++;

            if (total + q.peek() <= weight) {
                total += q.peek();
                crossQ.offer(q.poll());
            } else crossQ.offer(0);
        }

        return answer + bridge_length;
    }
}