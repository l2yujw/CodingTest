import java.util.LinkedList;
import java.util.Queue;

public class Bfs {
    public static void main(String[] args) {
        int[][] graph = {{}, {2,3,8}, {1,6,8}, {1,5}, {5,7}, {3,4,7}, {2}, {4,5}, {1,2}};
        boolean[] visited = new boolean[9];
        System.out.println(bfs(1, graph, visited));
    }

    public static String bfs(int start, int[][] graph, boolean[] visited) {
        StringBuilder sb =new StringBuilder();
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(start);

        visited[start] = true;
        while (!q.isEmpty()) {
            int newnode = q.poll();
            sb.append(newnode+" -> ");
            for (int i=0; i<graph[newnode].length; i++) {
                int tmp = graph[newnode][i];
                if (!visited[tmp]) {
                    visited[tmp] = true;
                    q.offer(tmp);
                }
            }
        }
        return sb.toString();
    }
}
