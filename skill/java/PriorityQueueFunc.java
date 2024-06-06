import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

public class PriorityQueueFunc {
    public static void main(String[] args) {
        PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();
        PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());

        priorityQueueLowest.add(1);			//큐에 삽입
        priorityQueueLowest.poll();			//최소힙의 첫번째 값 반환 (가장 작은 수) 하고 제거
        priorityQueueLowest.peek();			//최소힙의 첫번째 값 반환 (가장 작은 수)

        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            // 만일 2차원 배열의 첫 번째 원소가 같다면, 2번째 원소를 기준으로 내림차순 정렬한다.
            if(o1[0] == o2[0]) {
                return Integer.compare(o2[1], o1[1]);
            }
            // 2차원 배열의 첫 번째 원소를 기준으로 오름차순 정렬한다.
            return Integer.compare(o1[0], o2[0]);
        });
        pq.offer(new int[] {5, 2});
        pq.offer(new int[] {3, 3});
        pq.offer(new int[] {1, 4});
        pq.offer(new int[] {1, 5});
        pq.offer(new int[] {7, 5});

        while(!pq.isEmpty()) {
            System.out.println(Arrays.toString(pq.poll())); // [1, 5], [1, 3], [3, 3], [5, 2], [7, 5]
        }
    }
}
