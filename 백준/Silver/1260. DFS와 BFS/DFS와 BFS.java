import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static int[][] branch;
    public static boolean[] visit;
    public static Queue<Integer> queue;
    public static int N;
    public static int M;
    public static int V;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();

        branch = new int[1001][1001];
        visit = new boolean[1001];

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            branch[a][b] = branch[b][a] = 1;
        }

        dfs(V);
        System.out.println();

        Arrays.fill(visit, false);
        bfs(V);
    }

    public static void dfs(int v) {
        visit[v] = true;
        System.out.print(v + " ");
        for (int i = 1; i <= N; i++) {
            if (branch[v][i] == 1 && !visit[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int v) {
        queue = new LinkedList<>();
        queue.add(v);
        visit[v] = true;
        System.out.print(v + " ");
        while (!queue.isEmpty()) {
            int temp = queue.poll();

            for (int i = 1; i < branch.length; i++) {
                if (branch[temp][i] == 1 & !visit[i]) {
                    queue.add(i);
                    visit[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }
}